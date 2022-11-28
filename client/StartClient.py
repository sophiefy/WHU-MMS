from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

sys.path.append('frontend')
sys.path.append('backend')
from frontend.windows import *


class Client:
    def __init__(self):
        self.mainWin = MainWin()
        self.loginWin = LoginWin()

        self.init_signal_slots()

    def init_signal_slots(self):
        self.loginWin.loginBtn.clicked.connect(self.log_in)
        self.mainWin.logoutBtn.clicked.connect(self.log_out)

    def log_in(self):
        # TODO: 发送请求至服务端
        self.loginWin.close()
        self.mainWin.show()

    def log_out(self):
        reply = QMessageBox.question(self.mainWin,
                                     '询问',
                                     "确定要登出吗？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.mainWin.close()
            self.loginWin.exec()
        else:
            pass


if __name__ == '__main__':
    app = QApplication([])
    client = Client()
    client.loginWin.exec()
    sys.exit(app.exec())
