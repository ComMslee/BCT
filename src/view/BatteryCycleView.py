from typing import List

from PySide6.QtCore import QObject, Qt
from PySide6.QtWidgets import QTableWidgetItem, QTableWidget

from src.MainUI import Ui_BCT
from src.repository.DataConfig import DataConfig
from src.repository.DataLog import DataLog
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

        colSize = [65, 85, 105, 105, 90, 105]
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
        dataConfig = self.dataConfig
        dataConfig.setTime(
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
        dataConfig.setCycle(self.view.config_cycle.text())
        dataConfig.saveData()

    def startCycle(self):
        print("start cycle")
        dataConfig = self.dataConfig
        dataConfig.msgSaveData.emit()

        self.devThread = []
        devPort = [dataConfig.getComPort(1), dataConfig.getComPort(2)]
        self.devView = [DeviceView(
            "dev01",
            self.view.dev_version, self.view.dev_cycle,
            self.view.dev_ampere, self.view.dev_volt, self.view.dev_temperature,
            self.view.dev_led_state,
            self.view.dev_table
        ), DeviceView(
            "dev02",
            self.view.dev_version_2, self.view.dev_cycle_2,
            self.view.dev_ampere_2, self.view.dev_volt_2, self.view.dev_temperature_2,
            self.view.dev_led_state_2,
            self.view.dev_table_2
        )]

        for port, view in zip(devPort, self.devView):
            thread = SerialCycleWorker(
                port, dataConfig.getComBaudRate(),
                dataConfig.getTime(), dataConfig.getCycle()
            )
            thread.msgReadList.connect(view.pushTableData)
            thread.msgReadRealTime.connect(view.pushData)
            thread.msgReadSerial.connect(view.pushSerial)
            thread.msgCnt.connect(view.msgCnt)
            thread.msgThread.connect(view.threadNoti)
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
        if "finally" in msg:
            cnt = 0
            for dev in self.devThread:
                if not dev.bRunning:
                    cnt += 1
            if len(self.devThread) == cnt:
                print("BatteryCycleView::finally")
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
    def __init__(self, devNum, version, cycle, ampere, volt, temp, led, table):
        super().__init__()
        self.devNum = devNum
        self.version = version
        self.cycle = cycle
        self.ampere = ampere
        self.volt = volt
        self.temp = temp
        self.led = led
        self.table = table

        table.clearContents()
        row_count = table.rowCount()
        for row_index in range(row_count):
            table.removeRow(0)  # 첫 번째 행을 반복적으로 제거

    def pushTableData(self, items: list):
        self.table.insertRow(0)
        for col, item in enumerate(items):
            data = QTableWidgetItem(str(item))
            data.setTextAlignment(Qt.AlignCenter)
            data.setFlags(data.flags() & ~Qt.ItemIsEditable)  # 편집 불가능
            self.table.setItem(0, col, data)

    def pushData(self, items: dict):
        self.ampere.setText(str(items["current"]))
        self.volt.setText(str(items["voltage"]))
        self.temp.setText(str(items["tempAvg"]))

        progress_txt = {
            0: "ALL OFF",
            1: "Start",
            2: "Battery Con",
            3: "Charging Fail",
            4: "Charging Wait",
            5: "Percent"
        }.get(items["progrssbar"], "")
        self.led.setText(progress_txt)

    def pushSerial(self, serialNum: str):
        self.version.setText(serialNum)

    def msgCnt(self, idx: int):
        self.cycle.setText(str(idx))

    def threadNoti(self, msg):
        if "write complete" in msg:
            print(f"DeviceView({self.devNum})::write complete")
            datalog = DataLog(self.version.text(), self.devNum)

            for row in range(self.table.rowCount()):
                row_data = []
                for column in range(self.table.columnCount()):
                    item = self.table.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append("")
                datalog.appendData(row_data)
