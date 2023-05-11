"""
Файл для повторения темы QSettings

Напомнить про работу с QSettings.

Предлагается создать виджет с plainTextEdit на нём, при закрытии приложения,
сохранять введённый в нём текст с помощью QSettings, а при открытии устанавливать
в него сохранённый текст
"""

from PySide6 import QtWidgets, QtGui, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        settings = QtCore.QSettings("MyApp")

        print(settings.fileName())

        if settings.value("monitor_count", 1) != len(QtWidgets.QApplication.screens()):
            self.move(100, 100)
        else:
            self.move(settings.value("pos", QtCore.QPoint(100, 100)))

        self.resize(settings.value("size", QtCore.QSize(300, 200)))

        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setPlainText(settings.value("text", "Значение по умолчанию"))

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.plainTextEdit)

        self.setLayout(layout)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:

        settings = QtCore.QSettings("MyApp")
        print(settings.fileName())

        settings.setValue("text", self.plainTextEdit.toPlainText())
        settings.setValue("size", self.size())
        settings.setValue("pos", self.pos())
        settings.setValue("monitor_count", len(QtWidgets.QApplication.screens()))



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

