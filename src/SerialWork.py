import os
import time

import serial
from PySide6 import QtCore
from PySide6.QtCore import QThread, QMutex, QMutexLocker


class SerialConsoleWorker(QThread):
    bRunning = True
    msgThreadNoti = QtCore.Signal(str)
    msgReadNoti = QtCore.Signal(str)

    def __init__(self, ComPort, BaudRate=115200):
        super().__init__()

        self.serial_port = None
        self.comPort = ComPort
        self.BaudRate = BaudRate
        self.mutex = QMutex()

    def consoleWrite(self, data: str):
        data = data.replace("\n", "")
        sendData = bytes(data + "\r\n", "UTF-8")

        if self.serial_port is not None:
            self.serial_port.write(sendData)
            time.sleep(0.2)

        else:
            self.msgThreadNoti.emit("console is none... ")

    def run(self):
        with QMutexLocker(self.mutex):
            try:
                self.msgThreadNoti.emit("serial try open...")
                self.serial_port = serial.Serial(port=self.comPort, baudrate=self.BaudRate, timeout=3)

                time.sleep(0.4)

                if self.serial_port.isOpen():
                    self.msgThreadNoti.emit("console.isOpen!!!")

                    while self.bRunning:
                        if self.serial_port.in_waiting > 0:
                            input_data = self.serial_port.readline().decode().strip()
                            if input_data:
                                self.msgReadNoti.emit(input_data)
                            else:
                                self.msgThreadNoti.emit("input_data is Empty")
                        time.sleep(0.1)

                    self.msgThreadNoti.emit("write complete!!")
                else:
                    self.msgThreadNoti.emit("not open...")

            except Exception as error:
                print(error)
                self.msgThreadNoti.emit(str(error))
