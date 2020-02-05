import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit,\
    QLabel, QGridLayout, QLineEdit, QMessageBox

from PyQt5.QtCore import Qt, pyqtSignal

class ControlPanel(QWidget):
    def __init__(self):
        super().__init__()
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

        self.btnZero.clicked.connect(lambda: print("Zero clicked"))

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

        self.txtMonitor.insertPlainText(">>ПРИВЕТ\n")
        self.txtMonitor.insertPlainText(">>Добро пожаловать")

        self.setLayout(self.gridL)
        self.setWindowTitle("ТЕСТ")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ControlPanel()
    sys.exit(app.exec_())
