import time

import serial
from PySide6 import QtCore
from PySide6.QtCore import QThread, QMutex, QMutexLocker, QWaitCondition

from src.util.ReadThread import ReadThread


class TempWork(QThread):
    bRunning = True
    msgThread = QtCore.Signal(str)
    msgRead = QtCore.Signal(str)
    msgReadList = QtCore.Signal(list)

    def __init__(self, ComPort, baudrate=115200):
        super().__init__()

        self.comPort = ComPort
        self.BaudRate = baudrate

        self.serial_port = None
        self.read_thread: ReadThread = None
        self.chargingStartWaitTime = 17 * 1000

        self.mutex = QMutex()
        self.waitCondition = QWaitCondition()

    def consoleWriteBytes(self, sendData: bytes):
        print(f"[TempWork]>>>> {' '.join(format(byte, '02X') for byte in sendData)}")
        if self.serial_port is not None:
            self.serial_port.write(sendData)
            time.sleep(0.3)

        else:
            self.ThreadNoti("console is none...")

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

    def ack(self, ack: bytes):
        if len(ack) == 2:
            print(f"[TempWork][cmd:{ack[1]}][result:{ack[0] == 0}]")

    def initStopCharging(self):
        try:
            self.consoleWriteBytes(self.makePacket(bytes([0x04, 0x00])))
            self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x01, self.encodeSignedByte(30)[0], 0x00])))
            self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x02, self.encodeSignedByte(30)[0], 0x00])))
            self.consoleWriteBytes(self.makePacket(bytes([0x06, 0x00])))
            self.waitCondition.wait(self.mutex, 50)
        except Exception as error:
            print(f"[TempWork]initStopCharging Exception {error}")
            self.ThreadNoti(str(error))

    def pushTemp(self, temp: int):
        if temp > 30:
            self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x01, self.encodeSignedByte(30)[0], 0x00])))
            self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x02, self.encodeSignedByte(temp)[0], 0x00])))
        else:
            self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x01, self.encodeSignedByte(temp)[0], 0x00])))
            self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x02, self.encodeSignedByte(30)[0], 0x00])))
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
                    self.read_thread.msgAck.connect(self.ack)
                    self.read_thread.start()

                    # 01 testmode enable
                    print("[TempWork]start Test")
                    self.consoleWriteBytes(self.makePacket(bytes([0x01, 0x01])))
                    self.waitCondition.wait(self.mutex, 50)
                    if not self.bRunning: return

                    # 초기화
                    self.initStopCharging()
                    if not self.bRunning: return

                    # 충전시작
                    self.consoleWriteBytes(self.makePacket(bytes([0x06, 0x01])))
                    self.waitCondition.wait(self.mutex, self.chargingStartWaitTime)
                    if not self.bRunning: return

                    while True:
                        self.waitCondition.wait(self.mutex, 100)
                        if not self.bRunning: return

                    # 충전 중지 및 초기화
                    print("[TempWork]ErrTest::stop charging")
                    self.consoleWriteBytes(self.makePacket(bytes([0x04, 0x00])))
                    self.consoleWriteBytes(self.makePacket(bytes([0x06, 0x00])))
                    if not self.bRunning: return

                    # 충전종료
                    print("[TempWork]stop charging")
                    self.ThreadNoti("write complete")
                else:
                    self.ThreadNoti("not open...")

            except Exception as error:
                print(f"[TempWork]run Exception {error}")
                self.ThreadNoti(str(error))

            finally:
                if self.read_thread is not None:
                    self.read_thread.stop()

                # send Off
                if self.serial_port is not None and self.serial_port.isOpen():
                    print("[TempWork]factory test end init...")
                    self.initStopCharging()

                    print("[TempWork]end Test")
                    self.consoleWriteBytes(self.makePacket(bytes([0x01, 0x00])))
                    self.serial_port.close()

                print("[TempWork]finally")
                self.bRunning = False
                self.ThreadNoti("finally")

    def encodeSignedByte(self, value) -> bytes:
        if value < -128 or value > 127:
            raise ValueError("Value out of range for signed byte:" + str(value))
        return value.to_bytes(1, byteorder='big', signed=True)
