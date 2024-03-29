from PySide6.QtCore import QObject, Qt
from PySide6.QtWidgets import QLineEdit, QTableWidgetItem, QTableWidget

from src.MainUI import Ui_BCT
from src.repository.DataConfig import DataConfig
from src.util.SerialWorkCycle import SerialCycleWorker


class BatteryCycleView(QObject):
    def __init__(self, mainWindow: Ui_BCT):
        super().__init__()

        self.dev01: SerialCycleWorker = None
        self.dev02: SerialCycleWorker = None
        self.view = mainWindow

        self.dataConfig = DataConfig()
        self.dataConfig.loadData()

        self.initUI()
        self.updateUI()
        self.cnt = 0

    def initUI(self):
        self.view.config_btn_start.clicked.connect(self.startCycle)
        self.view.config_btn_stop.clicked.connect(self.stopCycle)
        self.dataConfig.msgSaveData.connect(self.saveData)

        colSize = [70, 80, 110, 110, 110, 110]
        self.setTableColumnSizes(self.view.dev_table, colSize)  # 각 열의 크기를 설정합니다.
        self.setTableColumnSizes(self.view.dev_table_2, colSize)  # 각 열의 크기를 설정합니다.
        self.view.config_btn_stop.setEnabled(False)

    def updateUI(self):
        self.view.config_cycle.setText(str(self.dataConfig.getCycle()))
        ontime, offtime = self.dataConfig.getTime()
        self.view.config_time_on_h.setText(str(ontime[0]))
        self.view.config_time_on_m.setText(str(ontime[1]))
        self.view.config_time_on_s.setText(str(ontime[2]))
        self.view.config_time_off_h.setText(str(offtime[0]))
        self.view.config_time_off_m.setText(str(offtime[1]))
        self.view.config_time_off_s.setText(str(offtime[2]))

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
        self.saveData()

        dataconfig = self.dataConfig
        self.dev01 = SerialCycleWorker(
            dataconfig.getComPort(1),
            dataconfig.getTime(),
            dataconfig.getComBaudRate(),
            dataconfig.getCycle()
        )
        self.dev01.start()
        self.dev01.msgReadList.connect(self.pushTableData)
        self.dev01.msgThread.connect(self.threadNoti)

        self.dev02 = SerialCycleWorker(
            dataconfig.getComPort(2),
            dataconfig.getTime(),
            dataconfig.getComBaudRate(),
            dataconfig.getCycle()
        )
        self.dev02.start()
        # self.dev02.msgReadList.connect(self.pushTableData)

        self.view.config_btn_start.setEnabled(False)
        self.view.config_btn_stop.setEnabled(True)

    def stopCycle(self):
        if self.dev01 is not None:
            self.dev01.stopWork()
        if self.dev02 is not None:
            self.dev02.stopWork()
        print("start cycle stop")
        self.view.config_btn_start.setEnabled(True)
        self.view.config_btn_stop.setEnabled(False)

    def threadNoti(self, msg):
        if "write complete" in msg:
            print("write complete")
            self.view.config_btn_start.setEnabled(True)
            self.view.config_btn_stop.setEnabled(False)

    def setTableColumnSizes(self, view: QTableWidget, sizes):
        for i, size in enumerate(sizes):
            view.setColumnWidth(i, size)

    def pushTableData(self, items: list):
        self.cnt += 1
        self.view.dev_table.insertRow(0)
        for col, item in enumerate(items):
            data = QTableWidgetItem(item)
            data.setTextAlignment(Qt.AlignCenter)
            data.setFlags(data.flags() & ~Qt.ItemIsEditable)  # 편집 불가능
            self.view.dev_table.setItem(0, col, data)

    def changeLEDState(self, idx: int, state: int):
        view: QLineEdit = None
        if idx == 2:
            view = self.view.dev_led_state.setStyleSheet()
        else:
            view = self.view.dev_led_state_2.setStyleSheet()
