from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

        print(self.pushButton.clicked)

    def initUi(self) -> None:
        self.pushButton = QtWidgets.QPushButton("Выполняю что-то")
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.pushButton)
        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Signal initializing
        :return: None
        """
        self.pushButton.clicked.connect(self.onPushButtonClicked)

    @QtCore.Slot()
    def onPushButtonClicked(self):
        print("PushButton was clicked")


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = Window()
    window.show()

    app.exec()
