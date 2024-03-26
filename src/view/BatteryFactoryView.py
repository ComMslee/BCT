from PySide6.QtCore import QObject

from src.MainUI import Ui_BCT
from src.repository.DataConfig import DataConfig


class BatteryFactoryView(QObject):
    def __init__(self, mainWindow: Ui_BCT):
        super().__init__()

        self.view = mainWindow

        self.dataConfig = DataConfig()
        self.dataConfig.loadData()

        self.initUI()
        self.updateUI()

    def initUI(self):
        pass

    def updateUI(self):
        pass
