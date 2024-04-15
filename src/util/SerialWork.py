import time

import serial
from PySide6 import QtCore
from PySide6.QtCore import QThread, QMutex, QMutexLocker, QWaitCondition

from src.util.ReadThread import ReadThread


class SerialWorker(QThread):
    bRunning = True
    msgThread = QtCore.Signal(str)
    msgRead = QtCore.Signal(str)

    def __init__(self, ComPort, writeNum: str, baudrate=115200):
        super().__init__()

        self.serial_port = None
        self.read_thread: ReadThread = None
        self.comPort = ComPort
        self.BaudRate = baudrate
        self.writeNum = writeNum
        self.mutex = QMutex()
        self.waitCondition = QWaitCondition()

    def consoleWriteBytes(self, sendData: bytes):
        print(f">>>> {' '.join(format(byte, '02X') for byte in sendData)}")
        if self.serial_port is not None:
            self.serial_port.write(sendData)
            time.sleep(0.3)

        else:
            self.ThreadNoti("console is none... ")

    def consoleWrite(self, data: str):
        data = data.replace("\n", "")
        sendData = bytes(data + "\r\n", "UTF-8")

        self.consoleWriteBytes(sendData)

    def stopWork(self):
        self.bRunning = False
        self.waitCondition.wakeAll()

    def ThreadNoti(self, msg: str):
        self.msgThread.emit(f"[{self.comPort} / {self.BaudRate}] {msg}")

    def makeCrc(self, data: bytes):
        crc = 0
        for byte in data:
            crc += byte
        crc ^= 0xFF
        return crc & 0xFF

    def makePacket(self, cmds: bytes) -> bytes:
        headAndData = bytes([0xA5, len(cmds)]) + cmds
        crc = self.makeCrc(headAndData)
        return headAndData + bytes([crc]) + bytes([0x7E])

    def serialRead(self, serialNum):
        print(serialNum)
        self.msgRead.emit(serialNum)

    def run(self):
        with QMutexLocker(self.mutex):
            try:
                self.ThreadNoti("serial try open...")
                self.serial_port = serial.Serial(port=self.comPort, baudrate=self.BaudRate, timeout=3)

                time.sleep(0.4)

                if self.serial_port.isOpen():
                    self.ThreadNoti("console.isOpen!!!")

                    # 00 start read
                    self.read_thread = ReadThread(self.serial_port)
                    self.read_thread.start()

                    # 01 testmode enable
                    onData = self.makePacket(bytes([0x01, 0x01]))
                    self.consoleWriteBytes(onData)
                    self.waitCondition.wait(self.mutex, 10)

                    byte_array = self.writeNum.encode('utf-8')
                    if len(byte_array) < 15:
                        padding_length = 15 - len(byte_array)
                        byte_array += b'\x00' * padding_length
                    elif len(byte_array) > 15:
                        byte_array = byte_array[:15]

                    onData = self.makePacket(bytes([0x07, 0x01]) + byte_array)
                    self.consoleWriteBytes(onData)
                    self.read_thread.msgReadSerial.connect(self.serialRead)
                    self.waitCondition.wait(self.mutex, 10)

                    onData = self.makePacket(bytes([0x01, 0x01]))
                    self.consoleWriteBytes(onData)
                    self.waitCondition.wait(self.mutex, 10)

                    self.ThreadNoti("write complete")
                else:
                    self.ThreadNoti("not open...")

            except Exception as error:
                print(error)
                self.ThreadNoti(str(error))

            finally:
                if self.read_thread is not None:
                    self.read_thread.stop()

                # send Off
                onData = self.makePacket(bytes([0x01, 0x00]))
                self.consoleWriteBytes(onData)
                self.serial_port.close()
