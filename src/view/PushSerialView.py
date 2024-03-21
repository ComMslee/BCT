from PySide6.QtCore import QObject

from src.MainUI import Ui_BCT


class PushSerialView(QObject):
    def __init__(self, mainWindow: Ui_BCT):
        super().__init__()

        self.view = mainWindow


