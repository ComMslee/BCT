import csv
import os
from datetime import datetime

from PySide6.QtCore import QObject


class DataLog(QObject):
    __init = False
    __DEBUG__ = False

    __SAVE_DIR = os.path.join(".", "data")

    def __init__(self, serialNum, devNum):
        super().__init__()

        current_time = datetime.now()
        formatted_time = current_time.strftime("%y%m%d")
        self.__SAVE_DIR = os.path.join(self.__SAVE_DIR, formatted_time)
        if os.path.isdir(self.__SAVE_DIR) is False:
            os.mkdir(self.__SAVE_DIR)

        self.serialNum = serialNum
        self.devNum = devNum
        formatted_time = current_time.strftime("%y%m%d_%H%M%S")
        self.fileName = f"{formatted_time}_{serialNum}_{devNum}.csv"
        self.writeData(["상태", "카운트", "Soc", "전류", "전압", "온도", "오류코드"])

    def writeData(self, data):
        fullDir = os.path.join(self.__SAVE_DIR, self.fileName)
        with open(fullDir, "w", newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)

    def appendData(self, data):
        fullDir = os.path.join(self.__SAVE_DIR, self.fileName)
        with open(fullDir, "a", newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)
