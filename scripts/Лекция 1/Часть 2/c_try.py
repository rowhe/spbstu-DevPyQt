from PySide6 import QtWidgets


class addWidgets(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        # btn = QtWidgets.QPushButton("Button", self)
        # btn.move(30, 30)

        layout = QtWidgets.QVBoxLayout()
        pushButton = QtWidgets.QPushButton("Button")
        radioButton = QtWidgets.QRadioButton("RadioButton")
        checkBox = QtWidgets.QCheckBox("CheckBox")
        layout.addWidget(checkBox)
        layout.addWidget(radioButton)
        layout.addWidget(pushButton)
        self.setLayout(layout)



if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = addWidgets()
    window.show()
    app.exec()
