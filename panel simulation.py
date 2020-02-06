import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit,\
    QLabel, QGridLayout, QLineEdit, QMessageBox

from PyQt5.QtCore import Qt, pyqtSignal
import math


class ControlPanel(QWidget):
    def __init__(self):
        super().__init__()

        try:
            with open("style.css", "r") as fh:
                self.setStyleSheet(fh.read())

        except:
            pass

        self.rolDiaMM = 50
        self.impsPerRound = 1000

        self.currentStep = 1

        self.currentPosition = 0
        self.movement = 0
        self.toolsPositionDict = {"drill": 825,
                                  "saw": 775,
                                  "cutterLeft": 360,
                                  "robot": 285,
                                  "cutterRight": 210,
                                  "outConv": -150}
        self.prevPosition = 0
        self.init_gui()

    def init_gui(self):
        self.txtLength = QLineEdit("Введите число")

        self.btnZero = QPushButton("ПОИСК НУЛЯ")
        self.btnDrill = QPushButton("СВЕРЛО")
        self.btnSaw = QPushButton("ПИЛА")
        self.btnCutterLeft = QPushButton("ФРЕЗА ЛЕВАЯ")
        self.btnRobot = QPushButton("РОБОТ")
        self.btnCutterRight = QPushButton("ФРЕЗА ПРАВАЯ")
        self.btnRemove = QPushButton("УБРАТЬ БАЛКУ")

        self.btnZero.clicked.connect(self.btnZero_clicked)
        self.btnDrill.clicked.connect(self.btnDrill_clicked)
        self.btnSaw.clicked.connect(self.btnSaw_clicked)
        self.btnCutterLeft.clicked.connect(self.btnCutterLeft_clicked)
        self.btnRobot.clicked.connect(self.btnRobot_clicked)
        self.btnCutterRight.clicked.connect(self.btnCutterRight_clicked)
        self.btnRemove.clicked.connect(self.btnRemove_clicked)

        self.txtMonitor = QTextEdit()

        self.gridL = QGridLayout()
        self.gridL.addWidget(QLabel("Позиция"), 0, 0, 1, 1, Qt.AlignCenter)
        self.gridL.addWidget(self.txtLength, 0, 1, 1, 1, Qt.AlignCenter)
        self.gridL.addWidget(self.btnZero, 0, 2, 1, 1, Qt.AlignCenter)
        self.gridL.addWidget(self.btnDrill, 1, 2, 1, 1, Qt.AlignCenter)
        self.gridL.addWidget(self.btnSaw, 2, 2, 1, 1, Qt.AlignCenter)
        self.gridL.addWidget(self.btnCutterLeft, 3, 2, 1, 1, Qt.AlignCenter)
        self.gridL.addWidget(self.btnRobot, 4, 2, 1, 1, Qt.AlignCenter)
        self.gridL.addWidget(self.btnCutterRight, 5, 2, 1, 1, Qt.AlignCenter)
        self.gridL.addWidget(self.btnRemove, 6, 2, 1, 1, Qt.AlignCenter)
        self.gridL.addWidget(self.txtMonitor, 1, 0, 7, 2)

        self.setLayout(self.gridL)
        self.setWindowTitle("ТЕСТ")
        self.show()

    def btnZero_clicked(self):
        self.currentPosition = 0;
        self.print_line("%d Поиск нулевого положения. Текущая позиция: 0" % self.currentStep)
        self.currentStep += 1

    def btnDrill_clicked(self):
        self.calculate_position("Сверло", self.toolsPositionDict["drill"])

    def btnSaw_clicked(self):
        self.calculate_position("Пила", self.toolsPositionDict["saw"])

    def btnCutterLeft_clicked(self):
        self.calculate_position("Фреза слева", self.toolsPositionDict["cutterLeft"])

    def btnRobot_clicked(self):
        self.calculate_position("Робот", self.toolsPositionDict["robot"])

    def btnCutterRight_clicked(self):
        self.calculate_position("Фреза справа", self.toolsPositionDict["cutterRight"])

    def btnRemove_clicked(self):
        self.movement = self.calculate_movement(0, self.toolsPositionDict["outConv"])
        imps = self.length_to_imp(self.movement)
        realPosition = self.prevPosition + self.imps_to_length(imps)
        self.print_line("%d %s <Перемещение> %.3f мм [%d имп]" %
                        (self.currentStep, "Убрали с конвеера", self.movement, imps))
        self.currentPosition = realPosition
        self.currentStep += 1

    def calculate_position(self, msg, tool):
        pos = self.get_position()
        if pos < 0:
            self.print_line("Введите корректное расстояние")
        else:
            self.movement = self.calculate_movement(pos, tool)
            imps = self.length_to_imp(self.movement)
            realPosition = self.prevPosition + self.imps_to_length(imps)
            self.print_line("%d %s <Положение> расчетное: %.3f, реальное: %.3f <Перемещение> %.3f мм [%d имп]" %
                            (self.currentStep, msg, self.currentPosition, realPosition, self.movement, imps))
            self.currentPosition = realPosition
            self.currentStep += 1

    def imps_to_length(self, imps):
        c = self.rolDiaMM * math.pi
        movement = round(imps / self.impsPerRound * c, 3)
        return movement

    def length_to_imp(self, movement):
        c = self.rolDiaMM * math.pi
        imps = round(movement / c * self.impsPerRound)
        return imps

    def calculate_movement(self, nessPos, toolPos):
        nextPos = nessPos + toolPos
        movement = nextPos- self.currentPosition
        self.prevPosition = self.currentPosition
        self.currentPosition = nextPos
        return movement

    def get_position(self):
        s = self.txtLength.text()
        try:
            pos = int(s)
        except:
            pos = -1
        return pos

    def print_line(self, s):
        self.txtMonitor.insertPlainText(">> " + s + "\n")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ControlPanel()
    sys.exit(app.exec_())
