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

        self.create_connection('database/books.db')

    def create_connection(self, db_path):
        self.database = Database(db_path)
        self.database.create_connection()

    def update_book_table(self):
        if self.database:
            table = self.database.read_book()
            # TODO: 对数据分页

            if table:
                self.mainWin.updateBookTable(table)
        else:
            QMessageBox.warning(self.mainWin, '警告', '请先链接至数据库！')

    def add_book(self):
        name, author, press, category, release_date, ISBN = self.mainWin.getNewBookInfo()

        if self.database:
            try:
                self.database.add_book(name, author, press, category, release_date, ISBN)
            except Exception as e:
                print(e)
            else:
                self.update_book_table()

    def edit_book(self):
        try:
            row = self.mainWin.getSelectedBookInfo()
            print('row', row)
        except:
            print('error')
            QMessageBox.warning(self.mainWin, '警告', '请先选择要编辑的书籍！')
        else:
            self.editBookWin.putOldBookInfo(row)
            self.editBookWin.exec()

    def confirm_edit_book(self):
        name, author, press, category, release_date, ISBN = self.editBookWin.getNewBookInfo()
        if self.database:
            try:
                self.database.update_book(name, author, press, category, release_date, ISBN)
            except Exception as e:
                print(e)
            else:
                self.update_book_table()

        self.editBookWin.close()

    def delete_book(self):
        if self.database:
            try:
                _, _, _, _, _, ISBN = self.mainWin.getSelectedBookInfo()
            except:
                QMessageBox.warning(self.mainWin, '警告', '请先选择要删除的书籍！')
            else:
                reply = QMessageBox.question(self.mainWin,
                                             '询问',
                                             '确定要删除该书籍吗？',
                                             QMessageBox.Yes | QMessageBox.No,
                                             QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.database.delete_book(ISBN)
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

    def add_paper(self):
        title, author, institute, field, release_date, conference, DOI = self.mainWin.getNewPaperInfo()

        if self.database:
            try:
                self.database.add_paper(title, author, institute, field, release_date, conference, DOI)
            except Exception as e:
                print(e)
            else:
                self.update_paper_table()

    def edit_paper(self):
        try:
            row = self.mainWin.getSelectedPaperInfo()
        except:
            QMessageBox.warning(self.mainWin, '警告', '请先选择要编辑的论文！')
        else:
            self.editPaperWin.putOldPaperInfo(row)
            self.editPaperWin.exec()

    def confirm_edit_paper(self):
        title, author, institute, field, release_date, conference, DOI = self.editPaperWin.getNewPaperInfo()
        if self.database:
            try:
                self.database.update_paper(title, author, institute, release_date, conference, DOI)
            except Exception as e:
                print(e)
            else:
                self.update_paper_table()

        self.editPaperWin.close()

    def delete_paper(self):
        if self.database:
            try:
                _, _, _, _, _, _, DOI = self.mainWin.getSelectedPaperInfo()
            except:
                QMessageBox.warning(self.mainWin, '警告', '请先选择要删除的论文！')
            else:
                reply = QMessageBox.question(self.mainWin,
                                             '询问',
                                             '确定要删除该书籍吗？',
                                             QMessageBox.Yes | QMessageBox.No,
                                             QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.database.delete_paper(DOI)
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

    def add_user(self):
        name, password, phone, number = self.mainWin.getNewUserInfo()

        if self.database:
            try:
                self.database.add_user(name, password, phone, number)
            except Exception as e:
                print(e)
            else:
                self.update_user_table()

    def edit_user(self):
        try:
            row = self.mainWin.getSelectedUserInfo()
        except:
            QMessageBox.warning(self.mainWin, '警告', '请先选择要编辑的用户！')
        else:
            self.editUserWin.putOldUserInfo(row)
            self.editUserWin.exec()

    def confirm_edit_user(self):
        name, password, phone, number = self.editUserWin.getNewUserInfo()
        if self.database:
            try:
                self.database.update_user(name, password, phone, number)
            except Exception as e:
                print(e)
            else:
                self.update_user_table()

        self.editUserWin.close()

    def delete_user(self):
        if self.database:
            try:
                _, _, _, number = self.mainWin.getSelectedUserInfo()
            except:
                QMessageBox.warning(self.mainWin, '警告', '请先选择要删除的用户！')
            else:
                reply = QMessageBox.question(self.mainWin,
                                             '询问',
                                             '确定要删除该书籍吗？',
                                             QMessageBox.Yes | QMessageBox.No,
                                             QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.database.delete_user(number)
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
                QMessageBox.information(self.mainWin, '提示', '跳转页码超出范围！')
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
