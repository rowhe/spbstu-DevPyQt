"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets, QtCore, QtGui
from ui.task_a import Ui_MainWindow  # Импортируем класс формы


class Window(QtWidgets.QMainWindow):  # наследуемся от того же класса, что и форма в QtDesigner
    def __init__(self, parent=None):
        super().__init__(parent)

        # Создание "прокси" переменной для работы с формой
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initSignals()

    def initSignals(self):
        # self.ui.pushButton.clicked.connect(self.reverse_text)
        self.ui.lineEdit.textChanged.connect(self.reverse_text)
    def reverse_text(self):
        text = self.ui.lineEdit.text()
        self.ui.lineEdit_2.setText(text[::-1])

    # def event(self, event: QtCore.QEvent) -> bool:
    #     print(event)
    #     return super().event(event)

    # def event(self, event) -> bool:
    #     print(event)
    #     return super().event(event)
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        print(event.text(), event.key(), event.keyCombination())
        if event.text() == "r":
            self.ui.lineEdit_3.clear()
        return super().keyPressEvent(event)

    def mousePressEvent(self, event) -> None:
        print(event)
        if event.button() == QtCore.Qt.LeftButton:
            print("Нажали левую кнопку")

        return super().mousePressEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
