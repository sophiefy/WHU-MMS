import traceback
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

sys.path.append('frontend')
sys.path.append('backend')
from frontend.windows import *
from backend.CRUD import Database


class Admin:
    def __init__(self):
        self.mainWin = MainWin()
        self.mainWin.pageSignal.connect(self.turn_page)
        self.editBookWin = EditBookWin()
        self.editPaperWin = EditPaperWin()
        self.editUserWin = EditUserWin()
        self.database = None

        # initial signal slots
        self.mainWin.searchBookBtn.clicked.connect(self.update_book_table)
        self.mainWin.bookAddBtn.clicked.connect(self.add_book)
        self.mainWin.bookEditBtn.clicked.connect(self.edit_book)
        self.mainWin.bookDeleteBtn.clicked.connect(self.delete_book)

        self.editBookWin.bookEditBtn.clicked.connect(self.confirm_edit_book)

        self.create_connection()

    def create_connection(self):
        self.database = Database()
        self.database.create_connection()

    def update_book_table(self):
        if self.database:
            # table = self.database.read_book()
            # # TODO: 对数据分页
            # if table:
            #     self.mainWin.updateBookTable(table)
            print('update book table!')
        else:
            QMessageBox.warning(self.mainWin, '警告', '请先链接至数据库！')

    def search_book(self):
        # id, name, author, press, release_date, ISBN
        # 可以为空
        keys = self.mainWin.getBookSearchKey()
        print('search books by keys:', keys)

        # TODO: 1.用线程获取数据库的表；2.将表分页显示；3.统计查询结果数量并显示

    def add_book(self):
        new_book_info = self.mainWin.getNewBookInfo()

        if self.database and new_book_info:
            try:
                # self.database.add_book(new_book_info)
                print('add book: ', new_book_info)
            except Exception as e:
                print(e)
            else:
                self.update_book_table()

    def edit_book(self):
        try:
            old_book_info = self.mainWin.getSelectedBookInfo()
        except:
            QMessageBox.warning(self.mainWin, '警告', '请先选择要编辑的书籍！')
        else:
            self.editBookWin.putOldBookInfo(old_book_info)
            self.editBookWin.exec()

    def confirm_edit_book(self):
        new_book_info = self.editBookWin.getNewBookInfo()
        if self.database:
            try:
                self.database.update_book(new_book_info)
            except Exception as e:
                print(e)
            else:
                self.update_book_table()

        self.editBookWin.close()

    def delete_book(self):
        if self.database:
            try:
                old_book_info = self.mainWin.getSelectedBookInfo()
                id = old_book_info[0]  # primary key
            except:
                QMessageBox.warning(self.mainWin, '警告', '请先选择要删除的书籍！')
            else:
                reply = QMessageBox.question(self.mainWin,
                                             '询问',
                                             '确定要删除该书籍吗？',
                                             QMessageBox.Yes | QMessageBox.No,
                                             QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.database.delete_book(id)
                    self.update_book_table()
                else:
                    pass

    def update_paper_table(self):
        if self.database:
            table = self.database.read_paper()
            # TODO: 对数据分页
            if table:
                self.mainWin.updatePaperTable(table)
        else:
            QMessageBox.warning(self.mainWin, '警告', '请先链接至数据库！')

    def search_paper(self):
        keys = self.mainWin.getPaperSearchKey()
        print('search papers by keys:', keys)

        # TODO: 1.用线程获取数据库的表；2.将表分页显示；3.统计查询结果数量并显示

    def add_paper(self):
        new_paper_info = self.mainWin.getNewPaperInfo()

        if self.database:
            try:
                self.database.add_paper(new_paper_info)
            except Exception as e:
                print(e)
            else:
                self.update_paper_table()

    def edit_paper(self):
        try:
            old_paper_info = self.mainWin.getSelectedPaperInfo()
        except:
            QMessageBox.warning(self.mainWin, '警告', '请先选择要编辑的论文！')
        else:
            self.editPaperWin.putOldPaperInfo(old_paper_info)
            self.editPaperWin.exec()

    def confirm_edit_paper(self):
        new_paper_info = self.editPaperWin.getNewPaperInfo()
        if self.database:
            try:
                self.database.update_paper(new_paper_info)
            except Exception as e:
                print(e)
            else:
                self.update_paper_table()

        self.editPaperWin.close()

    def delete_paper(self):
        if self.database:
            try:
                old_paper_info = self.mainWin.getSelectedPaperInfo()
                id = old_paper_info[0]  # primary key
            except:
                QMessageBox.warning(self.mainWin, '警告', '请先选择要删除的论文！')
            else:
                reply = QMessageBox.question(self.mainWin,
                                             '询问',
                                             '确定要删除该书籍吗？',
                                             QMessageBox.Yes | QMessageBox.No,
                                             QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.database.delete_paper(id)
                    self.update_paper_table()
                else:
                    pass

    def update_user_table(self):
        if self.database:
            table = self.database.read_user()
            # TODO: 对数据分页
            if table:
                self.mainWin.updateUserTable(table)
        else:
            QMessageBox.warning(self.mainWin, '警告', '请先链接至数据库！')

    def search_user(self):
        keys = self.mainWin.getUserSearchKey()
        print('search users by keys:', keys)

        # TODO: 1.用线程获取数据库的表；2.将表分页显示；3.统计查询结果数量并显示

    def add_user(self):
        new_user_info = self.mainWin.getNewUserInfo()

        if self.database:
            try:
                self.database.add_user(new_user_info)
            except Exception as e:
                print(e)
            else:
                self.update_user_table()

    def edit_user(self):
        try:
            old_user_info = self.mainWin.getSelectedUserInfo()
        except:
            QMessageBox.warning(self.mainWin, '警告', '请先选择要编辑的用户！')
        else:
            self.editUserWin.putOldUserInfo(old_user_info)
            self.editUserWin.exec()

    def confirm_edit_user(self):
        new_user_info = self.editUserWin.getNewUserInfo()
        if self.database:
            try:
                self.database.update_user(new_user_info)
            except Exception as e:
                print(e)
            else:
                self.update_user_table()

        self.editUserWin.close()

    def delete_user(self):
        if self.database:
            try:
                old_user_info = self.mainWin.getSelectedUserInfo()
                id = old_user_info[0]  # primary key
            except:
                QMessageBox.warning(self.mainWin, '警告', '请先选择要删除的用户！')
            else:
                reply = QMessageBox.question(self.mainWin,
                                             '询问',
                                             '确定要删除该书籍吗？',
                                             QMessageBox.Yes | QMessageBox.No,
                                             QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.database.delete_user(id)
                    self.update_user_table()
                else:
                    pass

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
        elif type == 'user':
            self.mainWin.userPage.setText('{} / {}'.format(cur_page, total_page))
            # TODO: 刷新表内容
        else:
            QMessageBox.critical(self.mainWin, '错误', '未知数据类型！')
            return


if __name__ == '__main__':
    app = QApplication([])
    admin = Admin()
    admin.mainWin.show()
    sys.exit(app.exec())
