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

        self.registered = False
        self.mainWin.bookBuyBtn.setDisabled(True)
        self.mainWin.paperUploadBtn.setDisabled(True)

        self.init_signal_slots()

    def init_signal_slots(self):
        self.loginWin.loginBtn.clicked.connect(self.log_in)
        self.loginWin.registerBtn.clicked.connect(self.register)

        self.mainWin.pageSignal.connect(self.turn_page)
        self.mainWin.logoutBtn.clicked.connect(self.log_out)
        self.mainWin.searchBookBtn.clicked.connect(self.search_book)
        self.mainWin.searchPaperBtn.clicked.connect(self.search_paper)
        self.mainWin.bookBuyBtn.clicked.connect(self.buy_book)
        self.mainWin.paperUploadBtn.clicked.connect(self.upload_paper)


    def register(self):
        # name, password, age, dpt, grade
        reg_info = self.loginWin.getRegisterInfo()
        if reg_info:
            # TODO: 数据库检查是否可以注册
            print('register: ', reg_info)
        else:
            pass

    def log_in(self):
        # TODO: 发送请求至数据库
        login_info = self.loginWin.getLoginInfo()   # number, password
        if login_info:
            # pass or not

            self.registered = True  # 是注册用户
            self.mainWin.bookBuyBtn.setEnabled(True)
            self.mainWin.paperUploadBtn.setEnabled(True)
            self.loginWin.close_flag = False
            self.loginWin.close()
            self.loginWin.close_flag = True
            self.mainWin.numEdit.setText(login_info[0])
            self.mainWin.show()
        else:
            reply = QMessageBox.question(self.mainWin,
                                         '询问',
                                         "要以游客身份访问吗？",
                                         QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.loginWin.close_flag = False
                self.loginWin.close()
                self.loginWin.close_flag = True
                self.mainWin.show()
            else:
                pass
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

    def update_book_table(self):
        print('try to update')
        # TODO: 从数据库获取表项
        table = ()
        print('table', table)
        # TODO: 对数据分页
        if table:
            self.mainWin.updateBookTable(table)

    def search_book(self):
        # name, author, press, release_date, ISBN
        # 可以为空
        keys = self.mainWin.getBookSearchKey()
        print('search books by keys:', keys)

        # TODO: 1.用线程获取数据库的表；2.将表分页显示；3.统计查询结果数量并显示

    def buy_book(self):
        try:
            # id, name, author, press, release_date, ISBN, stock
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

    def update_paper_table(self):
        # TODO: 从数据库获取表项
        table = ()
        print('paper table', table)
        # TODO: 对数据分页
        if table:
            self.mainWin.updatePaperTable(table)

    def search_paper(self):
        keys = self.mainWin.getPaperSearchKey()
        print('search papers by keys:', keys)

    def upload_paper(self):
        self.uploadWin.exec()

    def confirm_upload_paper(self):
        try:
            new_paper_info = self.uploadWin.getNewPaperInfo()
        except Exception as e:
            print(e)
        else:
            # TODO: 将要上传的论文信息发送至数据库。数据库检查是否可以插入。
            self.uploadWin.close()


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
