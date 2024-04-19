import PySide6
from PySide6.QtWidgets import QMainWindow, QApplication

from src.MainUI import Ui_BCT
from src.repository.DataConfig import DataConfig
from src.view.BatteryCycleView import BatteryCycleView
from src.view.BatteryFactoryView import BatteryFactoryView
from src.view.PushSerialView import PushSerialView
from src.view.RootView import RootView


class MainWindow(QMainWindow, Ui_BCT):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)

        DataConfig()
        self.rootView = RootView(self)
        self.batteryCycleTab = BatteryCycleView(self)
        self.batteryFactoryTab = BatteryFactoryView(self)
        self.pushSerialTab = PushSerialView(self)

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
    window.setWindowTitle("BCT_V1.0.0")
    window.show()
    app.exec_()
