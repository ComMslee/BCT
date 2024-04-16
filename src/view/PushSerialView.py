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
        dataConfig = self.dataConfig
        value = self.view.push_serial_val.text()
        srMix = self.mix(value)

        self.view.push_serial_mix.setText(srMix)

        self.serialWork = SerialWorker(
            dataConfig.getComPort(1),
            srMix,
            dataConfig.getComBaudRate(),
        )
        self.serialWork.msgSerialRead.connect(self.pushResult)
        self.serialWork.start()

        self.serialWork2 = SerialWorker(
            dataConfig.getComPort(2),
            srMix,
            dataConfig.getComBaudRate(),
        )
        self.serialWork2.msgSerialRead.connect(self.pushResult2)
        self.serialWork2.start()

    def pushResult(self, serialNum):
        self.result(serialNum, self.view.push_dev01_version)

    def pushResult2(self, serialNum):
        self.result(serialNum, self.view.push_dev02_version)

    def result(self, serialNum, view):
        view.setText(serialNum)
        dataConfig = self.dataConfig
        value = self.view.push_serial_val.text()
        srMix = self.mix(value)

        if srMix == serialNum:
            view.setStyleSheet("background-color: green")
            nextVal = self.nextNumber(value)
            srMixNextVal = self.mix(nextVal)
            self.view.push_serial_val.setText(nextVal)
            self.view.push_serial_next.setText(srMixNextVal)

            dataConfig.setSerial(self.view.push_serial_fixed.text(), nextVal)
            dataConfig.saveData()
        else:
            view.setStyleSheet("background-color: red")

    def mix(self, value):
        return self.view.push_serial_fixed.text() + value

    def nextNumber(self, string):
        # 정규 표현식을 사용하여 문자열에서 숫자를 찾습니다.
        # \d는 숫자를 나타내는 메타 문자입니다.
        # (\d+)는 하나 이상의 연속된 숫자를 찾습니다.
        # 숫자가 발견되면 해당 숫자에 1을 더합니다.
        result = re.sub(r'(\d+)', lambda x: str(int(x.group(0)) + 1).zfill(len(x.group(0))), string)
        return result
