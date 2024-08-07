import PySide6
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget

from src.MainUI import Ui_BCT
from src.repository.DataConfig import DataConfig
from src.view.BatteryCycleView import BatteryCycleView
from src.view.BatteryFactoryTempView import BatteryFactoryTempView
from src.view.BatteryFactoryView import BatteryFactoryView
from src.view.PushSerialView import PushSerialView
from src.view.RootView import RootView
from src.view.unit.LEDBar import MakeBar


class MainWindow(QMainWindow, Ui_BCT):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)

        DataConfig()
        self.rootView = RootView(self)
        self.batteryCycleTab = BatteryCycleView(self)
        self.batteryFactoryTab = BatteryFactoryView(self)
        self.batteryFactoryTempView = BatteryFactoryTempView(self)
        self.pushSerialTab = PushSerialView(self)

        # self.makeBar = MakeBar(self)

        self.initSelectTab()

    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:
        super().closeEvent(event)
        self.saveSelectTab()
        print("closeEvent...")

    def initSelectTab(self):
        config = DataConfig().getSelectTab()

        if "main_tab" in config:
            self.tbMain.setCurrentIndex(config["main_tab"])

    def saveSelectTab(self):
        config = DataConfig()
        select = config.getSelectTab()
        select["main_tab"] = self.tbMain.currentIndex()
        config.saveData()


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.setWindowTitle("BCT_V1.0.3")

    window.show()
    app.exec_()
