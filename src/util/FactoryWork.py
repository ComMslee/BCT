import time

import serial
from PySide6 import QtCore
from PySide6.QtCore import QThread, QMutex, QMutexLocker, QWaitCondition

from src.util.ReadThread import ReadThread


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

                    # 초기화
                    self.consoleWriteBytes(self.makePacket(bytes([0x06, 0x00])))
                    self.consoleWriteBytes(self.makePacket(bytes([0x04, 0x00])))
                    self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x01, self.encodeSignedByte(30)[0], 0x00])))
                    self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x02, self.encodeSignedByte(30)[0], 0x00])))
                    self.waitCondition.wait(self.mutex, 100)

                    # 충전시작
                    print("start charging")
                    self.consoleWriteBytes(self.makePacket(bytes([0x06, 0x01])))
                    self.waitCondition.wait(self.mutex, 17 * 1000)

                    # -5
                    self.setTest("-5", False)
                    self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x01, self.encodeSignedByte(-5)[0], 0x00])))
                    self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x02, self.encodeSignedByte(30)[0], 0x00])))
                    self.waitCondition.wait(self.mutex, 3 * 1000)

                    # +5
                    self.setTest("5", True)
                    self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x01, self.encodeSignedByte(5)[0], 0x00])))
                    self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x02, self.encodeSignedByte(30)[0], 0x00])))
                    self.waitCondition.wait(self.mutex, 3 * 1000)

                    # +60
                    self.setTest("60", False)
                    self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x01, self.encodeSignedByte(30)[0], 0x00])))
                    self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x02, self.encodeSignedByte(60)[0], 0x00])))
                    self.waitCondition.wait(self.mutex, 3 * 1000)

                    # +45
                    self.setTest("45", True)
                    self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x01, self.encodeSignedByte(30)[0], 0x00])))
                    self.consoleWriteBytes(self.makePacket(bytes([0x05, 0x02, self.encodeSignedByte(45)[0], 0x00])))
                    self.waitCondition.wait(self.mutex, 3 * 1000)

                    testCase = [
                        ("Cell_OVP_FAULT", 3),
                        ("Cell_OVP_FAILURE", 4),
                        ("Cell_UVP_FAULT", 7),
                        ("Cell_UVP_FAILURE", 8),
                        ("Cell_OVP_PACK_FAULT", 11),
                        ("Cell_UVP_PACK_FAILURE", 16),
                        ("Cell_OCCP_FAULT", 19),
                        ("Cell_OCCP_FAILURE", 20),
                        ("Cell_ODCP_FAULT", 23),
                        ("Cell_ODCP_FAILURE", 24),
                        ("Cell_OCTP_FAULT", 27),
                        ("Cell_OCTP_FAILURE", 28),
                        ("Cell_UCTP_FAULT", 35),
                        ("Cell_UDTP_FAULT", 39),
                        ("Cell_SOC_IM_FAULT", 55),
                        ("BMS_SHORT_IC", 60),
                        ("BMS_DFET_FAULT", 63),
                        ("BMS_CFET_FAULT", 67),
                        ("BMS_PFET_OT_FAULT", 71),
                        ("BMS_ASIC_SHUTDOWN_FAULT", 79),
                        ("BMS_ASIC_LOC_FAULT", 83),
                        ("Pack_FUSEROHM_FAULT", 87),
                        ("Pack_FUSEOC_FAULT", 95),
                        ("Pack_FETsOT_FAULT", 99),
                        ("ASIC_OV_FAILURE", 104),
                        ("ASIC_UV_FAULT", 107),
                        ("ASIC_UV_FAILURE", 108),
                        ("ASIC_ODC_FAULT", 111),
                        ("ASIC_SCD_FAULT", 119),
                        ("ASIC_SCD_FAILURE", 120),
                        ("ASIC_XREADY_FAULT", 127),
                        ("ASIC_OVERRIDE_FAULT", 131)
                    ]

                    for case in testCase:
                        status, code = case
                        # 충전시작
                        self.consoleWriteBytes(self.makePacket(bytes([0x04, 0x00])))
                        self.consoleWriteBytes(self.makePacket(bytes([0x06, 0x00])))
                        self.consoleWriteBytes(self.makePacket(bytes([0x06, 0x01])))
                        self.waitCondition.wait(self.mutex, 17 * 1000)
                        
                        # 애러코드
                        self.setTest(f"ERR::{status}", False)
                        self.consoleWriteBytes(self.makePacket(bytes([0x04, code])))
                        self.waitCondition.wait(self.mutex, 3 * 1000)

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
                self.ThreadNoti("finally...")

    def encodeSignedByte(self, value) -> bytes:
        if value < -128 or value > 127:
            raise ValueError("Value out of range for signed byte:" + str(value))
        return value.to_bytes(1, byteorder='big', signed=True)
