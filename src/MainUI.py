# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BCT_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
        BCT.resize(743, 556)
        self.tbMain = QTabWidget(BCT)
        self.tbMain.setObjectName(u"tbMain")
        self.tbMain.setGeometry(QRect(0, 60, 741, 491))
        self.tbBatteryTest = QWidget()
        self.tbBatteryTest.setObjectName(u"tbBatteryTest")
        self.groupBox = QGroupBox(self.tbBatteryTest)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 80, 731, 191))
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 20, 151, 161))
        self.gridLayoutWidget_2 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 70, 131, 80))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dev_ampere = QLineEdit(self.gridLayoutWidget_2)
        self.dev_ampere.setObjectName(u"dev_ampere")
        self.dev_ampere.setAlignment(Qt.AlignCenter)
        self.dev_ampere.setReadOnly(True)

        self.gridLayout_2.addWidget(self.dev_ampere, 1, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 2, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 1, 1, 1)

        self.dev_volt = QLineEdit(self.gridLayoutWidget_2)
        self.dev_volt.setObjectName(u"dev_volt")
        self.dev_volt.setAlignment(Qt.AlignCenter)
        self.dev_volt.setReadOnly(True)

        self.gridLayout_2.addWidget(self.dev_volt, 0, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)

        self.dev_temperature = QLineEdit(self.gridLayoutWidget_2)
        self.dev_temperature.setObjectName(u"dev_temperature")
        self.dev_temperature.setAlignment(Qt.AlignCenter)
        self.dev_temperature.setReadOnly(True)

        self.gridLayout_2.addWidget(self.dev_temperature, 2, 0, 1, 1)

        self.gridLayoutWidget_3 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 20, 131, 51))
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
        if (self.dev_table.columnCount() < 5):
            self.dev_table.setColumnCount(5)
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
        self.dev_table.setObjectName(u"dev_table")
        self.dev_table.setGeometry(QRect(170, 20, 551, 161))
        self.groupBox_4 = QGroupBox(self.tbBatteryTest)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 0, 731, 81))
        self.gridLayoutWidget_4 = QWidget(self.groupBox_4)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 20, 351, 56))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.gridLayoutWidget_4)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 0, 4, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.config_time_off_h = QLineEdit(self.gridLayoutWidget_4)
        self.config_time_off_h.setObjectName(u"config_time_off_h")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(60)
        sizePolicy1.setVerticalStretch(0)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(60)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.config_time_off_s.sizePolicy().hasHeightForWidth())
        self.config_time_off_s.setSizePolicy(sizePolicy2)
        self.config_time_off_s.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.config_time_off_s)

        self.label_48 = QLabel(self.gridLayoutWidget_4)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_4.addWidget(self.label_48)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 1, 5, 1, 1)

        self.config_cycle = QLineEdit(self.gridLayoutWidget_4)
        self.config_cycle.setObjectName(u"config_cycle")
        self.config_cycle.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.config_cycle, 0, 3, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.config_time_on_h = QLineEdit(self.gridLayoutWidget_4)
        self.config_time_on_h.setObjectName(u"config_time_on_h")
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
        sizePolicy2.setHeightForWidth(self.config_time_on_s.sizePolicy().hasHeightForWidth())
        self.config_time_on_s.setSizePolicy(sizePolicy2)
        self.config_time_on_s.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.config_time_on_s)

        self.label_47 = QLabel(self.gridLayoutWidget_4)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_3.addWidget(self.label_47)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 0, 5, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_4)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 1, 4, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_4)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 0, 2, 1, 1)

        self.verticalLayoutWidget = QWidget(self.groupBox_4)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(540, 20, 181, 56))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.pushButton)

        self.groupBox_7 = QGroupBox(self.tbBatteryTest)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(0, 270, 731, 191))
        self.groupBox_8 = QGroupBox(self.groupBox_7)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(10, 20, 151, 161))
        self.gridLayoutWidget_7 = QWidget(self.groupBox_8)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(10, 70, 131, 80))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.dev_ampere_2 = QLineEdit(self.gridLayoutWidget_7)
        self.dev_ampere_2.setObjectName(u"dev_ampere_2")
        self.dev_ampere_2.setAlignment(Qt.AlignCenter)
        self.dev_ampere_2.setReadOnly(True)

        self.gridLayout_7.addWidget(self.dev_ampere_2, 1, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_7)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_7.addWidget(self.label_9, 2, 1, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_7)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_7.addWidget(self.label_10, 1, 1, 1, 1)

        self.dev_volt_2 = QLineEdit(self.gridLayoutWidget_7)
        self.dev_volt_2.setObjectName(u"dev_volt_2")
        self.dev_volt_2.setAlignment(Qt.AlignCenter)
        self.dev_volt_2.setReadOnly(True)

        self.gridLayout_7.addWidget(self.dev_volt_2, 0, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_7)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.label_11, 0, 1, 1, 1)

        self.dev_temperature_2 = QLineEdit(self.gridLayoutWidget_7)
        self.dev_temperature_2.setObjectName(u"dev_temperature_2")
        self.dev_temperature_2.setAlignment(Qt.AlignCenter)
        self.dev_temperature_2.setReadOnly(True)

        self.gridLayout_7.addWidget(self.dev_temperature_2, 2, 0, 1, 1)

        self.gridLayoutWidget_8 = QWidget(self.groupBox_8)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(10, 20, 131, 52))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.dev_cycle_2 = QLineEdit(self.gridLayoutWidget_8)
        self.dev_cycle_2.setObjectName(u"dev_cycle_2")
        self.dev_cycle_2.setAlignment(Qt.AlignCenter)
        self.dev_cycle_2.setReadOnly(True)

        self.gridLayout_8.addWidget(self.dev_cycle_2, 1, 1, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget_8)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_8.addWidget(self.label_21, 1, 0, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget_8)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_8.addWidget(self.label_22, 0, 0, 1, 1)

        self.dev_version_2 = QLineEdit(self.gridLayoutWidget_8)
        self.dev_version_2.setObjectName(u"dev_version_2")
        self.dev_version_2.setAlignment(Qt.AlignCenter)
        self.dev_version_2.setReadOnly(True)

        self.gridLayout_8.addWidget(self.dev_version_2, 0, 1, 1, 1)

        self.dev_table_2 = QTableWidget(self.groupBox_7)
        if (self.dev_table_2.columnCount() < 5):
            self.dev_table_2.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.dev_table_2.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.dev_table_2.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.dev_table_2.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.dev_table_2.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.dev_table_2.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.dev_table_2.setObjectName(u"dev_table_2")
        self.dev_table_2.setGeometry(QRect(170, 20, 551, 161))
        self.tbMain.addTab(self.tbBatteryTest, "")
        self.tbSerial = QWidget()
        self.tbSerial.setObjectName(u"tbSerial")
        self.groupBox_5 = QGroupBox(self.tbSerial)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 10, 391, 91))
        self.gridLayoutWidget_5 = QWidget(self.groupBox_5)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 20, 371, 57))
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
        self.groupBox_6.setGeometry(QRect(10, 100, 391, 131))
        self.gridLayoutWidget_6 = QWidget(self.groupBox_6)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(10, 20, 371, 102))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.push_serial_val = QLineEdit(self.gridLayoutWidget_6)
        self.push_serial_val.setObjectName(u"push_serial_val")

        self.gridLayout_6.addWidget(self.push_serial_val, 1, 1, 1, 1)

        self.push_serial_fixed = QLineEdit(self.gridLayoutWidget_6)
        self.push_serial_fixed.setObjectName(u"push_serial_fixed")

        self.gridLayout_6.addWidget(self.push_serial_fixed, 0, 1, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget_6)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_6.addWidget(self.label_18, 1, 0, 1, 1)

        self.push_serial_autocnt = QCheckBox(self.gridLayoutWidget_6)
        self.push_serial_autocnt.setObjectName(u"push_serial_autocnt")

        self.gridLayout_6.addWidget(self.push_serial_autocnt, 0, 2, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget_6)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_6.addWidget(self.label_19, 3, 0, 1, 1)

        self.push_serial_mix = QLineEdit(self.gridLayoutWidget_6)
        self.push_serial_mix.setObjectName(u"push_serial_mix")
        self.push_serial_mix.setReadOnly(True)

        self.gridLayout_6.addWidget(self.push_serial_mix, 3, 1, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget_6)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_6.addWidget(self.label_17, 0, 0, 1, 1)

        self.push_serial_push = QPushButton(self.gridLayoutWidget_6)
        self.push_serial_push.setObjectName(u"push_serial_push")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.push_serial_push.sizePolicy().hasHeightForWidth())
        self.push_serial_push.setSizePolicy(sizePolicy4)

        self.gridLayout_6.addWidget(self.push_serial_push, 1, 2, 3, 1)

        self.label_20 = QLabel(self.gridLayoutWidget_6)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_6.addWidget(self.label_20, 2, 0, 1, 2)

        self.tbMain.addTab(self.tbSerial, "")
        self.groupBox_2 = QGroupBox(BCT)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 0, 611, 61))
        self.gridLayoutWidget = QWidget(self.groupBox_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 591, 31))
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
        self.config_save.setGeometry(QRect(624, 9, 111, 51))
        sizePolicy3.setHeightForWidth(self.config_save.sizePolicy().hasHeightForWidth())
        self.config_save.setSizePolicy(sizePolicy3)

        self.retranslateUi(BCT)

        self.tbMain.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(BCT)
    # setupUi

    def retranslateUi(self, BCT):
        BCT.setWindowTitle(QCoreApplication.translate("BCT", u"BCT", None))
        self.groupBox.setTitle(QCoreApplication.translate("BCT", u"Device 01", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("BCT", u"Battery Test Info", None))
        self.label_8.setText(QCoreApplication.translate("BCT", u"\u00b0C", None))
        self.label_7.setText(QCoreApplication.translate("BCT", u"A", None))
        self.label_4.setText(QCoreApplication.translate("BCT", u"V", None))
        self.label_6.setText(QCoreApplication.translate("BCT", u"Cycle", None))
        self.label_5.setText(QCoreApplication.translate("BCT", u"Version", None))
        ___qtablewidgetitem = self.dev_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("BCT", u"no", None));
        ___qtablewidgetitem1 = self.dev_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("BCT", u"\uc804\uc555", None));
        ___qtablewidgetitem2 = self.dev_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("BCT", u"\uc804\ub958", None));
        ___qtablewidgetitem3 = self.dev_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("BCT", u"\uc628\ub3c4", None));
        ___qtablewidgetitem4 = self.dev_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("BCT", u"\uc624\ub958\ucf54\ub4dc", None));
        self.groupBox_4.setTitle(QCoreApplication.translate("BCT", u"Control", None))
        self.label_13.setText(QCoreApplication.translate("BCT", u"\ucda9\uc804 \uc720\uc9c0", None))
        self.config_time_off_h.setText(QCoreApplication.translate("BCT", u"0", None))
        self.label_44.setText(QCoreApplication.translate("BCT", u" \uc2dc", None))
        self.config_time_off_m.setText(QCoreApplication.translate("BCT", u"0", None))
        self.label_46.setText(QCoreApplication.translate("BCT", u" \ubd84", None))
        self.config_time_off_s.setText(QCoreApplication.translate("BCT", u"0", None))
        self.label_48.setText(QCoreApplication.translate("BCT", u" \ucd08", None))
        self.config_cycle.setText(QCoreApplication.translate("BCT", u"0", None))
        self.config_time_on_h.setText(QCoreApplication.translate("BCT", u"0", None))
        self.label_43.setText(QCoreApplication.translate("BCT", u" \uc2dc", None))
        self.config_time_on_m.setText(QCoreApplication.translate("BCT", u"0", None))
        self.label_45.setText(QCoreApplication.translate("BCT", u" \ubd84", None))
        self.config_time_on_s.setText(QCoreApplication.translate("BCT", u"0", None))
        self.label_47.setText(QCoreApplication.translate("BCT", u" \ucd08", None))
        self.label_14.setText(QCoreApplication.translate("BCT", u"\ucda9\uc804 \uc911\uc9c0", None))
        self.label_12.setText(QCoreApplication.translate("BCT", u"\ubc18\ubcf5\ud69f\uc218", None))
        self.pushButton_2.setText(QCoreApplication.translate("BCT", u"start", None))
        self.pushButton.setText(QCoreApplication.translate("BCT", u"stop", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("BCT", u"Device 01", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("BCT", u"Battery Test Info", None))
        self.label_9.setText(QCoreApplication.translate("BCT", u"\u00b0C", None))
        self.label_10.setText(QCoreApplication.translate("BCT", u"A", None))
        self.label_11.setText(QCoreApplication.translate("BCT", u"V", None))
        self.label_21.setText(QCoreApplication.translate("BCT", u"Cycle", None))
        self.label_22.setText(QCoreApplication.translate("BCT", u"Version", None))
        ___qtablewidgetitem5 = self.dev_table_2.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("BCT", u"no", None));
        ___qtablewidgetitem6 = self.dev_table_2.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("BCT", u"\uc804\uc555", None));
        ___qtablewidgetitem7 = self.dev_table_2.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("BCT", u"\uc804\ub958", None));
        ___qtablewidgetitem8 = self.dev_table_2.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("BCT", u"\uc628\ub3c4", None));
        ___qtablewidgetitem9 = self.dev_table_2.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("BCT", u"\uc624\ub958\ucf54\ub4dc", None));
        self.tbMain.setTabText(self.tbMain.indexOf(self.tbBatteryTest), QCoreApplication.translate("BCT", u"Battery Test", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("BCT", u"FW Version", None))
        self.label_15.setText(QCoreApplication.translate("BCT", u"Dev01", None))
        self.label_16.setText(QCoreApplication.translate("BCT", u"Dev 02", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("BCT", u"Push Serial", None))
        self.label_18.setText(QCoreApplication.translate("BCT", u"\ubcc0\uacbd\uac12", None))
        self.push_serial_autocnt.setText(QCoreApplication.translate("BCT", u"\ubcc0\uacbd\uac12 \uc99d\uac00", None))
        self.label_19.setText(QCoreApplication.translate("BCT", u"SerialNumber", None))
        self.push_serial_mix.setText("")
        self.label_17.setText(QCoreApplication.translate("BCT", u"\uace0\uc815\uac12", None))
        self.push_serial_push.setText(QCoreApplication.translate("BCT", u"Push", None))
        self.label_20.setText("")
        self.tbMain.setTabText(self.tbMain.indexOf(self.tbSerial), QCoreApplication.translate("BCT", u"Push Serial", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("BCT", u"COM Connect", None))
        self.label.setText(QCoreApplication.translate("BCT", u"Port", None))
        self.label_2.setText(QCoreApplication.translate("BCT", u"Baud", None))
        self.label_24.setText(QCoreApplication.translate("BCT", u"Dev02", None))
        self.label_23.setText(QCoreApplication.translate("BCT", u"Dev01", None))
        self.label_3.setText(QCoreApplication.translate("BCT", u"Port", None))
        self.config_save.setText(QCoreApplication.translate("BCT", u"config save", None))
    # retranslateUi

