from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from loginWin import Ui_FormLogin
from mainWin import Ui_MainWindow


class LoginWin(QDialog, Ui_FormLogin):
    def __init__(self):
        super(LoginWin, self).__init__()

        self.setupUi(self)

        self.initSignalSlots()

    def initSignalSlots(self):
        self.toLoginBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.toRegisterBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))


class MainWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWin, self).__init__()

        self.setupUi(self)

        self.initSignalSlots()

    def initSignalSlots(self):
        self.toHomeBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.toSearchBookBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.toSearchPaperBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.aboutBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

    def closeEvent(self, e):
        reply = QMessageBox.question(self,
                                     '询问',
                                     "确定要退出吗？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            e.accept()
            self.close()
        else:
            e.ignore()
