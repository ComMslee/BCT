from PySide6.QtWidgets import QMainWindow, QApplication

from src.MainUI import Ui_BCT
from src.view.BatteryTestView import BatteryTestView
from src.view.PushSerialView import PushSerialView


class MainWindow(QMainWindow, Ui_BCT):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.BatteryTestTab = BatteryTestView(self)
        self.PushSerialTab = PushSerialView(self)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()
