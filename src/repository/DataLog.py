import json
import os
import re

from PySide6.QtCore import QObject


class DataLog(QObject):
    __init = False
    __DEBUG__ = False

    __SAVE_DIR = "data"
    __FILE_CONFIG = "./" + __SAVE_DIR + "/"

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(DataLog, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if self.__init:
            return
        self.__init = True

        if os.path.isdir(self.__SAVE_DIR) is False:
            os.mkdir(self.__SAVE_DIR)

        self.loadData("test.csv")

    def saveData(self, fileName: str):
        fullDir = self.__FILE_CONFIG + fileName
        with open(fullDir, "w") as csv_file:
            csv_file.write("a, a, a\nb,b,b\nc,c,cc")
            pass

    def loadData(self, fileName: str):
        fullDir = self.__FILE_CONFIG + fileName
        if os.path.isfile(fullDir) and os.path.getsize(fullDir) > 0:
            with open(fullDir, "r") as csv_file:
                pass
        else:
            self.saveData(fileName)
