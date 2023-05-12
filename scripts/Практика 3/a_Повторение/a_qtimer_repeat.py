"""
Файл для повторения темы QTimer

Напомнить про работу с QTimer.

Предлагается создать приложение-которое будет
с некоторой периодичностью вызывать определённую функцию.
"""

import random

import requests
from PySide6 import QtWidgets, QtGui, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initTimers()
        self.initSignals()

    def initUi(self) -> None:
        """

        :return:
        """

        self.setMinimumSize(640, 480)

        self.lineEditURL = QtWidgets.QLineEdit()
        self.lineEditURL.setReadOnly(True)

        self.labelImage = QtWidgets.QLabel("Получение изображения...")
        self.labelImage.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelImage.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding
        )
        pixmap = QtGui.QPixmap(r"E:\DEV\Python\Projects\POLY_DevPyQt2022\scripts\Лекция 5\a_QResources\ui\img\2.jpg")
        self.labelImage.setPixmap(pixmap)

        labelDelay = QtWidgets.QLabel("Время обновления: ")

        self.spinBox = QtWidgets.QSpinBox()
        self.spinBox.setMinimum(2)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lineEditURL)
        layout.addWidget(self.labelImage)
        layout.addWidget(labelDelay)
        layout.addWidget(self.spinBox)

        self.setLayout(layout)

    def initTimers(self) -> None:
        """

        :return:
        """

        self.timer = QtCore.QTimer()
        self.timer.setInterval(2000)
        self.timer.start()

    def initSignals(self) -> None:
        """

        :return:
        """

        self.timer.timeout.connect(self.getImage)
        self.spinBox.valueChanged.connect(lambda x: self.timer.setInterval(x * 1000))

    def getImage(self) -> None:
        response = requests.get("https://api.imgflip.com/get_memes")
        data = response.json()['data']['memes']

        if response.status_code != 200:
            self.labelImage.setText("Получение изображения...")
            self.lineEditURL.clear()
            return

        random_image_url = random.choice(data)["url"]
        self.lineEditURL.setText(random_image_url)
        image = requests.get(random_image_url).content
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image)

        self.labelImage.setPixmap(pixmap.scaledToWidth(500))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
