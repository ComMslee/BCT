import time

import serial
from PySide6 import QtCore
from PySide6.QtCore import QThread, QMutex, QMutexLocker, QWaitCondition

from src.util.ReadThread import ReadThread
from src.util.define import global_testCase


class SerialCycleWorker(QThread):
    bRunning = True
    msgThread = QtCore.Signal(str)
    msgReadSerial = QtCore.Signal(str)
    msgCnt = QtCore.Signal(int)
    msgReadList = QtCore.Signal(list)
    msgReadRealTime = QtCore.Signal(dict)

    def __init__(self, ComPort, baudRate, timeCycle, cycle=1000):
        super().__init__()

        self.serial_port = None
        self.read_thread: ReadThread = None
        self.comPort = ComPort
        self.baudRate = baudRate
        self.timeCycle = timeCycle
        self.cycle = int(cycle)
        self.cnt = [0, 0]
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

    def readRealTime(self, batteryData: dict):
        if len(batteryData) > 4:
            code = batteryData["diagInfo"]
            if code in global_testCase:
                code = global_testCase[code]
            self.msgReadList.emit(
                [batteryData["chargeMode"], f"{self.cnt[0]}::{self.cnt[1]}",
                 batteryData["current"], batteryData["voltage"], batteryData["tempAvg"], code])
            self.cnt[1] += 1

        soc = batteryData["soc"]
        voltage = batteryData["voltage"]
        current = batteryData["current"]

        # soc 값을 90 이하일 때만 10단위로 내림하고 0인 경우 1로 설정
        if soc <= 90:
            soc = max((soc // 10) * 10, 1)

        vmin, vmax = self.bctMap[soc][0] * 0.95, self.bctMap[soc][0] * 1.05
        amin, amax = self.bctMap[soc][1] * 0.95, self.bctMap[soc][1] * 1.05

        # 전류와 전압 조건 검사
        if batteryData["progrssbar"] == 5:
            currentPass = amin < current < amax
            voltagePass = vmin < voltage < vmax
            print(f"currnet {currentPass}, voltage {voltagePass}")

        self.msgReadRealTime.emit(batteryData)

    bctMap = {
        1: [46.25, 2.62],
        10: [49.32, 8.2],
        20: [50.55, 8.22],
        30: [51.45, 8.22],
        40: [52.32, 8.2],
        50: [53.42, 8.22],
        60: [54.78, 8.22],
        70: [55.88, 8.22],
        80: [57.23, 8.2],
        90: [58.18, 7.44],
        91: [58.22, 7.1],
        92: [58.26, 6.86],
        93: [58.26, 6.66],
        94: [58.26, 6.3],
        95: [58.3, 6.1],
        96: [58.26, 5.84],
        97: [58.3, 5.46],
        98: [58.34, 5.12],
        99: [49.32, 4.64],
        100: [49.32, 1],
        # 101: [49.32, 0.28],
    }

    def readSerial(self, serialNum: str):
        self.msgReadSerial.emit(serialNum)

    def ack(self, ack: bytes):
        if len(ack) == 2:
            print(f"[cmd:{ack[1]}][result:{ack[0] == 0}]")

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
                    self.read_thread.msgAck.connect(self.ack)
                    self.read_thread.start()

                    # 01 testmode enable
                    self.consoleWriteBytes(self.makePacket(bytes([0x01, 0x01])))

                    for idx in range(self.cycle):
                        if not self.bRunning: break
                        self.cnt = [idx, 0]
                        self.msgCnt.emit(idx)

                        # 001 충전on
                        self.consoleWriteBytes(self.makePacket(bytes([0x06, 0x01])))
                        waitTime = self.timeCycle[0][0] * 60 * 60 + (self.timeCycle[0][1] * 60) + (self.timeCycle[0][2])
                        print(f"on... {waitTime}s")
                        self.waitCondition.wait(self.mutex, waitTime * 1000)
                        if not self.bRunning: break

                        # 002 충전off
                        self.consoleWriteBytes(self.makePacket(bytes([0x06, 0x00])))
                        waitTime = self.timeCycle[1][0] * 60 * 60 + (self.timeCycle[1][1] * 60) + (self.timeCycle[1][2])
                        print(f"off... {waitTime}s")
                        self.waitCondition.wait(self.mutex, waitTime * 1000)
                        if not self.bRunning: break

                    self.ThreadNoti("write complete")
                else:
                    self.ThreadNoti("not open...")

            except Exception as error:
                print(f"Exception error :: {error}")
                self.ThreadNoti(str(error))

            finally:
                if self.read_thread is not None:
                    self.read_thread.stop()

                # send Off
                if self.serial_port is not None and self.serial_port.isOpen():
                    self.consoleWriteBytes(self.makePacket(bytes([0x01, 0x00])))
                    self.serial_port.close()
                print("SerialCycleWorker finally")
                self.bRunning = False
                self.ThreadNoti("finally...")
