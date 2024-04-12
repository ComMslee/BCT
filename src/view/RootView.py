from PySide6.QtCore import QObject

from src.MainUI import Ui_BCT
from src.repository.DataConfig import DataConfig


class RootView(QObject):
    def __init__(self, mainWindow: Ui_BCT):
        super().__init__()

        self.view = mainWindow

        self.dataConfig = DataConfig()
        self.dataConfig.loadData()

        self.initUI()
        self.updateUI()

    def initUI(self):
        self.view.config_save.clicked.connect(self.saveDataEvent)
        self.dataConfig.msgSaveData.connect(self.saveData)

    def updateUI(self):
        self.view.dev_baud.setText(str(self.dataConfig.getComBaudRate()))
        self.view.dev_port.setText(self.dataConfig.getComPort(1))
        self.view.dev_port_2.setText(self.dataConfig.getComPort(2))

    def saveDataEvent(self):
        self.dataConfig.msgSaveData.emit()

    def saveData(self):
        self.dataConfig.setComBaudRate(self.view.dev_baud.text())
        self.dataConfig.setComPort(1, self.view.dev_port.text())
        self.dataConfig.setComPort(2, self.view.dev_port_2.text())
        self.dataConfig.saveData()

