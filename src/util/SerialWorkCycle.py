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
        self.msgReadRealTime.emit(batteryData)

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
