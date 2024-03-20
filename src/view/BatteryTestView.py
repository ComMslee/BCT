from PySide6.QtCore import QObject

from src.MainUI import Ui_BCT
from src.util.SerialWork import SerialConsoleWorker


class BatteryTestView(QObject):
    def __init__(self, mainWindow: Ui_BCT):
        super().__init__()

        self.view = mainWindow

        self.dev01 = SerialConsoleWorker("COM3", 115200)
        self.dev02 = SerialConsoleWorker("COM4", 115200)

        self.devList = [self.dev01, self.dev02]
        for dev in self.devList:
            dev.msgThreadNoti.connect(logThread)
            dev.msgReadNoti.connect(logRead)
            dev.start()


def logThread(msg: str):
    print("logThread " + msg)


def logRead(msg: str):
    print("logRead " + msg)
