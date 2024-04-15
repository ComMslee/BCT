import time

import serial
from PySide6 import QtCore
from PySide6.QtCore import QThread, QMutex, QMutexLocker, QWaitCondition

from src.util.ReadThread import ReadThread


class SerialCycleWorker(QThread):
    bRunning = True
    msgThread = QtCore.Signal(str)
    msgReadSerial = QtCore.Signal(str)
    msgCnt = QtCore.Signal(int)
    msgReadList = QtCore.Signal(list)
    msgReadRealTime = QtCore.Signal(list)

    def __init__(self, ComPort, timeCycle, baudRate=115200, cycle=1000):
        super().__init__()

        self.serial_port = None
        self.read_thread: ReadThread = None
        self.comPort = ComPort
        self.baudRate = baudRate
        self.timeCycle = timeCycle
        self.cycle = int(cycle)
        self.oneCycleAvg = []
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
        self.msgThread.emit(f"[{self.comPort} / {self.baudRate}] {msg}")

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

    def readRealTime(self, batteryData: list):
        self.oneCycleAvg.append(batteryData)
        self.msgReadRealTime.emit(batteryData)

    def readSerial(self, serialNum: str):
        self.msgReadSerial.emit(serialNum)

    def run(self):
        with QMutexLocker(self.mutex):
            try:
                self.ThreadNoti("serial try open...")
                self.serial_port = serial.Serial(port=self.comPort, baudrate=self.baudRate, timeout=3)

                time.sleep(0.4)

                if self.serial_port.isOpen():
                    self.ThreadNoti("console.isOpen!!!")

                    # 00 start read
                    self.read_thread = ReadThread(self.serial_port)
                    self.read_thread.msgReadRealTime.connect(self.readRealTime)
                    self.read_thread.msgReadSerial.connect(self.readSerial)
                    self.read_thread.start()

                    # 01 testmode enable
                    onData = self.makePacket(bytes([0x01, 0x01]))
                    self.consoleWriteBytes(onData)

                    for idx in range(self.cycle):
                        if not self.bRunning: break
                        self.msgCnt.emit(idx)

                        self.oneCycleAvg = []

                        onData = self.makePacket(bytes([0x06, 0x01]))
                        self.consoleWriteBytes(onData)
                        waitTime = self.timeCycle[0][0] * 60 * 60 + (self.timeCycle[0][1] * 60) + (self.timeCycle[0][2])
                        print("on .. " + str(waitTime) + "s")
                        self.waitCondition.wait(self.mutex, waitTime * 1000)

                        print(f"{len(self.oneCycleAvg)} {self.oneCycleAvg}")

                        if len(self.oneCycleAvg) > 3:
                            avglist = self.oneCycleAvg[1:len(self.oneCycleAvg) - 1]
                        else:
                            avglist = self.oneCycleAvg
                        zipped_lists = zip(*avglist)
                        averages = [sum(values) / len(values) for values in zipped_lists]
                        print(averages)
                        self.msgReadList.emit(["", str(idx), averages[1], averages[0], averages[2], ""])

                        self.oneCycleAvg = []

                        if not self.bRunning: break
                        onData = self.makePacket(bytes([0x06, 0x00]))
                        self.consoleWriteBytes(onData)
                        waitTime = self.timeCycle[1][0] * 60 * 60 + (self.timeCycle[1][1] * 60) + (self.timeCycle[1][2])
                        print("off .. " + str(waitTime) + "s")
                        self.waitCondition.wait(self.mutex, waitTime * 1000)

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
