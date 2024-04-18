import csv
import os
from datetime import datetime

from PySide6.QtCore import QObject


class DataLog(QObject):
    __init = False
    __DEBUG__ = False

    __SAVE_DIR = "data"
    __FILE_CONFIG = "./" + __SAVE_DIR + "/"

    def __init__(self, serialNum, devNum):
        super().__init__()

        if os.path.isdir(self.__SAVE_DIR) is False:
            os.mkdir(self.__SAVE_DIR)

        self.serialNum = serialNum
        self.devNum = devNum

        current_time = datetime.now()
        formatted_time = current_time.strftime("%y%m%d.%H%M%S")
        self.fileName = f"{serialNum}_{devNum}_{formatted_time}.csv"
        self.writeData(["충전상태", "사이클", "전류", "전압", "온도", "오류코드"])

    def writeData(self, data):
        fullDir = self.__FILE_CONFIG + self.fileName
        with open(fullDir, "w", newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)

    def appendData(self, data):
        fullDir = self.__FILE_CONFIG + self.fileName
        with open(fullDir, "a", newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)

    # def loadData(self, fileName: str):
    #     fullDir = self.__FILE_CONFIG + fileName
    #     if os.path.isfile(fullDir) and os.path.getsize(fullDir) > 0:
    #         with open(fullDir, "r") as csv_file:
    #             pass
    #     else:
    #         self.saveData(fileName)
