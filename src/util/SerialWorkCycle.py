import time

import serial
from PySide6 import QtCore
from PySide6.QtCore import QThread, QMutex, QMutexLocker


class SerialCycleWorker(QThread):
    bRunning = True
    msgThread = QtCore.Signal(str)
    msgRead = QtCore.Signal(str)
    msgReadList = QtCore.Signal(list)

    def __init__(self, ComPort, time, baudrate=115200, cycle=1000):
        super().__init__()

        self.serial_port = None
        self.comPort = ComPort
        self.BaudRate = baudrate
        self.time = time
        self.cycle = int(cycle)
        self.mutex = QMutex()

    def consoleWrite(self, data: str):
        data = data.replace("\n", "")
        sendData = bytes(data + "\r\n", "UTF-8")

        if self.serial_port is not None:
            self.serial_port.write(sendData)
            time.sleep(0.2)

        else:
            self.ThreadNoti("console is none... ")

    def stopWork(self):
        self.cycle = -1

    def ThreadNoti(self, msg: str):
        self.msgThread.emit(f"[{self.comPort} / {self.BaudRate}] {msg}")

    def run(self):
        with QMutexLocker(self.mutex):
            try:
                self.ThreadNoti("serial try open...")
                self.serial_port = serial.Serial(port=self.comPort, baudrate=self.BaudRate, timeout=3)

                time.sleep(0.4)

                if self.serial_port.isOpen():
                    self.ThreadNoti("console.isOpen!!!")

                    for idx in range(self.cycle):
                        if self.serial_port.in_waiting > 0:
                            input_data = self.serial_port.readline().decode().strip()
                            if input_data:
                                self.msgRead.emit(input_data)
                            else:
                                self.ThreadNoti("input_data is Empty")
                        time.sleep(0.5)
                        self.msgReadList.emit(["", str(idx), "", "", "", ""])
                        print("cycle .. " + str(idx))

                    self.ThreadNoti("write complete")
                else:
                    self.ThreadNoti("not open...")

            except Exception as error:
                print(error)
                self.ThreadNoti(str(error))
