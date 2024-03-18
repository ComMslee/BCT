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
    QLabel, QSizePolicy, QTabWidget, QTextEdit,
    QWidget)

class Ui_BCT(object):
    def setupUi(self, BCT):
        if not BCT.objectName():
            BCT.setObjectName(u"BCT")
        BCT.resize(645, 533)
        self.tbMain = QTabWidget(BCT)
        self.tbMain.setObjectName(u"tbMain")
        self.tbMain.setGeometry(QRect(0, 0, 641, 531))
        self.tbControl = QWidget()
        self.tbControl.setObjectName(u"tbControl")
        self.groupBox = QGroupBox(self.tbControl)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 291, 501))
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 20, 271, 91))
        self.gridLayoutWidget = QWidget(self.groupBox_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 251, 61))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.textEdit = QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)

        self.textEdit_2 = QTextEdit(self.gridLayoutWidget)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.gridLayout.addWidget(self.textEdit_2, 1, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 210, 271, 171))
        self.gridLayoutWidget_2 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 70, 251, 80))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dv01_Volt_ = QLabel(self.gridLayoutWidget_2)
        self.dv01_Volt_.setObjectName(u"dv01_Volt_")
        self.dv01_Volt_.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.dv01_Volt_, 0, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)

        self.dv01_Ampere = QLabel(self.gridLayoutWidget_2)
        self.dv01_Ampere.setObjectName(u"dv01_Ampere")
        self.dv01_Ampere.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.dv01_Ampere, 1, 0, 1, 1)

        self.dv01_Temp = QLabel(self.gridLayoutWidget_2)
        self.dv01_Temp.setObjectName(u"dv01_Temp")
        self.dv01_Temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.dv01_Temp, 2, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 2, 1, 1, 1)

        self.horizontalLayoutWidget = QWidget(self.groupBox_3)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 251, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.tbMain.addTab(self.tbControl, "")
        self.tbSerial = QWidget()
        self.tbSerial.setObjectName(u"tbSerial")
        self.tbMain.addTab(self.tbSerial, "")
        self.tbSetting = QWidget()
        self.tbSetting.setObjectName(u"tbSetting")
        self.tbMain.addTab(self.tbSetting, "")

        self.retranslateUi(BCT)

        self.tbMain.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(BCT)
    # setupUi

    def retranslateUi(self, BCT):
        BCT.setWindowTitle(QCoreApplication.translate("BCT", u"BCT", None))
        self.groupBox.setTitle(QCoreApplication.translate("BCT", u"Device 01", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("BCT", u"COM", None))
        self.label.setText(QCoreApplication.translate("BCT", u"Port", None))
        self.label_2.setText(QCoreApplication.translate("BCT", u"Baud", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("BCT", u"Battery Info", None))
        self.dv01_Volt_.setText(QCoreApplication.translate("BCT", u"-", None))
        self.label_4.setText(QCoreApplication.translate("BCT", u"V", None))
        self.dv01_Ampere.setText(QCoreApplication.translate("BCT", u"-", None))
        self.dv01_Temp.setText(QCoreApplication.translate("BCT", u"-", None))
        self.label_7.setText(QCoreApplication.translate("BCT", u"A", None))
        self.label_8.setText(QCoreApplication.translate("BCT", u"\u00b0C", None))
        self.label_5.setText(QCoreApplication.translate("BCT", u"FW Version", None))
        self.label_3.setText(QCoreApplication.translate("BCT", u"-", None))
        self.tbMain.setTabText(self.tbMain.indexOf(self.tbControl), QCoreApplication.translate("BCT", u"Battery Test", None))
        self.tbMain.setTabText(self.tbMain.indexOf(self.tbSerial), QCoreApplication.translate("BCT", u"Input Serial", None))
        self.tbMain.setTabText(self.tbMain.indexOf(self.tbSetting), QCoreApplication.translate("BCT", u"Setting", None))
    # retranslateUi

