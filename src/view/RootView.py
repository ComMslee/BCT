from PySide6.QtCore import QObject

from src.MainUI import Ui_BCT
from src.repository.DataConfig import DataConfig
from src.util.InfoWork import InfoWorker


class RootView(QObject):
    def __init__(self, mainWindow: Ui_BCT):
        super().__init__()

        self.view = mainWindow
        self.infoWork = None
        self.infoWork2 = None

        self.dataConfig = DataConfig()
        self.dataConfig.loadData()

        self.initUI()
        self.updateUI()

    def initUI(self):
        self.view.config_save.clicked.connect(self.onSaveDataEvent)
        self.view.config_check.clicked.connect(self.onCheckDev)
        self.dataConfig.msgSaveData.connect(self.onSaveData)

    def updateUI(self):
        self.view.dev_baud.setText(str(self.dataConfig.getComBaudRate()))
        self.view.dev_port.setText(self.dataConfig.getComPort(1))
        self.view.dev_port_2.setText(self.dataConfig.getComPort(2))

    def onCheckDev(self):
        dataConfig = self.dataConfig
        self.infoWork = InfoWorker(
            dataConfig.getComPort(1),
            dataConfig.getComBaudRate(),
        )
        self.infoWork.msgVersionRead.connect(self.msgVersionRead)
        self.infoWork.msgSerialRead.connect(self.msgSerialRead)
        self.infoWork.start()

        self.infoWork2 = InfoWorker(
            dataConfig.getComPort(2),
            dataConfig.getComBaudRate(),
        )
        self.infoWork2.msgVersionRead.connect(self.msgVersionRead2)
        self.infoWork2.msgSerialRead.connect(self.msgSerialRead2)
        self.infoWork2.start()

    def msgVersionRead(self, ver):
        self.view.dev_mcu_vsersion.setText(ver)
        pass

    def msgVersionRead2(self, ver):
        self.view.dev_mcu_vsersion.setText(ver)
        pass

    def msgSerialRead(self, num):
        #  self.view.dev_mcu_vsersion.setText(num)
        pass

    def msgSerialRead2(self, num):
        #  self.view.dev_mcu_vsersion.setText(num)
        pass

    def onSaveDataEvent(self):
        self.dataConfig.msgSaveData.emit()

    def onSaveData(self):
        self.dataConfig.setComBaudRate(self.view.dev_baud.text())
        self.dataConfig.setComPort(1, self.view.dev_port.text())
        self.dataConfig.setComPort(2, self.view.dev_port_2.text())
        self.dataConfig.saveData()

