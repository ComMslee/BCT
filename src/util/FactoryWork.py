import time

import serial
from PySide6 import QtCore
from PySide6.QtCore import QThread, QMutex, QMutexLocker, QWaitCondition

from src.util.ReadThread import ReadThread
from src.util.define import bctMap


class FactoryWork(QThread):
    bRunning = True
    msgThread = QtCore.Signal(str)
    msgRead = QtCore.Signal(str)
    msgReadList = QtCore.Signal(list)

    def __init__(self, ComPort, baudrate=115200, bElectricity: bool = True, bTempTest: bool = False, bErrTestDict=None):
        super().__init__()

        self.serial_port = None
        self.read_thread: ReadThread = None
        self.comPort = ComPort
        self.BaudRate = baudrate
        self.bElectricity = bElectricity
        self.bTempTest = bTempTest
        self.bErrTestDict = bErrTestDict if bErrTestDict else {}
        self.chargingStartWaitTime = 17 * 1000
        self.testWaitTime = 4 * 1000
        self.charging = False

        self.testType: bool = False
        self.testTitle: str = ""

        self.mutex = QMutex()
        self.waitCondition = QWaitCondition()

    def consoleWriteBytes(self, sendData: bytes):
        print(f"[FactoryWork]>>>> {' '.join(format(byte, '02X') for byte in sendData)}")
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

    def electricityTest(self, batteryData: dict):
        # 전류와 전압 조건 검사
        if batteryData["progrssbar"] == 5:
            soc = batteryData["soc"]
            voltage = batteryData["voltage"]
            current = batteryData["current"]

            # soc 값을 90 이하일 때만 10단위로 내림하고 0인 경우 1로 설정
            if soc <= 90:
                soc = max((soc // 10) * 10, 1)

            vmin, vmax = bctMap[soc][0] * 0.95, bctMap[soc][0] * 1.05
            amin, amax = bctMap[soc][1] * 0.95, bctMap[soc][1] * 1.05

            currentPass = amin < current < amax
            voltagePass = vmin < voltage < vmax
            print(f"currnet {currentPass}, voltage {voltagePass}")
            self.msgReadList.emit([self.testTitle, f"{currentPass}/{voltagePass}"])
        else:
            self.msgReadList.emit([self.testTitle, f""])

    def stateTest(self, batteryData: dict):
        if batteryData["progrssbar"] == 5:
            if not self.charging:
                self.testOnOff(True)
            self.charging = True
        elif batteryData["progrssbar"] == 3:
            if self.charging:
                self.testOnOff(False)
            self.charging = False

    def setTest(self, testTitle: str, testType: bool):
        print(f"[FactoryWork]{testTitle}")
        self.testTitle = str(testTitle)
        self.testType = testType
        if len(self.testTitle) > 0:
            self.msgReadList.emit([self.testTitle, ""])

    def testOnOff(self, chargingOn):
        print(f"[FactoryWork]testOnOff {self.testTitle} {chargingOn}, {self.testType}")
        if chargingOn == self.testType and len(self.testTitle) > 0:
            self.msgReadList.emit([self.testTitle, "Pass"])

    def ack(self, ack: bytes):
        if len(ack) == 2:
            print(f"[FactoryWork][cmd:{ack[1]}][result:{ack[0] == 0}]")

    def initStopCharging(self):
        try:
            self.consoleWriteBytes(self.makePacket(bytes([0x04, 0x00])))
            self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x01, self.encodeSignedByte(30)[0], 0x00])))
            self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x02, self.encodeSignedByte(30)[0], 0x00])))
            self.consoleWriteBytes(self.makePacket(bytes([0x06, 0x00])))
            self.waitCondition.wait(self.mutex, 50)
        except Exception as error:
            print(f"[FactoryWork]initStopCharging Exception {error}")
            self.ThreadNoti(str(error))

    def tempTest(self, testTitle, testType, minVal=30, maxVal=30):
        try:
            self.setTest(testTitle, testType)
            self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x01, self.encodeSignedByte(minVal)[0], 0x00])))
            self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x02, self.encodeSignedByte(maxVal)[0], 0x00])))
            self.waitCondition.wait(self.mutex, self.testWaitTime)
        except Exception as error:
            print(f"[FactoryWork]tempTest Exception {error}")
            self.ThreadNoti(str(error))

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
                    print("[FactoryWork]start Test")
                    self.consoleWriteBytes(self.makePacket(bytes([0x01, 0x01])))
                    self.waitCondition.wait(self.mutex, 50)
                    if not self.bRunning: return

                    # 초기화
                    self.initStopCharging()
                    if not self.bRunning: return

                    if self.bElectricity:
                        self.read_thread.msgReadRealTime.connect(self.electricityTest)
                        self.testTitle = str(f"ElectricityTest")
                        self.consoleWriteBytes(self.makePacket(bytes([0x06, 0x01])))
                        self.waitCondition.wait(self.mutex, self.chargingStartWaitTime * 1.2)
                        if not self.bRunning: return

                    self.read_thread.msgReadRealTime.connect(self.stateTest)

                    # 충전시작
                    if self.bTempTest:
                        print("[FactoryWork]tempTest::start charging")
                        self.consoleWriteBytes(self.makePacket(bytes([0x06, 0x01])))
                        self.waitCondition.wait(self.mutex, self.chargingStartWaitTime)
                        if not self.bRunning: return

                        self.tempTest("-5", False, minVal=-5)
                        if not self.bRunning: return

                        self.tempTest("5", True, minVal=-5)
                        if not self.bRunning: return

                        self.tempTest("60", False, maxVal=60)
                        if not self.bRunning: return

                        self.tempTest("45", True, maxVal=45)
                        if not self.bRunning: return
                    else:
                        print("[FactoryWork]tempTest:: is False Skip temp Test")

                    itemCnt = 0  # 카운터 변수 초기화
                    itemLen = len(self.bErrTestDict)
                    for code, status in self.bErrTestDict.items():
                        itemCnt += 1
                        # 충전시작
                        print(f"[FactoryWork]ErrTest::start charging [ {itemCnt}/{itemLen} ]")
                        self.consoleWriteBytes(self.makePacket(bytes([0x06, 0x01])))
                        self.waitCondition.wait(self.mutex, self.chargingStartWaitTime)
                        if not self.bRunning: return

                        # 애러코드
                        self.setTest(f"ERR::{status}", False)
                        self.consoleWriteBytes(self.makePacket(bytes([0x04, int(code)])))
                        self.waitCondition.wait(self.mutex, self.testWaitTime)

                        # 충전 중지 및 초기화
                        print("[FactoryWork]ErrTest::stop charging")
                        self.consoleWriteBytes(self.makePacket(bytes([0x04, 0x00])))
                        self.consoleWriteBytes(self.makePacket(bytes([0x06, 0x00])))
                        if not self.bRunning: return

                    # 충전종료
                    print("[FactoryWork]stop charging")
                    self.ThreadNoti("write complete")
                else:
                    self.ThreadNoti("not open...")

            except Exception as error:
                print(f"[FactoryWork]run Exception {error}")
                self.ThreadNoti(str(error))

            finally:
                if self.read_thread is not None:
                    self.read_thread.stop()

                # send Off
                if self.serial_port is not None and self.serial_port.isOpen():
                    print("[FactoryWork]factory test end init...")
                    self.initStopCharging()

                    print("[FactoryWork]end Test")
                    self.consoleWriteBytes(self.makePacket(bytes([0x01, 0x00])))
                    self.serial_port.close()

                print("[FactoryWork]finally")
                self.bRunning = False
                self.ThreadNoti("finally")

    def encodeSignedByte(self, value) -> bytes:
        if value < -128 or value > 127:
            raise ValueError("Value out of range for signed byte:" + str(value))
        return value.to_bytes(1, byteorder='big', signed=True)
