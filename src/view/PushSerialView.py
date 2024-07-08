import re

from PySide6.QtCore import QObject

from src.MainUI import Ui_BCT
from src.repository.DataConfig import DataConfig
from src.util.SerialWork import SerialWorker


class PushSerialView(QObject):
    def __init__(self, mainWindow: Ui_BCT):
        super().__init__()

        self.view = mainWindow
        self.serialWork = None
        self.serialWork2 = None

        self.srMixNextVal = None
        self.nextVal = None

        self.dataConfig = DataConfig()
        self.dataConfig.loadData()

        self.initUI()
        self.updateUI()

    def initUI(self):
        self.view.push_serial_push.clicked.connect(self.onPush)
        self.view.push_serial_autocnt.stateChanged.connect(self.onChangeAuto)
        pass

    def updateUI(self):
        dataConfig = self.dataConfig
        fixed, value = dataConfig.getSerial()
        self.view.push_serial_fixed.setText(fixed)
        self.view.push_serial_val.setText(value)
        self.view.push_serial_autocnt.setChecked(dataConfig.getAuto())

    def onChangeAuto(self, state):
        dataConfig = self.dataConfig
        dataConfig.setAuto(state)
        dataConfig.saveData()

    def onPush(self):
        print("start cycle")
        dataConfig = self.dataConfig
        dataConfig.msgSaveData.emit()

        value = self.view.push_serial_val.text()
        srMix = self.mix(value)

        self.nextVal = self.nextNumber(value)
        self.srMixNextVal = self.mix(self.nextVal)

        self.view.push_serial_mix.setText(srMix)

        self.serialWork = SerialWorker(
            srMix,
            dataConfig.getComPort(1),
            dataConfig.getComBaudRate(),
        )
        self.serialWork.msgSerialRead.connect(self.pushResult)
        self.serialWork.start()

        self.serialWork2 = SerialWorker(
            srMix,
            dataConfig.getComPort(2),
            dataConfig.getComBaudRate(),
        )
        self.serialWork2.msgSerialRead.connect(self.pushResult2)
        self.serialWork2.start()

    def pushResult(self, writeNum, serialNum):
        self.result(writeNum, serialNum, self.view.push_dev01_version)

    def pushResult2(self, writeNum, serialNum):
        self.result(writeNum, serialNum, self.view.push_dev02_version)

    def result(self, writeNum, serialNum, view):
        view.setText(serialNum)

        if writeNum == serialNum:
            view.setStyleSheet("background-color: green")
            self.setNextVal()
        else:
            view.setStyleSheet("background-color: red")

    def setNextVal(self):
        dataConfig = self.dataConfig
        if dataConfig.getAuto():
            self.view.push_serial_val.setText(self.nextVal)
            self.view.push_serial_next.setText(self.srMixNextVal)

            dataConfig.setSerial(self.view.push_serial_fixed.text(), self.nextVal)
            dataConfig.saveData()

    def mix(self, value):
        return self.view.push_serial_fixed.text() + value

    def nextNumber(self, string):
        # 정규 표현식을 사용하여 문자열에서 숫자를 찾습니다.
        # \d는 숫자를 나타내는 메타 문자입니다.
        # (\d+)는 하나 이상의 연속된 숫자를 찾습니다.
        # 숫자가 발견되면 해당 숫자에 1을 더합니다.
        result = re.sub(r'(\d+)', lambda x: str(int(x.group(0)) + 1).zfill(len(x.group(0))), string)
        return result
