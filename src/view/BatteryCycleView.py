from PySide6.QtCore import QObject

from src.MainUI import Ui_BCT
from src.util.SerialWork import SerialConsoleWorker


class BatteryCycleView(QObject):
    def __init__(self, mainWindow: Ui_BCT):
        super().__init__()

        self.view = mainWindow

        self.initUI()

    def initUI(self):
        self.view.config_btn_start.clicked.connect(self.startCycle)
        self.view.config_btn_stop.clicked.connect(self.stopCycle)

    def startCycle(self):
        pass

    def stopCycle(self):
        pass


######################################################
#         self.dev01 = SerialConsoleWorker("COM3", 115200)
#         self.dev02 = SerialConsoleWorker("COM4", 115200)
#
#         self.devList = [self.dev01, self.dev02]
#         for dev in self.devList:
#             dev.msgThread.connect(logThread)
#             dev.msgRead.connect(logRead)
#             dev.start()
#
#
# def logThread(msg: str):
#     print("logThread " + msg)
#
#
# def logRead(msg: str):
#     print("logRead " + msg)
