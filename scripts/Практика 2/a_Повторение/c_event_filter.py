"""
Файл для повторения темы фильтр событий

Напомнить про работу с фильтром событий.

Предлагается создать кликабельный QLabel с текстом "Красивая кнопка",
используя html - теги, покрасить разные части текста на нём в разные цвета
(красивая - красным, кнопка - синим)
"""

from PySide6 import QtWidgets, QtCore
from ui.task_a import Ui_MainWindow


class Window(QtWidgets.QMainWindow):  # наследуемся от того же класса, что и форма в QtDesigner
    def __init__(self, parent=None):
        super().__init__(parent)

        centralWidget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(self)
        centralWidget.setLayout(layout)
        self.pb = QtWidgets.QPushButton("Press me")
        self.pb1 = QtWidgets.QPushButton("Press me too")
        self.setMouseTracking(True)

        layout.addWidget(self.pb)
        layout.addWidget(self.pb1)
        self.setCentralWidget(centralWidget)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if watched == self.pb:
            print(event.type())
            if event.type() == QtCore.QEvent.Type.Leave:
                print("Вышли из области")
            if event.type() == QtCore.QEvent.Type.Enter:
                print("Вошли в область")
        return super().eventFilter(watched, event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
