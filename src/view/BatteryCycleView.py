from PySide6.QtCore import QObject

from src.MainUI import Ui_BCT
from src.repository.DataConfig import DataConfig
from src.util.SerialWorkCycle import SerialCycleWorker


class BatteryCycleView(QObject):
    def __init__(self, mainWindow: Ui_BCT):
        super().__init__()

        self.dev01: SerialCycleWorker = None
        self.dev02: SerialCycleWorker = None
        self.view = mainWindow

        self.dataConfig = DataConfig()
        self.dataConfig.loadData()

        self.initUI()
        self.updateUI()

    def initUI(self):
        self.view.config_btn_start.clicked.connect(self.startCycle)
        self.view.config_btn_stop.clicked.connect(self.stopCycle)
        self.dataConfig.msgSaveData.connect(self.saveData)

    def updateUI(self):
        self.view.config_cycle.setText(str(self.dataConfig.getCycle()))
        ontime, offtime = self.dataConfig.getTime()
        self.view.config_time_on_h.setText(str(ontime[0]))
        self.view.config_time_on_m.setText(str(ontime[1]))
        self.view.config_time_on_s.setText(str(ontime[2]))
        self.view.config_time_off_h.setText(str(offtime[0]))
        self.view.config_time_off_m.setText(str(offtime[1]))
        self.view.config_time_off_s.setText(str(offtime[2]))

    def saveData(self):
        dataconfig = self.dataConfig
        dataconfig.setTime(
            [
                int(self.view.config_time_on_h.text()),
                int(self.view.config_time_on_m.text()),
                int(self.view.config_time_on_s.text()),
            ],
            [
                int(self.view.config_time_off_h.text()),
                int(self.view.config_time_off_m.text()),
                int(self.view.config_time_off_s.text()),
            ])
        dataconfig.setCycle(self.view.config_cycle.text())
        dataconfig.saveData()

    def startCycle(self):
        print("start cycle")
        dataconfig = self.dataConfig
        self.dev01 = SerialCycleWorker(
            dataconfig.getComPort(1),
            dataconfig.getTime(),
            dataconfig.getComBaudRate(),
            dataconfig.getCycle()
        )
        self.dev01.start()

        self.dev02 = SerialCycleWorker(
            dataconfig.getComPort(2),
            dataconfig.getTime(),
            dataconfig.getComBaudRate(),
            dataconfig.getCycle()
        )
        self.dev02.start()

        pass

    def stopCycle(self):
        if self.dev01 is not None:
            self.dev01.stopWork()
        if self.dev02 is not None:
            self.dev02.stopWork()
        print("start cycle stop")
        pass

######################################################
#         self.dev01 = SerialWorker("COM3", 115200)
#         self.dev02 = SerialWorker("COM4", 115200)
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
