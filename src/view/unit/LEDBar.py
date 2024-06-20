from PySide6.QtCore import QTimer
from PySide6.QtGui import QColor, QPainter, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy

from src.MainUI import Ui_BCT


class MakeBar(QWidget):
    def __init__(self, mainWindow: Ui_BCT):
        super().__init__()
        self.timer = None
        self.led_bars = []

        self.initUI(mainWindow)

    def initUI(self, mainWindow: Ui_BCT):
        # label_33에 레이아웃을 추가합니다.
        self.ly = QVBoxLayout(mainWindow.label_33)

        colors = [
            '#FE2E2E',
            '#FE9A2E',
            '#58FAAC',
            '#FACC2E',
            '#FF0000',
            '#58FAD0',
            '#045FB4',
            '#BF00FF',
            '#0101DF',
            '#4B89DC'
        ]

        for color in colors:
            led_bar = LedBar(color)
            self.ly.addWidget(led_bar)  # 레이아웃에 LED 바를 추가합니다.
            self.led_bars.append(led_bar)

        self.startRamp()

    def startRamp(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_led_bars)
        self.timer.start(500)  # 500ms 간격으로 타이머 작동

    def update_led_bars(self):
        for i, led_bar in enumerate(self.led_bars):
            led_bar.blink()


class LedBar(QWidget):
    MyColor = None

    def __init__(self, color, width=100, height=100, parent=None):
        super().__init__(parent)
        self.color = QColor(color)
        self.MyColor = self.color
        self.width = width
        self.height = height
        self.setMinimumSize(self.width, self.height)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 크기 정책 설정

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(self.color)
        painter.setPen(Qt.NoPen)
        painter.drawRect(0, 0, self.width, self.height)

    def blink(self):
        if self.color == QColor("white"):
            self.color = self.MyColor
        else:
            self.color = QColor("white")

        self.update()
