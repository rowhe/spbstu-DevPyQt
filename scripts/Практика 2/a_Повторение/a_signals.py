"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """

        :return:
        """

        self.lineEditInput = QtWidgets.QLineEdit()
        self.lineEditMirror = QtWidgets.QLineEdit()
        self.lineEditMirror.setReadOnly(True)

        self.pushButtonMirror = QtWidgets.QPushButton("Отзеркалить")
        self.pushButtonClearMirror = QtWidgets.QPushButton("Очистить результат")

        layoutLineEdit = QtWidgets.QHBoxLayout()
        layoutLineEdit.addWidget(self.lineEditInput)
        layoutLineEdit.addWidget(self.lineEditMirror)

        layoutPushButton = QtWidgets.QHBoxLayout()
        layoutPushButton.addWidget(self.pushButtonMirror)
        layoutPushButton.addWidget(self.pushButtonClearMirror)

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutLineEdit)
        layoutMain.addLayout(layoutPushButton)

        self.setLayout(layoutMain)

    def initSignals(self):
        self.pushButtonMirror.clicked.connect(self.mirrorText)
        self.pushButtonClearMirror.clicked.connect(self.lineEditMirror.clear)

        # self.lineEditInput.textChanged.connect(self.mirrorText)

        # виджет . сигнал . connect(ССЫЛКА на функцию для вызова)

    def mirrorText(self) -> None:
        source_text = self.lineEditInput.text()
        self.lineEditMirror.setText(source_text[::-1])

    def clearLineEdits(self):
        self.lineEditMirror.clear()
        self.lineEditInput.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
