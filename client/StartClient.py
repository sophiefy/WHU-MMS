from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

sys.path.append('frontend')
sys.path.append('backend')
from frontend.windows import *
from backend.RUD import Database
import threading

class Client:
    def __init__(self):
        self.mainWin = MainWin()
        self.loginWin = LoginWin()
        self.uploadWin = UploadWin()

        self.registered = False
        self.database = None
        self.init_signal_slots()
        self.create_connection()

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
            user_info = self.database.user_login(*login_info)
            if user_info:
                self.registered = True  # 是注册用户
                self.loginWin.close_flag = False
                self.loginWin.close()
                self.loginWin.close_flag = True
                self.mainWin.numEdit.setText(login_info[0])
                self.mainWin.nameEdit.setText(user_info[1])
                self.mainWin.show()
            else:
                QMessageBox.warning(self.loginWin,
                                    '警告',
                                    "用户名或密码错误！",
                                    QMessageBox.Yes)
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
                self.mainWin.numEdit.setText('游客')
                self.mainWin.nameEdit.setText('游客')
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

    def create_connection(self):
        self.database = Database()
        self.database.create_connection()

    def update_book_table(self):
        print('try to update')
        # TODO: 从数据库获取表项
        table = self.database.read_book(20)
        print('table', table)
        # TODO: 对数据分页
        if table:
            self.mainWin.updateBookTable(table)

    def search_book(self):
        # name, author, press, release_date, ISBN
        # 可以为空
        keys = self.mainWin.getBookSearchKey()
        print('search books by keys:', keys)
        table = self.database.search_book(*keys, limit=20)
        if table:
            self.mainWin.updateBookTable(table)


    def buy_book(self):
        if self.registered:
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
        else:
            reply = QMessageBox.question(self.mainWin,
                                         '询问',
                                         "游客无法购买图书！\n"
                                         "是否前往注册？",
                                         QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.mainWin.close_flag = False
                self.mainWin.close()
                self.mainWin.close_flag = True
                self.loginWin.stackedWidget.setCurrentIndex(1)
                self.loginWin.close_flag = False
                self.loginWin.exec()
                self.loginWin.close_flag = True
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
        table = self.database.search_paper(*keys, limit=20)
        if table:
            self.mainWin.updatePaperTable(table)

    def upload_paper(self):
        if self.registered:
            self.uploadWin.exec()
        else:
            reply = QMessageBox.question(self.mainWin,
                                         '询问',
                                         "游客无法上传论文！\n"
                                         "是否前往注册？",
                                         QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.mainWin.close_flag = False
                self.mainWin.close()
                self.mainWin.close_flag = True
                self.loginWin.stackedWidget.setCurrentIndex(1)
                self.loginWin.close_flag = False
                self.loginWin.exec()
                self.loginWin.close_flag = True
            else:
                pass

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
