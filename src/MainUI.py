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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_BCT(object):
    def setupUi(self, BCT):
        if not BCT.objectName():
            BCT.setObjectName(u"BCT")
        BCT.resize(734, 617)
        self.tbMain = QTabWidget(BCT)
        self.tbMain.setObjectName(u"tbMain")
        self.tbMain.setGeometry(QRect(0, 0, 731, 611))
        self.tbControl = QWidget()
        self.tbControl.setObjectName(u"tbControl")
        self.groupBox = QGroupBox(self.tbControl)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 80, 711, 251))
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 20, 201, 61))
        self.gridLayoutWidget = QWidget(self.groupBox_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 181, 31))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 80, 201, 161))
        self.gridLayoutWidget_2 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 60, 71, 80))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_17 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_17, 1, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 2, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 1, 1, 1)

        self.lineEdit_16 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_16, 0, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)

        self.lineEdit_18 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_18, 2, 0, 1, 1)

        self.horizontalLayoutWidget = QWidget(self.groupBox_3)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 181, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.lineEdit_21 = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_21)

        self.gridLayoutWidget_3 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(90, 60, 101, 52))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.gridLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.lineEdit_20 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_20, 0, 1, 1, 1)

        self.lineEdit_19 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_19, 1, 1, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)

        self.listWidget = QListWidget(self.groupBox)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(220, 20, 481, 221))
        self.groupBox_4 = QGroupBox(self.tbControl)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 0, 711, 81))
        self.gridLayoutWidget_4 = QWidget(self.groupBox_4)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 20, 461, 56))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.gridLayoutWidget_4)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 0, 4, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_14 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(60)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_14.sizePolicy().hasHeightForWidth())
        self.lineEdit_14.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.lineEdit_14)

        self.label_44 = QLabel(self.gridLayoutWidget_4)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_4.addWidget(self.label_44)

        self.lineEdit_15 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        sizePolicy1.setHeightForWidth(self.lineEdit_15.sizePolicy().hasHeightForWidth())
        self.lineEdit_15.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.lineEdit_15)

        self.label_46 = QLabel(self.gridLayoutWidget_4)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_4.addWidget(self.label_46)

        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(60)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.lineEdit_5)

        self.label_48 = QLabel(self.gridLayoutWidget_4)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_4.addWidget(self.label_48)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 1, 5, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_4.addWidget(self.lineEdit_3, 0, 3, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_13 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        sizePolicy1.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.lineEdit_13)

        self.label_43 = QLabel(self.gridLayoutWidget_4)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_3.addWidget(self.label_43)

        self.lineEdit_12 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        sizePolicy1.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.lineEdit_12)

        self.label_45 = QLabel(self.gridLayoutWidget_4)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_3.addWidget(self.label_45)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy2.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.lineEdit_4)

        self.label_47 = QLabel(self.gridLayoutWidget_4)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_3.addWidget(self.label_47)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 0, 5, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_4)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 1, 4, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_4.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_4)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 0, 2, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.verticalLayoutWidget = QWidget(self.groupBox_4)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(590, 20, 111, 51))
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

        self.tbMain.addTab(self.tbControl, "")
        self.tbSerial = QWidget()
        self.tbSerial.setObjectName(u"tbSerial")
        self.gridLayoutWidget_5 = QWidget(self.tbSerial)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 20, 621, 57))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_22 = QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineEdit_22, 0, 2, 1, 1)

        self.lineEdit_11 = QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_5.addWidget(self.lineEdit_11, 0, 3, 2, 1)

        self.label_21 = QLabel(self.gridLayoutWidget_5)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_5.addWidget(self.label_21, 1, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget_5)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_5.addWidget(self.pushButton_5, 0, 4, 2, 1)

        self.label_17 = QLabel(self.gridLayoutWidget_5)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 0, 1, 1, 1)

        self.lineEdit_23 = QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineEdit_23, 1, 2, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_5)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_5)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_5.addWidget(self.label_16, 1, 0, 1, 1)

        self.tbMain.addTab(self.tbSerial, "")

        self.retranslateUi(BCT)

        self.tbMain.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(BCT)
    # setupUi

    def retranslateUi(self, BCT):
        BCT.setWindowTitle(QCoreApplication.translate("BCT", u"BCT", None))
        self.groupBox.setTitle(QCoreApplication.translate("BCT", u"Device 01", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("BCT", u"COM Connect", None))
        self.label.setText(QCoreApplication.translate("BCT", u"Port", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("BCT", u"Battery Test Info", None))
        self.label_8.setText(QCoreApplication.translate("BCT", u"\u00b0C", None))
        self.label_7.setText(QCoreApplication.translate("BCT", u"A", None))
        self.label_4.setText(QCoreApplication.translate("BCT", u"V", None))
        self.label_5.setText(QCoreApplication.translate("BCT", u"Version", None))
        self.label_6.setText(QCoreApplication.translate("BCT", u"Cycle", None))
        self.label_10.setText(QCoreApplication.translate("BCT", u"Fail Cnt", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("BCT", u"Control", None))
        self.label_13.setText(QCoreApplication.translate("BCT", u"\ucda9\uc804 \uc720\uc9c0 \uc2dc\uac04", None))
        self.lineEdit_14.setText(QCoreApplication.translate("BCT", u"0", None))
        self.label_44.setText(QCoreApplication.translate("BCT", u" \uc2dc", None))
        self.lineEdit_15.setText(QCoreApplication.translate("BCT", u"0", None))
        self.label_46.setText(QCoreApplication.translate("BCT", u" \ubd84", None))
        self.lineEdit_5.setText(QCoreApplication.translate("BCT", u"0", None))
        self.label_48.setText(QCoreApplication.translate("BCT", u" \ucd08", None))
        self.lineEdit_3.setText(QCoreApplication.translate("BCT", u"0", None))
        self.lineEdit_13.setText(QCoreApplication.translate("BCT", u"0", None))
        self.label_43.setText(QCoreApplication.translate("BCT", u" \uc2dc", None))
        self.lineEdit_12.setText(QCoreApplication.translate("BCT", u"0", None))
        self.label_45.setText(QCoreApplication.translate("BCT", u" \ubd84", None))
        self.lineEdit_4.setText(QCoreApplication.translate("BCT", u"0", None))
        self.label_47.setText(QCoreApplication.translate("BCT", u" \ucd08", None))
        self.label_14.setText(QCoreApplication.translate("BCT", u"\ucda9\uc804 \uc911\uc9c0 \uc2dc\uac04", None))
        self.label_12.setText(QCoreApplication.translate("BCT", u"\ubc18\ubcf5\ud69f\uc218", None))
        self.label_2.setText(QCoreApplication.translate("BCT", u"Baud", None))
        self.pushButton_2.setText(QCoreApplication.translate("BCT", u"start", None))
        self.pushButton.setText(QCoreApplication.translate("BCT", u"stop", None))
        self.tbMain.setTabText(self.tbMain.indexOf(self.tbControl), QCoreApplication.translate("BCT", u"Battery Test", None))
        self.label_21.setText(QCoreApplication.translate("BCT", u"FW Version", None))
        self.pushButton_5.setText(QCoreApplication.translate("BCT", u"PushButton", None))
        self.label_17.setText(QCoreApplication.translate("BCT", u"FW Version", None))
        self.label_15.setText(QCoreApplication.translate("BCT", u"Device 01", None))
        self.label_16.setText(QCoreApplication.translate("BCT", u"Device 02", None))
        self.tbMain.setTabText(self.tbMain.indexOf(self.tbSerial), QCoreApplication.translate("BCT", u"Push Serial", None))
    # retranslateUi

