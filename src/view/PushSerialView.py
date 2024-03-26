import re

from PySide6.QtCore import QObject

from src.MainUI import Ui_BCT
from src.repository.DataConfig import DataConfig


class PushSerialView(QObject):
    def __init__(self, mainWindow: Ui_BCT):
        super().__init__()

        self.view = mainWindow

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
        fixed = self.view.push_serial_fixed.text()
        value = self.view.push_serial_val.text()

        srMix = self.mix(value)
        self.view.push_serial_mix.setText(srMix)

        ##push 해서 결과에 따라서 아래의 동작을 해야함..

        suss = True
        if suss:
            self.view.push_serial_push.setStyleSheet("background-color: green")
            next = self.nextNumber(value)
            srMixNext = self.mix(next)
            self.view.push_serial_val.setText(next)
            self.view.push_serial_next.setText(srMixNext)

            dataConfig.setSerial(fixed, next)
            dataConfig.saveData()
        else:
            self.view.push_serial_push.setStyleSheet("background-color: red")

    def mix(self, value):
        return self.view.push_serial_fixed.text() + value

    def nextNumber(self, string):
        # 정규 표현식을 사용하여 문자열에서 숫자를 찾습니다.
        # \d는 숫자를 나타내는 메타 문자입니다.
        # (\d+)는 하나 이상의 연속된 숫자를 찾습니다.
        # 숫자가 발견되면 해당 숫자에 1을 더합니다.
        result = re.sub(r'(\d+)', lambda x: str(int(x.group(0)) + 1).zfill(len(x.group(0))), string)
        return result
