from PySide6.QtCore import QObject

from src.MainUI import Ui_BCT
from src.repository.DataConfig import DataConfig
from src.util.FactoryWork import FactoryWork


class BatteryFactoryView(QObject):
    def __init__(self, mainWindow: Ui_BCT):
        super().__init__()

        self.view = mainWindow

        self.serialWork = None
        self.serialWork2 = None
        self.dataConfig = DataConfig()
        self.dataConfig.loadData()

        self.initUI()
        self.updateUI()

    def initUI(self):
        self.view.factory_start.clicked.connect(self.onStart)
        pass

    def updateUI(self):
        pass

    def onStart(self):
        dataConfig = self.dataConfig
        self.serialWork = FactoryWork(
            dataConfig.getComPort(1),
            dataConfig.getComBaudRate(),
        )
        self.serialWork.start()

        self.serialWork2 = FactoryWork(
            dataConfig.getComPort(2),
            dataConfig.getComBaudRate(),
        )
        self.serialWork2.start()
        pass
