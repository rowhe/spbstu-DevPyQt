"""
Файл для повторения темы фильтр событий

Напомнить про работу с фильтром событий.

Предлагается создать кликабельный QLabel с текстом "Красивая кнопка",
используя html - теги, покрасить разные части текста на нём в разные цвета
(красивая - красным, кнопка - синим)
"""

from PySide6 import QtWidgets, QtCore, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):
        self.label = QtWidgets.QLabel("-----")
        self.label.installEventFilter(self)
        self.label.setText("<span style='color: red'>Нестандартная</span> <span style='color: blue'>кнопка</span>")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("border: 1px solid black")

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.label)

        self.setLayout(layout)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if watched == self.label and event.type() == QtCore.QEvent.Type.MouseButtonPress:
            if event.button() == QtCore.Qt.MouseButton.LeftButton:
                print("Нажата левая кнопка мыши")
            if event.button() == QtCore.Qt.MouseButton.RightButton:
                print("Нажата правая кнопка мыши")

        return super(Window, self).eventFilter(watched, event)

# class Window(QtWidgets.QLabel):
#     clicked = QtCore.Signal(bool)
#     def __init__(self):
#         super(Window, self).__init__(None)
#
#         self.setText("Кнопка-окно")
#         self.installEventFilter(self)
#
#     def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
#         if watched == self and event.type() == QtCore.QEvent.Type.MouseButtonPress:
#             if event.button() == QtCore.Qt.MouseButton.LeftButton:
#                 print("Нажата левая кнопка мыши")
#             if event.button() == QtCore.Qt.MouseButton.RightButton:
#                 print("Нажата правая кнопка мыши")
#
#
#         return super(Window, self).eventFilter(watched, event)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.clicked.connect(lambda data: print(data))
    window.show()

    app.exec()
