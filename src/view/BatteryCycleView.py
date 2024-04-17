from PySide6.QtCore import QObject, Qt
from PySide6.QtWidgets import QTableWidgetItem, QTableWidget
from typing import List

from src.MainUI import Ui_BCT
from src.repository.DataConfig import DataConfig
from src.util.SerialWorkCycle import SerialCycleWorker


class BatteryCycleView(QObject):
    def __init__(self, mainWindow: Ui_BCT):
        super().__init__()

        self.devThread: List[SerialCycleWorker] = []
        self.devView = []
        self.view = mainWindow

        self.dataConfig = DataConfig()
        self.dataConfig.loadData()

        self.initUI()
        self.updateUI()

    def initUI(self):
        self.view.config_btn_start.clicked.connect(self.startCycle)
        self.view.config_btn_stop.clicked.connect(self.stopCycle)
        self.dataConfig.msgSaveData.connect(self.saveData)

        colSize = [65, 85, 105, 105, 105, 105]
        for view in [self.view.dev_table, self.view.dev_table_2]:
            for i, size in enumerate(colSize):
                view.setColumnWidth(i, size)
        self.view.config_btn_stop.setEnabled(False)

    def updateUI(self):
        self.view.config_cycle.setText(str(self.dataConfig.getCycle()))
        onTime, offTime = self.dataConfig.getTime()
        for view, time in zip([self.view.config_time_on_h, self.view.config_time_on_m, self.view.config_time_on_s],
                              onTime):
            view.setText(str(time))
        for view, time in zip([self.view.config_time_off_h, self.view.config_time_off_m, self.view.config_time_off_s],
                              offTime):
            view.setText(str(time))

    def saveData(self):
        dataconfig = self.dataConfig
        dataconfig.setTime(
            [
                int(self.view.config_time_on_h.text()),
                int(self.view.config_time_on_m.text()),
                int(self.view.config_time_on_s.text()),
            ],
            [
                int(self.view.config_time_off_h.text()),
                int(self.view.config_time_off_m.text()),
                int(self.view.config_time_off_s.text()),
            ])
        dataconfig.setCycle(self.view.config_cycle.text())
        dataconfig.saveData()

    def startCycle(self):
        print("start cycle")
        dataconfig = self.dataConfig
        dataconfig.msgSaveData.emit()

        self.devThread = []
        devPort = [dataconfig.getComPort(1), dataconfig.getComPort(2)]
        self.devView = [DeviceView(
            self.view.dev_version, self.view.dev_cycle,
            self.view.dev_ampere, self.view.dev_volt, self.view.dev_temperature,
            self.view.dev_led_state,
            self.view.dev_table
        ), DeviceView(
            self.view.dev_version_2, self.view.dev_cycle_2,
            self.view.dev_ampere_2, self.view.dev_volt_2, self.view.dev_temperature_2,
            self.view.dev_led_state_2,
            self.view.dev_table_2
        )]

        for port, view in zip(devPort, self.devView):
            thread = SerialCycleWorker(
                port, dataconfig.getComBaudRate(),
                dataconfig.getTime(), dataconfig.getCycle()
            )
            thread.msgReadList.connect(view.pushTableData)
            thread.msgReadRealTime.connect(view.pushData)
            thread.msgReadSerial.connect(view.pushSerial)
            thread.msgCnt.connect(view.msgCnt)
            thread.msgThread.connect(self.threadNoti)
            thread.start()
            self.devThread.append(thread)

        self.enableBtn(False)

    def stopCycle(self):
        for dev in self.devThread:
            dev.stopWork()
        print("start cycle stop")
        self.enableBtn(True)

    def threadNoti(self, msg):
        if "write complete" in msg:
            print("write complete")
            self.enableBtn(True)

    def enableBtn(self, enable):
        self.view.config_btn_start.setEnabled(enable)
        self.view.config_btn_stop.setEnabled(not enable)
        self.view.tbMain.setTabEnabled(1, enable)
        self.view.tbMain.setTabEnabled(2, enable)

    def setTableColumnSize(self, view: QTableWidget, sizes):
        for i, size in enumerate(sizes):
            view.setColumnWidth(i, size)


class DeviceView(QObject):
    def __init__(self, version, cycle, ampere, volt, temp, led, table):
        super().__init__()
        self.version = version
        self.cycle = cycle
        self.ampere = ampere
        self.volt = volt
        self.temp = temp
        self.led = led
        self.table = table

    def pushTableData(self, items: list):
        self.table.insertRow(0)
        for col, item in enumerate(items):
            data = QTableWidgetItem(str(item))
            data.setTextAlignment(Qt.AlignCenter)
            data.setFlags(data.flags() & ~Qt.ItemIsEditable)  # 편집 불가능
            self.table.setItem(0, col, data)

    def pushData(self, items: list):
        self.ampere.setText(str(items[0]))
        self.volt.setText(str(items[1]))
        self.temp.setText(str(items[2]))

        progress_txt = {
            0: "ALL OFF",
            1: "Start",
            2: "Battery Con",
            3: "Charging Fail",
            4: "Charging Wait",
            5: "Percent"
        }.get(items[3], "")
        self.led.setText(progress_txt)

    def pushSerial(self, serialNum: str):
        self.version.setText(serialNum)

    def msgCnt(self, idx: int):
        self.cycle.setText(str(idx))
