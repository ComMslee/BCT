from PySide6.QtWidgets import QMainWindow, QApplication

from src.MainUI import Ui_BCT


class MainWindow(QMainWindow, Ui_BCT):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()
