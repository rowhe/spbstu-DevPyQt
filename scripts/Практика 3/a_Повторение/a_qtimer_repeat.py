"""
Файл для повторения темы QThread

Напомнить про работу с QThread.

Предлагается создать небольшое приложение, которое будет с помощью модуля request
получать доступность того или иного сайта (возвращать из потока status_code сайта).

Поработать с сигналами, которые возникают при запуске/остановке потока,
передать данные в поток (в данном случае url + время обновления(таймаута)),
получить данные из потока (статус код сайта),
попробовать управлять потоком (запуск, остановка).

Опционально поработать с валидацией url
"""
import time

from PySide6 import QtWidgets, QtCore
import requests


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

        self.initThread()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.lineEditUrl = QtWidgets.QLineEdit()
        self.lineEditUrl.setPlaceholderText("Введите URL")

        self.pushButton = QtWidgets.QPushButton("Начать выполнение")
        self.pushButton.setCheckable(True)

        self.spinBox = QtWidgets.QSpinBox()
        self.spinBox.setValue(2)
        self.spinBox.setMinimum(2)

        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setReadOnly(True)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lineEditUrl)
        layout.addWidget(self.spinBox)
        layout.addWidget(self.pushButton)
        layout.addWidget(self.plainTextEdit)

        self.setLayout(layout)

    def initThread(self):
        self.urlCheckerThread = URLCheckerThread()
        self.urlCheckerThread.url = 'https://www.google.ru/'
        self.urlCheckerThread.start()


class URLCheckerThread(QtCore.QThread):
    responsed = QtCore.Signal(int)

    def __init__(self, url=None, timeout=2, parent=None):
        super().__init__(parent)

        self.url = url
        self.timeout = timeout
        self.status = True

    def run(self):

        while self.status:
            response = requests.get(self.url)
            print(response.status_code)

            time.sleep(self.timeout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
