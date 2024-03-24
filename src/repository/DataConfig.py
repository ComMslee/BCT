import json
import os
import re

from PySide6 import QtCore
from PySide6.QtCore import QObject


class DataConfig(QObject):
    msgUpdateData = QtCore.Signal()

    __init = False
    __DEBUG__ = False

    __SAVE_DIR = "data"
    __FILE_CONFIG = "./data/config.json"

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(DataConfig, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if self.__init:
            return
        self.__init = True

        if os.path.isdir(self.__SAVE_DIR) is False:
            os.mkdir(self.__SAVE_DIR)

        super(DataConfig, self).__init__()
        self.__VERSION = 0

        self.__version = 0
        self.__comPort_dev01 = "COM3"  # ComPort = "/dev/tty.usbserial-FTH0U0HX"
        self.__comPort_dev02 = "COM4"  # ComPort = "/dev/tty.usbserial-FTH0U0HX"
        self.__comBaudRate = 115200

        self.__selectTab = {}

        self.__cycle = 1000
        self.__onTime = [0, 1, 0]
        self.__offTime = [0, 1, 0]

        self.__serial_fixed = ""
        self.__serial_val = ""
        self.__auto_cnt = True

        self.loadData()

    def saveData(self):
        saveConfig = {
            "version": self.__VERSION,
            "setup": {
                "last_tap": self.__selectTab
            },
            "com": {
                "rate": self.__comBaudRate,
                "port_dev1": self.__comPort_dev01,
                "port_dev2": self.__comPort_dev02,
            },

            "tap_battery_test": {
                "cycle": self.__cycle,
                "ontime": self.__onTime,
                "offtime": self.__offTime,
            },
            "tap_push_serial": {
                "auto_cnt": self.__auto_cnt,
                "serial_fixed": self.__serial_fixed,
                "serial_val": self.__serial_val,
            }
        }
        with open(self.__FILE_CONFIG, "w") as json_file:
            json.dump(saveConfig, json_file)
            print("Config save. " + (json.dumps(saveConfig) if self.__DEBUG__ else ""))

    def loadData(self):
        if os.path.isfile(self.__FILE_CONFIG) and os.path.getsize(self.__FILE_CONFIG) > 0:
            with open(self.__FILE_CONFIG, "r") as json_file:
                loadConfig = json.load(json_file)
                print("Config load. " + (json.dumps(loadConfig) if self.__DEBUG__ else ""))
                if "version" in loadConfig:
                    self.__version = loadConfig["version"]

                if "setup" in loadConfig:
                    setup = loadConfig["setup"]
                    if isinstance(setup, dict):
                        self.__selectTab = setup["last_tap"]

                if "com" in loadConfig:
                    comInfo = loadConfig["com"]
                    if isinstance(comInfo, dict):
                        self.__comPort_dev01 = comInfo["port_dev1"]
                        self.__comPort_dev02 = comInfo["port_dev2"]
                        self.__comBaudRate = comInfo["rate"]
                        if self.__comBaudRate == 0:
                            self.__comBaudRate = 115200

                if "tap_battery_test" in loadConfig:
                    tapPush = loadConfig["tap_battery_test"]
                    if isinstance(tapPush, dict):
                        self.__cycle = tapPush["cycle"]
                        self.__onTime = tapPush["ontime"]
                        self.__offTime = tapPush["offtime"]

                if "tap_push_serial" in loadConfig:
                    tapRush = loadConfig["tap_push_serial"]
                    if isinstance(tapRush, dict):
                        self.__auto_cnt = tapRush["auto_cnt"]
                        self.__serial_fixed = tapRush["serial_fixed"]
                        self.__serial_val = tapRush["serial_val"]

        else:
            self.saveData()

    # config
    def setComPort(self, index: int, port: str):
        matchPort = re.compile("(^com)\\d{1,3}", re.I).match(port)
        if matchPort is not None:
            comtext = matchPort.group().upper()
            if index == 2:
                self.__comPort_dev02 = comtext
            else:
                self.__comPort_dev01 = comtext

    def getComPort(self, index: int) -> str:
        if index == 2:
            return self.__comPort_dev02
        else:
            return self.__comPort_dev01

    def setComBaudRate(self, rate):
        if rate.isdigit() and int(rate) != 0:
            self.__comBaudRate = rate
        else:
            if len(rate) == 0:
                self.__comBaudRate = 115200

    def getComBaudRate(self):
        return self.__comBaudRate

    def getSelectTab(self):
        return self.__selectTab
