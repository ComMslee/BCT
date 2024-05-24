from typing import List

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QTableWidgetItem, QTableWidget, QLineEdit, QListWidget, QListWidgetItem

from src.MainUI import Ui_BCT
from src.repository.DataConfig import DataConfig
from src.util.FactoryWork import FactoryWork
from src.util.define import global_testCase


class BatteryFactoryView(QObject):
    def __init__(self, mainWindow: Ui_BCT):
        super().__init__()

        self.selected_dict = None
        self.view = mainWindow

        self.dataConfig = DataConfig()
        self.dataConfig.loadData()

        self.devThread: List[FactoryWork] = []
        self.devView = []

        self.initUI()
        self.updateUI()

    def initUI(self):
        dataConfig = self.dataConfig
        self.view.factory_start.clicked.connect(self.startCycle)
        self.view.factory_stop.clicked.connect(self.stopCycle)
        self.view.factory_select.clicked.connect(self.select_all_items)
        self.view.factory_temp.stateChanged.connect(self.onChangeTemp)
        self.view.factory_temp.setChecked(dataConfig.getTemp())

        colSize = [240, 90, 90]
        for view in [self.view.factory_table]:
            for i, size in enumerate(colSize):
                view.setColumnWidth(i, size)
        self.view.factory_stop.setEnabled(False)

        errlist = dataConfig.getErr()
        self.view.factory_list.setSelectionMode(QListWidget.MultiSelection)

        for key, value in global_testCase.items():
            item = QListWidgetItem(f"{key}: {value}")
            item.setData(1, key)  # Save the key in user data
            item.setData(2, value)  # Save the value in user data
            self.view.factory_list.addItem(item)

        for i in range(self.view.factory_list.count()):
            item: QListWidgetItem = self.view.factory_list.item(i)
            item.setSelected(item.data(2) in errlist.values())

        self.view.factory_list.itemSelectionChanged.connect(self.update_selected_items)

    def update_selected_items(self):
        dataConfig = self.dataConfig
        selected_items = self.view.factory_list.selectedItems()
        self.selected_dict = {item.data(1): item.data(2) for item in selected_items}
        dataConfig.setErr(self.selected_dict)
        dataConfig.saveData()
        # selected_texts = [f"{item.data(1)}: {item.data(2)}" for item in selected_items]
        # print("Selected: " + ", ".join(selected_texts))

    def select_all_items(self):
        selected_items = self.view.factory_list.selectedItems()
        itemCnt = self.view.factory_list.count()
        for i in range(self.view.factory_list.count()):
            item = self.view.factory_list.item(i)
            item.setSelected(len(selected_items) != itemCnt)

    def onChangeTemp(self, state):
        dataConfig = self.dataConfig
        dataConfig.setTemp(state)
        dataConfig.saveData()

    def updateUI(self):
        pass

    def startCycle(self):
        print("start cycle")
        dataConfig = self.dataConfig
        dataConfig.msgSaveData.emit()

        self.devThread = []
        devPort = [dataConfig.getComPort(1), dataConfig.getComPort(2)]
        self.devView = [DeviceView(self.view.factory_table, self.view.factory_result, 1),
                        DeviceView(self.view.factory_table, self.view.factory_result_2, 2)]
        for port, view in zip(devPort, self.devView):
            thread = FactoryWork(
                port, baudrate=dataConfig.getComBaudRate(),
                bTempTest=dataConfig.getTemp(),
                bErrTestDict=dataConfig.getErr()
            )
            thread.msgReadList.connect(view.pushTable)
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
                print("BatteryFactoryView::finally")
                self.enableBtn(True)

    def enableBtn(self, enable):
        self.view.factory_start.setEnabled(enable)
        self.view.factory_stop.setEnabled(not enable)
        self.view.tbMain.setTabEnabled(0, enable)
        self.view.tbMain.setTabEnabled(2, enable)


class DeviceView(QObject):
    def __init__(self, table: QTableWidget, resultView, devNum: int):
        super().__init__()
        self.table: QTableWidget = table
        self.resultView: QLineEdit = resultView
        self.devNum: int = devNum

        table.clearContents()
        row_count = table.rowCount()
        for row_index in range(row_count):
            table.removeRow(0)  # 첫 번째 행을 반복적으로 제거

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
                    if len(setVal) > 0:
                        table.setItem(row, target, QTableWidgetItem(setVal))
                return  # 작업 완료 후 함수 종료

        # 첫 번째 열의 값이 일치하는 행이 없는 경우
        newRowCount = table.rowCount()
        table.insertRow(newRowCount)
        table.setItem(newRowCount, 0, QTableWidgetItem(findVal))
        if len(setVal) > 0:
            table.setItem(newRowCount, target, QTableWidgetItem(setVal))

    def threadNoti(self, msg):
        if "write complete" in msg:
            print(f"DeviceView({self.devNum})::write complete")
            table = self.table
            cnt = 0
            for row in range(table.rowCount()):
                item = table.item(row, 0)
                if item:
                    item = table.item(row, self.devNum)
                    if item and "pass" == item.text():
                        print(f"{item.text()} : {item.text()}")
                        cnt += 1

            print(f"write complete is cnt {cnt} | {table.rowCount()}")
            if cnt == table.rowCount():
                self.resultView.setText("Pass")
