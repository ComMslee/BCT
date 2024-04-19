import time

import serial
from PySide6 import QtCore
from PySide6.QtCore import QThread, QMutex, QMutexLocker, QWaitCondition

from src.util.ReadThread import ReadThread
from src.util.define import global_testCase


class FactoryWork(QThread):
    bRunning = True
    msgThread = QtCore.Signal(str)
    msgRead = QtCore.Signal(str)
    msgReadList = QtCore.Signal(list)

    def __init__(self, ComPort, baudrate=115200):
        super().__init__()

        self.serial_port = None
        self.read_thread: ReadThread = None
        self.comPort = ComPort
        self.BaudRate = baudrate
        self.charging = False

        self.testType: bool = False
        self.testTitle: str = ""

        self.mutex = QMutex()
        self.waitCondition = QWaitCondition()

    def consoleWriteBytes(self, sendData: bytes):
        print(f">>>> {' '.join(format(byte, '02X') for byte in sendData)}")
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

    def readRealTime(self, batteryData: dict):
        if batteryData["progrssbar"] == 5:
            if not self.charging:
                self.testOnOff(True)
            self.charging = True
        elif batteryData["progrssbar"] == 3:
            if self.charging:
                self.testOnOff(False)
            self.charging = False

    def setTest(self, testTitle: str, testType: bool):
        print(testTitle)
        self.testTitle = str(testTitle)
        self.testType = testType
        self.msgReadList.emit([self.testTitle, ""])

    def testOnOff(self, chargingOn):
        print(f"-----------------------{self.testTitle} {chargingOn}, {self.testType}")
        if chargingOn == self.testType:
            self.msgReadList.emit([self.testTitle, "Pass"])

    def ack(self, ack: bytes):
        if len(ack) == 2:
            print(f"[cmd:{ack[1]}][result:{ack[0] == 0}]")

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
                    self.read_thread.msgReadRealTime.connect(self.readRealTime)
                    self.read_thread.msgAck.connect(self.ack)
                    self.read_thread.start()

                    # 01 testmode enable
                    print("start Test")
                    self.consoleWriteBytes(self.makePacket(bytes([0x01, 0x01])))
                    self.waitCondition.wait(self.mutex, 100)
                    if not self.bRunning: return

                    # 초기화
                    self.consoleWriteBytes(self.makePacket(bytes([0x04, 0x00])))
                    self.consoleWriteBytes(self.makePacket(bytes([0x06, 0x00])))
                    self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x01, self.encodeSignedByte(30)[0], 0x00])))
                    self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x02, self.encodeSignedByte(30)[0], 0x00])))
                    self.waitCondition.wait(self.mutex, 100)
                    if not self.bRunning: return

                    # 충전시작
                    print("start charging")
                    self.consoleWriteBytes(self.makePacket(bytes([0x06, 0x01])))
                    self.waitCondition.wait(self.mutex, 17 * 1000)
                    if not self.bRunning: return

                    # -5
                    self.setTest("-5", False)
                    self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x01, self.encodeSignedByte(-5)[0], 0x00])))
                    self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x02, self.encodeSignedByte(30)[0], 0x00])))
                    self.waitCondition.wait(self.mutex, 3 * 1000)
                    if not self.bRunning: return

                    # +5
                    self.setTest("5", True)
                    self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x01, self.encodeSignedByte(5)[0], 0x00])))
                    self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x02, self.encodeSignedByte(30)[0], 0x00])))
                    self.waitCondition.wait(self.mutex, 3 * 1000)
                    if not self.bRunning: return

                    # +60
                    self.setTest("60", False)
                    self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x01, self.encodeSignedByte(30)[0], 0x00])))
                    self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x02, self.encodeSignedByte(60)[0], 0x00])))
                    self.waitCondition.wait(self.mutex, 3 * 1000)
                    if not self.bRunning: return

                    # +45
                    self.setTest("45", True)
                    self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x01, self.encodeSignedByte(30)[0], 0x00])))
                    self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x02, self.encodeSignedByte(45)[0], 0x00])))
                    self.waitCondition.wait(self.mutex, 3 * 1000)
                    if not self.bRunning: return

                    if not self.bRunning: return
                    for code, status in global_testCase.items():
                        # 충전시작
                        self.consoleWriteBytes(self.makePacket(bytes([0x06, 0x01])))
                        self.waitCondition.wait(self.mutex, 17 * 1000)
                        if not self.bRunning: return

                        # 애러코드
                        self.setTest(f"ERR::{status}", False)
                        self.consoleWriteBytes(self.makePacket(bytes([0x04, code])))
                        self.waitCondition.wait(self.mutex, 3 * 1000)
                        self.consoleWriteBytes(self.makePacket(bytes([0x04, 0x00])))
                        self.consoleWriteBytes(self.makePacket(bytes([0x06, 0x00])))
                        if not self.bRunning: return

                    # 충전종료
                    print("stop charging")
                    self.consoleWriteBytes(self.makePacket(bytes([0x06, 0x00])))
                    self.waitCondition.wait(self.mutex, 10)
                    # work
                    # self.consoleWriteBytes(self.makePacket(bytes([0x01, 0x01])))
                    # self.waitCondition.wait(self.mutex, 10)

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
                if self.serial_port is not None and self.serial_port.isOpen():
                    print("end Test")
                    self.consoleWriteBytes(self.makePacket(bytes([0x01, 0x00])))
                    self.serial_port.close()
                print("SerialCycleWorker finally")
                self.bRunning = False
                self.ThreadNoti("finally")

    def encodeSignedByte(self, value) -> bytes:
        if value < -128 or value > 127:
            raise ValueError("Value out of range for signed byte:" + str(value))
        return value.to_bytes(1, byteorder='big', signed=True)
