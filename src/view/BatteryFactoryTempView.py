from typing import List

from PySide6.QtCore import QObject

from src.MainUI import Ui_BCT
from src.repository.DataConfig import DataConfig
from src.util.TempWork import TempWork


class BatteryFactoryTempView(QObject):
    def __init__(self, mainWindow: Ui_BCT):
        super().__init__()

        self.view = mainWindow

        self.dataConfig = DataConfig()
        self.dataConfig.loadData()

        self.devThread: List[TempWork] = []
        self.devView = []

        self.initUI()
        self.updateUI()

    def initUI(self):
        self.view.factory_temp_start.clicked.connect(self.startCycle)
        self.view.factory_temp_stop.clicked.connect(self.stopCycle)
        self.view.factory_temp_push.clicked.connect(self.push)
        self.enableBtn(True)

    def updateUI(self):
        pass

    def startCycle(self):
        print("start cycle")
        dataConfig = self.dataConfig
        dataConfig.msgSaveData.emit()

        self.devThread = []
        devPort = [dataConfig.getComPort(1), dataConfig.getComPort(2)]
        self.devView = [DeviceView(), DeviceView()]
        for port, view in zip(devPort, self.devView):
            thread = TempWork(port, baudrate=dataConfig.getComBaudRate())
            thread.msgThread.connect(self.threadNoti)
            thread.start()
            self.devThread.append(thread)

        self.enableBtn(False)

    def stopCycle(self):
        for dev in self.devThread:
            dev.stopWork()
        print("start cycle stop")
        self.enableBtn(True)

    def push(self):
        for dev in self.devThread:
            if dev.bRunning:
                dev.pushTemp(int(self.view.factory_temp_value.text()))

    def threadNoti(self, msg):
        if "finally" in msg:
            cnt = 0
            for dev in self.devThread:
                if not dev.bRunning:
                    cnt += 1
            if len(self.devThread) == cnt:
                print("BatteryFactoryTempView::finally")
                self.enableBtn(True)

    def enableBtn(self, enable):
        self.view.factory_temp_start.setEnabled(enable)
        self.view.factory_temp_stop.setEnabled(not enable)
        self.view.tbMain.setTabEnabled(0, enable)
        self.view.tbMain.setTabEnabled(1, enable)
        self.view.tbMain.setTabEnabled(3, enable)


class DeviceView(QObject):
    def __init__(self):
        super().__init__()
