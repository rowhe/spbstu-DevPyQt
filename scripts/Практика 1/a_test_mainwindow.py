import sys
from PySide6 import QtWidgets, QtGui


class MyMainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        # menuBar отсутствует у QWidgets
        self.fileMenu = self.menuBar().addMenu('File')
        self.fileMenu.addAction("Open")

        # toolBar отсутствует у QWidgets
        self.toolBarFirst = self.addToolBar("First")
        self.toolBarFirst.addAction("Edit_1")

        self.toolBarSec = self.addToolBar("Second")
        self.toolBarSec.addAction("Edit_2")
        self.toolBarSec.addAction("Edit_3")

        # statusBar отсутствует у QWidgets
        self.appStatusBar = self.statusBar()
        self.appStatusBar.showMessage("Status: Ok!")

        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

        layout = QtWidgets.QHBoxLayout()
        centralWidget.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyMainWindow()
    myWindow.show()

    app.exec_()