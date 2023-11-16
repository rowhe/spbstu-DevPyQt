from PySide6 import QtWidgets

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.fileMenu = self.menuBar().addMenu('File')
        self.fileMenu = self.menuBar().addAction('Open')

        self.toolBarOne = self.addToolBar('One')
        self.toolBarOne.addAction('Action One')

        self.toolBarTwo = self.addToolBar('Two')
        self.toolBarTwo.addAction('New Action')
        self.toolBarTwo.addAction('New Action2')

        self.appStatusBar = self.statusBar()
        self.appStatusBar.showMessage('Hello!')

        layout = QtWidgets.QHBoxLayout()
        self.bcd = QtWidgets.QPushButton('bcd')
        self.bcd.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

        layout.addWidget(QtWidgets.QLabel("Надпись"))
        layout.addWidget(self.bcd)

        centralWidget = QtWidgets.QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = Window()
    window.show()

    app.exec_()