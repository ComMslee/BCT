from typing import List

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QTableWidgetItem, QTableWidget

from src.MainUI import Ui_BCT
from src.repository.DataConfig import DataConfig
from src.util.FactoryWork import FactoryWork


class BatteryFactoryView(QObject):
    def __init__(self, mainWindow: Ui_BCT):
        super().__init__()

        self.view = mainWindow

        self.dataConfig = DataConfig()
        self.dataConfig.loadData()

        self.devThread: List[FactoryWork] = []
        self.devView = []

        self.initUI()
        self.updateUI()

    def initUI(self):
        self.view.factory_start.clicked.connect(self.startCycle)
        self.view.factory_stop.clicked.connect(self.stopCycle)

        colSize = [240, 90, 90]
        for view in [self.view.factory_table]:
            for i, size in enumerate(colSize):
                view.setColumnWidth(i, size)
        self.view.factory_stop.setEnabled(False)

    def updateUI(self):
        pass

    def startCycle(self):
        print("start cycle")
        dataConfig = self.dataConfig
        self.devThread = []
        devPort = [dataConfig.getComPort(1), dataConfig.getComPort(2)]
        self.devView = [DeviceView(self.view.factory_table, 1), DeviceView(self.view.factory_table, 2)]
        for port, view in zip(devPort, self.devView):
            thread = FactoryWork(
                port, dataConfig.getComBaudRate(),
            )
            thread.msgReadList.connect(view.pushTable)
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
        self.view.factory_start.setEnabled(enable)
        self.view.factory_stop.setEnabled(not enable)
        self.view.tbMain.setTabEnabled(0, enable)
        self.view.tbMain.setTabEnabled(2, enable)


class DeviceView(QObject):
    def __init__(self, table: QTableWidget, devNum: int):
        super().__init__()
        self.table: QTableWidget = table
        self.devNum: int = devNum

    def pushTable(self, items: list):
        self.pushTableData(items, self.devNum)

    def pushTableData(self, items, target: int = 1):
        table = self.table
        findVal = str(items[0])
        setVal = str(items[1])

        for row in range(table.rowCount()):
            item = table.item(row, 0)
            if item and findVal == item.text():
                # 첫 번째 열의 값이 일치하는 경우
                item = table.item(row, target)
                if item:
                    # 해당 열의 값이 이미 있는 경우
                    item.setText(setVal)
                else:
                    # 해당 열의 값이 없는 경우
                    table.setItem(row, target, QTableWidgetItem(setVal))
                return  # 작업 완료 후 함수 종료

        # 첫 번째 열의 값이 일치하는 행이 없는 경우
        newRowCount = table.rowCount()
        table.insertRow(newRowCount)
        table.setItem(newRowCount, 0, QTableWidgetItem(findVal))
        table.setItem(newRowCount, target, QTableWidgetItem(setVal))
