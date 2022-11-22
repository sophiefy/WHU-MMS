from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


from mainWin import Ui_MainWindow


class MainWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWin, self).__init__()

        self.setupUi(self)

        self.initSignalSlots()

    def initSignalSlots(self):
        # NOTE: CRUD -> Create, Read, Update and Delete
        self.actionHome.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.actionCbook.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.actionRbook.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.actionCpaper.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.actionRpaper.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.actionCuser.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.actionRuser.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        # self.actionStatBook
        # self.actionStatBook
        # self.actionStatPaper

    def closeEvent(self, e):
        reply = QMessageBox.question(self,
                                     '询问',
                                     "确定要退出吗？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            e.accept()
            sys.exit(0)
        else:
            e.ignore()


class Admin:
    def __init__(self):
        self.mainWin = MainWin()



if __name__ == '__main__':
    app = QApplication([])
    admin = Admin()
    admin.mainWin.show()
    sys.exit(app.exec())
