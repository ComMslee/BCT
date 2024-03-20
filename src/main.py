import time

from PySide6.QtWidgets import QMainWindow, QApplication

from src.MainUI import Ui_BCT
from src.SerialWork import SerialConsoleWorker


class MainWindow(QMainWindow, Ui_BCT):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)

        self.con = SerialConsoleWorker("COM3", 115200)
        self.con.msgThreadNoti.connect(self.Thread)
        self.con.msgReadNoti.connect(self.read)
        self.con.start()

    def Thread(self, msg: str):
        print("Thread : [" + msg + "]")

    def read(self, msg: str):
        print("read : [" + msg + "]")


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()
