"""
Файл для повторения темы QTimer

Напомнить про работу с QTimer.

Предлагается создать приложение-которое будет
с некоторой периодичностью вызывать определённую функцию.
"""
import datetime
from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initTimer()
        self.initSignal()
        self.initlogging()


    def initUi(self) -> None:

        self.plainText = QtWidgets.QPlainTextEdit()
        self.spinBox = QtWidgets.QSpinBox()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.plainText)
        self.setLayout(layout)
        layout.addWidget(self.spinBox)

    def initTimer(self) -> None:
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
    def initSignal(self) -> None:
        self.timer.timeout.connect(self.initlogging)
        self.spinBox.valueChanged.connect(self.changeInterval)

    def changeInterval(self, value):
        self.timer.setInterval(value * 100 + 100)
    def initlogging(self) -> None:
        self.plainText.appendPlainText(str(datetime.datetime.now()))



    # def initUi(self):
    #     self.labelTime = QtWidgets.QLabel()
    #     self.labelTime.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    #
    #     layout = QtWidgets.QVBoxLayout()
    #     layout.addWidget(self.labelTime)
    #     layout.addWidget(QtWidgets.QPlainTextEdit())
    #
    #     self.setLayout(layout)
    #     self.showTime()
    # def initTimer(self) -> None:
    #     self.timeTimer = QtCore.QTimer()
    #     self.timeTimer.setInterval(1000)
    #     self.timeTimer.start()
    #
    # def initSignal(self) -> None:
    #     self.timeTimer.timeout.connect(self.showTime)
    #
    # def showTime(self) -> None:
    #     time = QtCore.QDateTime.currentDateTime()
    #     timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
    #     self.labelTime.setText(timeDisplay)



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
