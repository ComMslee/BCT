# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BCT_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_BCT(object):
    def setupUi(self, BCT):
        if not BCT.objectName():
            BCT.setObjectName(u"BCT")
        BCT.resize(800, 694)
        self.tbMain = QTabWidget(BCT)
        self.tbMain.setObjectName(u"tbMain")
        self.tbMain.setGeometry(QRect(0, 70, 801, 621))
        self.tbMain.setTabBarAutoHide(False)
        self.tbBatteryCycle = QWidget()
        self.tbBatteryCycle.setObjectName(u"tbBatteryCycle")
        self.groupBox = QGroupBox(self.tbBatteryCycle)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 100, 791, 241))
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 20, 151, 211))
        self.gridLayoutWidget_2 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 80, 131, 116))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dev_volt = QLineEdit(self.gridLayoutWidget_2)
        self.dev_volt.setObjectName(u"dev_volt")
        self.dev_volt.setAlignment(Qt.AlignCenter)
        self.dev_volt.setReadOnly(True)

        self.gridLayout_2.addWidget(self.dev_volt, 0, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 2, 1, 1, 1)

        self.dev_temperature = QLineEdit(self.gridLayoutWidget_2)
        self.dev_temperature.setObjectName(u"dev_temperature")
        self.dev_temperature.setAlignment(Qt.AlignCenter)
        self.dev_temperature.setReadOnly(True)

        self.gridLayout_2.addWidget(self.dev_temperature, 2, 0, 1, 1)

        self.dev_ampere = QLineEdit(self.gridLayoutWidget_2)
        self.dev_ampere.setObjectName(u"dev_ampere")
        self.dev_ampere.setAlignment(Qt.AlignCenter)
        self.dev_ampere.setReadOnly(True)

        self.gridLayout_2.addWidget(self.dev_ampere, 1, 0, 1, 1)

        self.dev_led_state = QLineEdit(self.gridLayoutWidget_2)
        self.dev_led_state.setObjectName(u"dev_led_state")
        self.dev_led_state.setAlignment(Qt.AlignCenter)
        self.dev_led_state.setReadOnly(True)

        self.gridLayout_2.addWidget(self.dev_led_state, 3, 0, 1, 2)

        self.gridLayoutWidget_3 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 30, 131, 51))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.dev_cycle = QLineEdit(self.gridLayoutWidget_3)
        self.dev_cycle.setObjectName(u"dev_cycle")
        self.dev_cycle.setAlignment(Qt.AlignCenter)
        self.dev_cycle.setReadOnly(True)

        self.gridLayout_3.addWidget(self.dev_cycle, 1, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.dev_version = QLineEdit(self.gridLayoutWidget_3)
        self.dev_version.setObjectName(u"dev_version")
        self.dev_version.setAlignment(Qt.AlignCenter)
        self.dev_version.setReadOnly(True)

        self.gridLayout_3.addWidget(self.dev_version, 0, 1, 1, 1)

        self.dev_table = QTableWidget(self.groupBox)
        if (self.dev_table.columnCount() < 6):
            self.dev_table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.dev_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.dev_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.dev_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.dev_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.dev_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.dev_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.dev_table.setObjectName(u"dev_table")
        self.dev_table.setGeometry(QRect(170, 30, 611, 201))
        self.groupBox_4 = QGroupBox(self.tbBatteryCycle)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 0, 541, 101))
        self.gridLayoutWidget_4 = QWidget(self.groupBox_4)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(101, 30, 291, 61))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.gridLayoutWidget_4)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_14, 1, 4, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.config_time_on_h = QLineEdit(self.gridLayoutWidget_4)
        self.config_time_on_h.setObjectName(u"config_time_on_h")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(60)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.config_time_on_h.sizePolicy().hasHeightForWidth())
        self.config_time_on_h.setSizePolicy(sizePolicy1)
        self.config_time_on_h.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.config_time_on_h)

        self.label_43 = QLabel(self.gridLayoutWidget_4)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_3.addWidget(self.label_43)

        self.config_time_on_m = QLineEdit(self.gridLayoutWidget_4)
        self.config_time_on_m.setObjectName(u"config_time_on_m")
        sizePolicy1.setHeightForWidth(self.config_time_on_m.sizePolicy().hasHeightForWidth())
        self.config_time_on_m.setSizePolicy(sizePolicy1)
        self.config_time_on_m.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.config_time_on_m)

        self.label_45 = QLabel(self.gridLayoutWidget_4)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_3.addWidget(self.label_45)

        self.config_time_on_s = QLineEdit(self.gridLayoutWidget_4)
        self.config_time_on_s.setObjectName(u"config_time_on_s")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(60)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.config_time_on_s.sizePolicy().hasHeightForWidth())
        self.config_time_on_s.setSizePolicy(sizePolicy2)
        self.config_time_on_s.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.config_time_on_s)

        self.label_47 = QLabel(self.gridLayoutWidget_4)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_3.addWidget(self.label_47)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 0, 5, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_4)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_13, 0, 4, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.config_time_off_h = QLineEdit(self.gridLayoutWidget_4)
        self.config_time_off_h.setObjectName(u"config_time_off_h")
        sizePolicy1.setHeightForWidth(self.config_time_off_h.sizePolicy().hasHeightForWidth())
        self.config_time_off_h.setSizePolicy(sizePolicy1)
        self.config_time_off_h.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.config_time_off_h)

        self.label_44 = QLabel(self.gridLayoutWidget_4)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_4.addWidget(self.label_44)

        self.config_time_off_m = QLineEdit(self.gridLayoutWidget_4)
        self.config_time_off_m.setObjectName(u"config_time_off_m")
        sizePolicy1.setHeightForWidth(self.config_time_off_m.sizePolicy().hasHeightForWidth())
        self.config_time_off_m.setSizePolicy(sizePolicy1)
        self.config_time_off_m.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.config_time_off_m)

        self.label_46 = QLabel(self.gridLayoutWidget_4)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_4.addWidget(self.label_46)

        self.config_time_off_s = QLineEdit(self.gridLayoutWidget_4)
        self.config_time_off_s.setObjectName(u"config_time_off_s")
        sizePolicy2.setHeightForWidth(self.config_time_off_s.sizePolicy().hasHeightForWidth())
        self.config_time_off_s.setSizePolicy(sizePolicy2)
        self.config_time_off_s.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.config_time_off_s)

        self.label_48 = QLabel(self.gridLayoutWidget_4)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_4.addWidget(self.label_48)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 1, 5, 1, 1)

        self.verticalLayoutWidget = QWidget(self.groupBox_4)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(420, 30, 111, 62))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.config_btn_start = QPushButton(self.verticalLayoutWidget)
        self.config_btn_start.setObjectName(u"config_btn_start")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.config_btn_start.sizePolicy().hasHeightForWidth())
        self.config_btn_start.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.config_btn_start)

        self.config_btn_stop = QPushButton(self.verticalLayoutWidget)
        self.config_btn_stop.setObjectName(u"config_btn_stop")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.config_btn_stop.sizePolicy().hasHeightForWidth())
        self.config_btn_stop.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.config_btn_stop)

        self.verticalLayoutWidget_2 = QWidget(self.groupBox_4)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 30, 81, 61))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.verticalLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy4.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy4)

        self.verticalLayout_2.addWidget(self.label_12)

        self.config_cycle = QLineEdit(self.verticalLayoutWidget_2)
        self.config_cycle.setObjectName(u"config_cycle")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.config_cycle.sizePolicy().hasHeightForWidth())
        self.config_cycle.setSizePolicy(sizePolicy5)
        self.config_cycle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.config_cycle)

        self.groupBox_7 = QGroupBox(self.tbBatteryCycle)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(550, 0, 231, 101))
        self.gridLayoutWidget_7 = QWidget(self.groupBox_7)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(10, 30, 211, 61))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.gridLayoutWidget_7)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_7.addWidget(self.label_27, 1, 0, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget_7)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_7.addWidget(self.label_25, 0, 0, 1, 1)

        self.dev_result_2 = QLineEdit(self.gridLayoutWidget_7)
        self.dev_result_2.setObjectName(u"dev_result_2")
        self.dev_result_2.setAlignment(Qt.AlignCenter)
        self.dev_result_2.setReadOnly(True)

        self.gridLayout_7.addWidget(self.dev_result_2, 1, 1, 1, 1)

        self.dev_result = QLineEdit(self.gridLayoutWidget_7)
        self.dev_result.setObjectName(u"dev_result")
        self.dev_result.setAlignment(Qt.AlignCenter)
        self.dev_result.setReadOnly(True)

        self.gridLayout_7.addWidget(self.dev_result, 0, 1, 1, 1)

        self.groupBox_8 = QGroupBox(self.tbBatteryCycle)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(0, 350, 791, 241))
        self.groupBox_9 = QGroupBox(self.groupBox_8)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(10, 20, 151, 211))
        self.gridLayoutWidget_8 = QWidget(self.groupBox_9)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(10, 80, 131, 116))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.dev_volt_2 = QLineEdit(self.gridLayoutWidget_8)
        self.dev_volt_2.setObjectName(u"dev_volt_2")
        self.dev_volt_2.setAlignment(Qt.AlignCenter)
        self.dev_volt_2.setReadOnly(True)

        self.gridLayout_8.addWidget(self.dev_volt_2, 0, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_8)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_8.addWidget(self.label_9, 1, 1, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_8)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.label_10, 0, 1, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_8)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_8.addWidget(self.label_11, 2, 1, 1, 1)

        self.dev_temperature_2 = QLineEdit(self.gridLayoutWidget_8)
        self.dev_temperature_2.setObjectName(u"dev_temperature_2")
        self.dev_temperature_2.setAlignment(Qt.AlignCenter)
        self.dev_temperature_2.setReadOnly(True)

        self.gridLayout_8.addWidget(self.dev_temperature_2, 2, 0, 1, 1)

        self.dev_ampere_2 = QLineEdit(self.gridLayoutWidget_8)
        self.dev_ampere_2.setObjectName(u"dev_ampere_2")
        self.dev_ampere_2.setAlignment(Qt.AlignCenter)
        self.dev_ampere_2.setReadOnly(True)

        self.gridLayout_8.addWidget(self.dev_ampere_2, 1, 0, 1, 1)

        self.dev_led_state_2 = QLineEdit(self.gridLayoutWidget_8)
        self.dev_led_state_2.setObjectName(u"dev_led_state_2")
        self.dev_led_state_2.setAlignment(Qt.AlignCenter)
        self.dev_led_state_2.setReadOnly(True)

        self.gridLayout_8.addWidget(self.dev_led_state_2, 3, 0, 1, 2)

        self.gridLayoutWidget_9 = QWidget(self.groupBox_9)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(10, 30, 131, 54))
        self.gridLayout_9 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.dev_cycle_2 = QLineEdit(self.gridLayoutWidget_9)
        self.dev_cycle_2.setObjectName(u"dev_cycle_2")
        self.dev_cycle_2.setAlignment(Qt.AlignCenter)
        self.dev_cycle_2.setReadOnly(True)

        self.gridLayout_9.addWidget(self.dev_cycle_2, 1, 1, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget_9)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_9.addWidget(self.label_20, 1, 0, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget_9)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_9.addWidget(self.label_21, 0, 0, 1, 1)

        self.dev_version_2 = QLineEdit(self.gridLayoutWidget_9)
        self.dev_version_2.setObjectName(u"dev_version_2")
        self.dev_version_2.setAlignment(Qt.AlignCenter)
        self.dev_version_2.setReadOnly(True)

        self.gridLayout_9.addWidget(self.dev_version_2, 0, 1, 1, 1)

        self.dev_table_2 = QTableWidget(self.groupBox_8)
        if (self.dev_table_2.columnCount() < 6):
            self.dev_table_2.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.dev_table_2.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.dev_table_2.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.dev_table_2.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.dev_table_2.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.dev_table_2.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.dev_table_2.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.dev_table_2.setObjectName(u"dev_table_2")
        self.dev_table_2.setGeometry(QRect(170, 30, 611, 201))
        self.tbMain.addTab(self.tbBatteryCycle, "")
        self.tbBatteryFactory = QWidget()
        self.tbBatteryFactory.setObjectName(u"tbBatteryFactory")
        self.tableWidget = QTableWidget(self.tbBatteryFactory)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 0, 311, 541))
        self.config_btn_start_2 = QPushButton(self.tbBatteryFactory)
        self.config_btn_start_2.setObjectName(u"config_btn_start_2")
        self.config_btn_start_2.setGeometry(QRect(330, 0, 91, 91))
        sizePolicy3.setHeightForWidth(self.config_btn_start_2.sizePolicy().hasHeightForWidth())
        self.config_btn_start_2.setSizePolicy(sizePolicy3)
        self.tbMain.addTab(self.tbBatteryFactory, "")
        self.tbSerial = QWidget()
        self.tbSerial.setObjectName(u"tbSerial")
        self.groupBox_5 = QGroupBox(self.tbSerial)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 0, 311, 91))
        self.gridLayoutWidget_5 = QWidget(self.groupBox_5)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 30, 291, 57))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.gridLayoutWidget_5)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_5)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_5.addWidget(self.label_16, 1, 0, 1, 1)

        self.push_dev01_version = QLineEdit(self.gridLayoutWidget_5)
        self.push_dev01_version.setObjectName(u"push_dev01_version")
        self.push_dev01_version.setReadOnly(True)

        self.gridLayout_5.addWidget(self.push_dev01_version, 0, 1, 1, 1)

        self.push_dev02_version = QLineEdit(self.gridLayoutWidget_5)
        self.push_dev02_version.setObjectName(u"push_dev02_version")
        self.push_dev02_version.setReadOnly(True)

        self.gridLayout_5.addWidget(self.push_dev02_version, 1, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.tbSerial)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(340, 0, 431, 151))
        self.gridLayoutWidget_6 = QWidget(self.groupBox_6)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(10, 30, 411, 111))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.gridLayoutWidget_6)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_6.addWidget(self.label_18, 0, 2, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget_6)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_6.addWidget(self.label_19, 1, 0, 1, 1)

        self.push_serial_fixed = QLineEdit(self.gridLayoutWidget_6)
        self.push_serial_fixed.setObjectName(u"push_serial_fixed")

        self.gridLayout_6.addWidget(self.push_serial_fixed, 0, 1, 1, 1)

        self.push_serial_autocnt = QCheckBox(self.gridLayoutWidget_6)
        self.push_serial_autocnt.setObjectName(u"push_serial_autocnt")

        self.gridLayout_6.addWidget(self.push_serial_autocnt, 0, 4, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget_6)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_6.addWidget(self.label_17, 0, 0, 1, 1)

        self.push_serial_val = QLineEdit(self.gridLayoutWidget_6)
        self.push_serial_val.setObjectName(u"push_serial_val")

        self.gridLayout_6.addWidget(self.push_serial_val, 0, 3, 1, 1)

        self.push_serial_next = QLineEdit(self.gridLayoutWidget_6)
        self.push_serial_next.setObjectName(u"push_serial_next")
        self.push_serial_next.setReadOnly(True)

        self.gridLayout_6.addWidget(self.push_serial_next, 2, 1, 1, 3)

        self.push_serial_mix = QLineEdit(self.gridLayoutWidget_6)
        self.push_serial_mix.setObjectName(u"push_serial_mix")
        self.push_serial_mix.setReadOnly(True)

        self.gridLayout_6.addWidget(self.push_serial_mix, 1, 1, 1, 3)

        self.label_26 = QLabel(self.gridLayoutWidget_6)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_6.addWidget(self.label_26, 2, 0, 1, 1)

        self.push_serial_push = QPushButton(self.gridLayoutWidget_6)
        self.push_serial_push.setObjectName(u"push_serial_push")
        sizePolicy3.setHeightForWidth(self.push_serial_push.sizePolicy().hasHeightForWidth())
        self.push_serial_push.setSizePolicy(sizePolicy3)

        self.gridLayout_6.addWidget(self.push_serial_push, 1, 4, 2, 1)

        self.tbMain.addTab(self.tbSerial, "")
        self.groupBox_2 = QGroupBox(BCT)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 0, 651, 71))
        self.gridLayoutWidget = QWidget(self.groupBox_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 30, 631, 31))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.dev_baud = QLineEdit(self.gridLayoutWidget)
        self.dev_baud.setObjectName(u"dev_baud")
        self.dev_baud.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.dev_baud, 0, 1, 1, 1)

        self.dev_port = QLineEdit(self.gridLayoutWidget)
        self.dev_port.setObjectName(u"dev_port")
        self.dev_port.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.dev_port, 0, 5, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout.addWidget(self.label_24, 0, 6, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 0, 2, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 7, 1, 1)

        self.dev_port_2 = QLineEdit(self.gridLayoutWidget)
        self.dev_port_2.setObjectName(u"dev_port_2")
        self.dev_port_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.dev_port_2, 0, 8, 1, 1)

        self.config_save = QPushButton(BCT)
        self.config_save.setObjectName(u"config_save")
        self.config_save.setGeometry(QRect(660, 10, 141, 71))
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.config_save.sizePolicy().hasHeightForWidth())
        self.config_save.setSizePolicy(sizePolicy6)

        self.retranslateUi(BCT)

        self.tbMain.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(BCT)
    # setupUi

    def retranslateUi(self, BCT):
        BCT.setWindowTitle(QCoreApplication.translate("BCT", u"BCT", None))
        self.groupBox.setTitle(QCoreApplication.translate("BCT", u"Device 01", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("BCT", u"Current Battery Info", None))
        self.label_7.setText(QCoreApplication.translate("BCT", u"A", None))
        self.label_4.setText(QCoreApplication.translate("BCT", u"V", None))
        self.label_8.setText(QCoreApplication.translate("BCT", u"\u00b0C", None))
        self.dev_led_state.setText(QCoreApplication.translate("BCT", u"Battery State", None))
        self.label_6.setText(QCoreApplication.translate("BCT", u"\ubc18\ubcf5", None))
        self.label_5.setText(QCoreApplication.translate("BCT", u"\ubc84\uc804", None))
        ___qtablewidgetitem = self.dev_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("BCT", u"Pass", None));
        ___qtablewidgetitem1 = self.dev_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("BCT", u"No", None));
        ___qtablewidgetitem2 = self.dev_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("BCT", u"\uc804\uc555", None));
        ___qtablewidgetitem3 = self.dev_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("BCT", u"\uc804\ub958", None));
        ___qtablewidgetitem4 = self.dev_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("BCT", u"\uc628\ub3c4", None));
        ___qtablewidgetitem5 = self.dev_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("BCT", u"\uc624\ub958\ucf54\ub4dc", None));
        self.groupBox_4.setTitle(QCoreApplication.translate("BCT", u"Control", None))
        self.label_14.setText(QCoreApplication.translate("BCT", u"\ucda9\uc804 \uc911\uc9c0", None))
        self.config_time_on_h.setText(QCoreApplication.translate("BCT", u"0", None))
        self.label_43.setText(QCoreApplication.translate("BCT", u" \uc2dc", None))
        self.config_time_on_m.setText(QCoreApplication.translate("BCT", u"0", None))
        self.label_45.setText(QCoreApplication.translate("BCT", u" \ubd84", None))
        self.config_time_on_s.setText(QCoreApplication.translate("BCT", u"0", None))
        self.label_47.setText(QCoreApplication.translate("BCT", u" \ucd08", None))
        self.label_13.setText(QCoreApplication.translate("BCT", u"\ucda9\uc804 \uc720\uc9c0", None))
        self.config_time_off_h.setText(QCoreApplication.translate("BCT", u"0", None))
        self.label_44.setText(QCoreApplication.translate("BCT", u" \uc2dc", None))
        self.config_time_off_m.setText(QCoreApplication.translate("BCT", u"0", None))
        self.label_46.setText(QCoreApplication.translate("BCT", u" \ubd84", None))
        self.config_time_off_s.setText(QCoreApplication.translate("BCT", u"0", None))
        self.label_48.setText(QCoreApplication.translate("BCT", u" \ucd08", None))
        self.config_btn_start.setText(QCoreApplication.translate("BCT", u"start", None))
        self.config_btn_stop.setText(QCoreApplication.translate("BCT", u"stop", None))
        self.label_12.setText(QCoreApplication.translate("BCT", u"\ubc18\ubcf5\ud69f\uc218", None))
        self.config_cycle.setText(QCoreApplication.translate("BCT", u"0", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("BCT", u"Test Result", None))
        self.label_27.setText(QCoreApplication.translate("BCT", u"Dev02", None))
        self.label_25.setText(QCoreApplication.translate("BCT", u"Dev01", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("BCT", u"Device 01", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("BCT", u"Current Battery Info", None))
        self.label_9.setText(QCoreApplication.translate("BCT", u"A", None))
        self.label_10.setText(QCoreApplication.translate("BCT", u"V", None))
        self.label_11.setText(QCoreApplication.translate("BCT", u"\u00b0C", None))
        self.dev_led_state_2.setText(QCoreApplication.translate("BCT", u"Battery State", None))
        self.label_20.setText(QCoreApplication.translate("BCT", u"\ubc18\ubcf5", None))
        self.label_21.setText(QCoreApplication.translate("BCT", u"\ubc84\uc804", None))
        ___qtablewidgetitem6 = self.dev_table_2.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("BCT", u"Pass", None));
        ___qtablewidgetitem7 = self.dev_table_2.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("BCT", u"No", None));
        ___qtablewidgetitem8 = self.dev_table_2.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("BCT", u"\uc804\uc555", None));
        ___qtablewidgetitem9 = self.dev_table_2.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("BCT", u"\uc804\ub958", None));
        ___qtablewidgetitem10 = self.dev_table_2.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("BCT", u"\uc628\ub3c4", None));
        ___qtablewidgetitem11 = self.dev_table_2.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("BCT", u"\uc624\ub958\ucf54\ub4dc", None));
        self.tbMain.setTabText(self.tbMain.indexOf(self.tbBatteryCycle), QCoreApplication.translate("BCT", u"Battery Cycle", None))
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("BCT", u"Test Name", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("BCT", u"Dev1", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("BCT", u"Dev2", None));
        self.config_btn_start_2.setText(QCoreApplication.translate("BCT", u"start", None))
        self.tbMain.setTabText(self.tbMain.indexOf(self.tbBatteryFactory), QCoreApplication.translate("BCT", u"Factory Test", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("BCT", u"FW Version", None))
        self.label_15.setText(QCoreApplication.translate("BCT", u"Dev01", None))
        self.label_16.setText(QCoreApplication.translate("BCT", u"Dev02", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("BCT", u"Push Serial", None))
        self.label_18.setText(QCoreApplication.translate("BCT", u"\ubcc0\uacbd\uac12", None))
        self.label_19.setText(QCoreApplication.translate("BCT", u"Push", None))
        self.push_serial_autocnt.setText(QCoreApplication.translate("BCT", u"\ubcc0\uacbd\uac12 \uc99d\uac00", None))
        self.label_17.setText(QCoreApplication.translate("BCT", u"\uace0\uc815\uac12", None))
        self.push_serial_next.setText("")
        self.push_serial_mix.setText("")
        self.label_26.setText(QCoreApplication.translate("BCT", u"Next", None))
        self.push_serial_push.setText(QCoreApplication.translate("BCT", u"Push", None))
        self.tbMain.setTabText(self.tbMain.indexOf(self.tbSerial), QCoreApplication.translate("BCT", u"Push Serial", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("BCT", u"COM Connect", None))
        self.label.setText(QCoreApplication.translate("BCT", u"Port", None))
        self.label_2.setText(QCoreApplication.translate("BCT", u"Baud", None))
        self.label_24.setText(QCoreApplication.translate("BCT", u"Dev02", None))
        self.label_23.setText(QCoreApplication.translate("BCT", u"Dev01", None))
        self.label_3.setText(QCoreApplication.translate("BCT", u"Port", None))
        self.config_save.setText(QCoreApplication.translate("BCT", u"config save", None))
    # retranslateUi

