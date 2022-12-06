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
        self.uploadWin = UploadWin()

        self.init_signal_slots()

    def init_signal_slots(self):
        self.mainWin.pageSignal.connect(self.turn_page)
        self.loginWin.loginBtn.clicked.connect(self.log_in)
        self.mainWin.logoutBtn.clicked.connect(self.log_out)
        self.mainWin.bookBuyBtn.clicked.connect(self.buy_book)
        self.mainWin.paperUploadBtn.clicked.connect(self.upload_paper)

    def log_in(self):
        # TODO: 发送请求至服务端
        number = self.loginWin.loginNumEdit.text()
        self.loginWin.close_flag = False
        self.loginWin.close()
        self.loginWin.close_flag = True
        self.mainWin.numEdit.setText(number)
        self.mainWin.show()

    def log_out(self):
        reply = QMessageBox.question(self.mainWin,
                                     '询问',
                                     "确定要登出吗？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.mainWin.close_flag = False
            self.mainWin.close()
            self.mainWin.close_flag = True
            self.loginWin.loginPasswordEdit.setText('')  # 登录界面密码栏清空
            self.loginWin.exec()
        else:
            pass

    def buy_book(self):
        try:
            book_info = self.mainWin.getSelectedBookInfo()
        except:
            QMessageBox.warning(self.mainWin, '警告', '请先选择要购买的图书！')
        else:
            reply = QMessageBox.question(self.mainWin,
                                         '询问',
                                         "确定要购买这本书吗？",
                                         QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
            if reply == QMessageBox.Yes:
                print('成功购买: ', book_info)
                # TODO: 后端检查是否可以购买并修改数据库图书信息
            else:
                pass

    def upload_paper(self):
        self.uploadWin.exec()


    # SECTION: 翻页
    def turn_page(self, signal):
        type = signal[0]
        command = signal[1]
        page = int(signal[2])  # 可以是上一次的current page，也可以是target page
        total_page = self.mainWin.totalPage(type)

        if command == 'first':
            cur_page = str(1)
        elif command == 'pre':
            if page == 1:  # 当前页面已经是第一页
                QMessageBox.information(self.mainWin, '提示', '已经是第一页了！')
                return
            cur_page = str(page - 1)
        elif command == 'next':
            if page == total_page:  # 当前页面已经是最后一页
                QMessageBox.information(self.mainWin, '提示', '已经是最后一页了！')
                return
            cur_page = str(page + 1)
        elif command == 'last':
            cur_page = str(total_page)
        elif command == 'jump':
            if page < 0 or page > total_page:  # 跳转超出范围
                QMessageBox.information(self.mainWin, '提示', '非法的跳转页码！')
                return
            cur_page = str(page)
        else:
            QMessageBox.critical(self.mainWin, '错误', '未知指令类型！')
            return

        if type == 'book':
            self.mainWin.bookPage.setText('{} / {}'.format(cur_page, total_page))
            # TODO: 刷新表内容
        elif type == 'paper':
            self.mainWin.paperPage.setText('{} / {}'.format(cur_page, total_page))
            # TODO: 刷新表内容
        else:
            QMessageBox.critical(self.mainWin, '错误', '未知数据类型！')
            return


if __name__ == '__main__':
    app = QApplication([])
    client = Client()
    client.loginWin.exec()
    sys.exit(app.exec())
