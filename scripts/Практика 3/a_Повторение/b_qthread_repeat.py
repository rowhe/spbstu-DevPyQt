"""
Файл для повторения темы QThread

Напомнить про работу с QThread.

Предлагается создать небольшое приложение, которое будет с помощью модуля request
получать доступность того или иного сайта (возвращать из потока status_code сайта).

Поработать с сигналами, которые возникают при запуске/остановке потока,
передать данные в поток (в данном случае url),
получить данные из потока (статус код сайта),
попробовать управлять потоком (запуск, остановка).

Опционально поработать с валидацией url
"""
import os
import time

import requests
from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initThreads()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.setMinimumSize(600, 400)

        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setReadOnly(True)

        self.pushButtonThreadHandle = QtWidgets.QPushButton("Запустить")
        self.pushButtonThreadHandle.setCheckable(True)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.plainTextEdit)
        layout.addWidget(self.pushButtonThreadHandle)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButtonThreadHandle.clicked.connect(self.threadHandle)
        self.downloadManager.started.connect(
            lambda: self.plainTextEdit.appendPlainText(f"{time.ctime()} >>> Загрузка файлов начата"))
        self.downloadManager.finished.connect(self.downloadManagerFinished)
        self.downloadManager.download_finished.connect(lambda file_url: self.plainTextEdit.appendPlainText(
            f"{time.ctime()} >>> Загрузка файла {file_url} закончена"))
        self.downloadManager.download_started.connect(
            lambda file_url: self.plainTextEdit.appendPlainText(f"{time.ctime()} >>> Загрузка файла {file_url} начата"))

    def initThreads(self) -> None:
        """
        Инициализация потоков

        :return: None
        """

        self.downloadManager = DownloadManager()

    def threadHandle(self, button_status: bool) -> None:
        """
        Метод для обработки нажатия на кнопку запуска/остановки сигналов

        :param button_status: состояние кнопка (нажата/отжата)
        :return: None
        """

        if not button_status:
            self.downloadManager.status = False
            self.pushButtonThreadHandle.setText("Запустить")
            return

        self.downloadManager.start()
        self.pushButtonThreadHandle.setText("Остановить")

    def downloadManagerFinished(self) -> None:
        """
        Метод для обработки сигнала завершения потока downloadManager

        :return: None
        """

        self.plainTextEdit.appendPlainText(f"{time.ctime()} >>> Загрузка файлов завершена")
        self.pushButtonThreadHandle.setChecked(False)
        self.pushButtonThreadHandle.setText("Запустить")


class DownloadManager(QtCore.QThread):
    download_started = QtCore.Signal(str)
    download_finished = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__delay = 4
        self.__status = None
        self.__queue = []

    @property
    def delay(self) -> str:
        return self.__delay

    @delay.setter
    def delay(self, value):
        if not isinstance(value, int):
            raise ValueError
        self.__delay = value

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, value):
        if not isinstance(value, bool):
            raise ValueError
        self.__status = value

    @property
    def queue(self):
        return self.__queue

    def run(self) -> None:
        response = requests.get("https://api.imgflip.com/get_memes")
        data = response.json()['data']['memes']

        if response.status_code != 200:
            pass

        self.status = True

        while data and self.status:
            if len(self.queue) > 10:
                continue

            downloader = Downloader(self)
            downloader.finished.connect(self.fileDownloaded)
            downloader.url = data.pop()["url"]

            self.__queue.append(downloader)
            downloader.start()
            self.download_started.emit(downloader.url)

    def fileDownloaded(self):
        self.download_finished.emit(self.sender().url)
        self.__queue.remove(self.sender())


class Downloader(QtCore.QThread):
    downloaded = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__url = ""

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, value):
        if not isinstance(value, str):
            raise ValueError
        self.__url = value

    def run(self) -> None:
        if not self.url:
            return

        image = requests.get(self.url).content
        image_name = self.url.split("/")[-1]
        with open(os.path.join("images", image_name), "wb") as f:
            f.write(image)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
