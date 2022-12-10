import math
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

        # SECTION: initial signal slots
        # book
        self.mainWin.searchBookBtn.clicked.connect(self.search_book)
        self.mainWin.bookAddBtn.clicked.connect(self.add_book)
        self.mainWin.bookEditBtn.clicked.connect(self.edit_book)
        self.mainWin.bookDeleteBtn.clicked.connect(self.delete_book)
        self.editBookWin.bookEditBtn.clicked.connect(self.confirm_edit_book)

        # buyer
        self.mainWin.searchBuyerBtn.clicked.connect(self.search_buyer)
        self.mainWin.freshBookFanBtn.clicked.connect(self.update_top_buyer_table)
        self.mainWin.freshBestSellerBtn.clicked.connect(self.update_top_book_table)

        # paper
        self.mainWin.searchPaperBtn.clicked.connect(self.search_paper)
        self.mainWin.paperAddBtn.clicked.connect(self.add_paper)
        self.mainWin.paperEditBtn.clicked.connect(self.edit_paper)
        self.mainWin.paperDeleteBtn.clicked.connect(self.delete_paper)
        self.editPaperWin.paperEditBtn.clicked.connect(self.confirm_edit_paper)

        # upload
        self.mainWin.searchUploadBtn.clicked.connect(self.search_upload)
        self.mainWin.freshContributorBtn.clicked.connect(self.update_top_uploader_table)

        # user
        self.mainWin.searchUserBtn.clicked.connect(self.search_user)
        self.mainWin.userAddBtn.clicked.connect(self.add_user)
        self.mainWin.userEditBtn.clicked.connect(self.edit_user)
        self.mainWin.userDeleteBtn.clicked.connect(self.delete_user)
        self.editUserWin.userEditBtn.clicked.connect(self.confirm_edit_user)

        self.book_search_keys = self.mainWin.getBookSearchKey()
        self.paper_search_keys = self.mainWin.getPaperSearchKey()
        self.user_search_keys = self.mainWin.getUserSearchKey()
        self.buyer_search_keys = self.mainWin.getBuyerSearchKey()
        self.upload_search_keys = self.mainWin.getBuyerSearchKey()

        self.create_connection()

    def create_connection(self):
        self.database = Database()
        self.database.create_connection()

    def update_book_table(self, keys, page_num=1):
        if self.database:
            offset = (page_num - 1) * 20
            table = self.database.search_book(*keys, limit=20, offset=offset)  # TODO: 分页
            if table:
                self.mainWin.updateBookTable(table)
        else:
            QMessageBox.warning(self.mainWin, '警告', '请先链接至数据库！')

    def search_book(self):
        # id, name, author, press, release_date, ISBN
        # 可以为空
        self.book_search_keys = self.mainWin.getBookSearchKey()
        if not self.book_search_keys:
            return

        total_num = self.database.get_book_num(*self.book_search_keys)
        total_page = math.ceil(total_num / 20)
        self.mainWin.setTotalPage('book', total_page)
        self.mainWin.showBookNum(total_num)
        self.update_book_table(keys=self.book_search_keys)

        return

    def add_book(self):
        new_book_info = self.mainWin.getNewBookInfo()

        if self.database and new_book_info:
            try:
                self.database.add_book(*new_book_info)
            except Exception as e:
                print(e)
            else:
                self.update_book_table(keys=self.book_search_keys)

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
                self.database.update_book(*new_book_info)
            except Exception as e:
                print(e)
            else:
                self.update_book_table(keys=self.book_search_keys)

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
                    self.update_book_table(keys=self.book_search_keys)
                else:
                    pass

    def update_buyer_table(self, keys, page_num=1):
        if self.database:
            offset = (page_num - 1) * 20
            # buy_id, buy_date, b_id, b_name, u_id, u_name
            table = self.database.search_buyer(*keys, limit=20, offset=offset)
            if table:
                self.mainWin.updateBuyerTable(table)
        else:
            QMessageBox.warning(self.mainWin, '警告', '请先链接至数据库！')

    def update_top_buyer_table(self):
        if self.database:
            table = self.database.get_top_buyers()
            if table:
                self.mainWin.updateBookFanTable(table)
        else:
            QMessageBox.warning(self.mainWin, '警告', '请先链接至数据库！')

    def update_top_book_table(self):
        if self.database:
            table = self.database.get_top_books()
            if table:
                self.mainWin.updateBestSellerTable(table)
        else:
            QMessageBox.warning(self.mainWin, '警告', '请先链接至数据库！')

    def search_buyer(self):
        self.buyer_search_keys = self.mainWin.getBuyerSearchKey()
        if not self.buyer_search_keys:
            return
        total_num = self.database.get_buyer_num(*self.buyer_search_keys)
        total_page = math.ceil(total_num / 20)
        self.mainWin.setTotalPage('buyer', total_page)
        self.mainWin.showBuyerNum(total_num)
        self.update_buyer_table(keys=self.buyer_search_keys)

    def update_paper_table(self, keys, page_num=1):
        if self.database:
            offset = (page_num - 1) * 20

            table = self.database.search_document(*keys, limit=20, offset=offset)
            if table:
                self.mainWin.updatePaperTable(table)
        else:
            QMessageBox.warning(self.mainWin, '警告', '请先链接至数据库！')

    def search_paper(self):
        self.paper_search_keys = self.mainWin.getPaperSearchKey()
        if not self.paper_search_keys:
            return
        total_num = self.database.get_document_num(*self.paper_search_keys)
        total_page = math.ceil(total_num / 20)
        self.mainWin.setTotalPage('paper', total_page)
        self.mainWin.showPaperNum(total_num)
        self.update_paper_table(keys=self.paper_search_keys)

    def add_paper(self):
        new_paper_info = self.mainWin.getNewPaperInfo()

        if self.database:
            try:
                self.database.add_paper(new_paper_info)
            except Exception as e:
                print(e)
            else:
                self.update_paper_table(keys=self.paper_search_keys)

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
        if self.database and new_paper_info:
            try:
                self.database.update_document(*new_paper_info)
            except Exception as e:
                print(e)
            else:
                self.update_paper_table(keys=self.paper_search_keys)

        self.editPaperWin.close()

    def delete_paper(self):
        if self.database:
            try:
                old_paper_info = self.mainWin.getSelectedPaperInfo()
                id = old_paper_info[0]
            except:
                QMessageBox.warning(self.mainWin, '警告', '请先选择要删除的论文！')
            else:
                reply = QMessageBox.question(self.mainWin,
                                             '询问',
                                             '确定要删除该书籍吗？',
                                             QMessageBox.Yes | QMessageBox.No,
                                             QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.database.delete_document(id)
                    QMessageBox.information(self.mainWin, '提示', '删除成功！')
                    self.update_paper_table(keys=self.paper_search_keys)
                else:
                    pass

    def update_upload_table(self, keys, page_num=1):
        if self.database:
            offset = (page_num - 1) * 20
            table = self.database.search_upload(*keys, limit=20, offset=offset)
            if table:
                self.mainWin.updateUploadTable(table)
        else:
            QMessageBox.warning(self.mainWin, '警告', '请先链接至数据库！')

    def update_top_uploader_table(self):
        if self.database:
            table = self.database.get_top_uploaders()
            if table:
                self.mainWin.updateContributorTbl(table)
        else:
            QMessageBox.warning(self.mainWin, '警告', '请先链接至数据库！')

    def search_upload(self):
        self.upload_search_keys = self.mainWin.getUploadSearchKey()
        if not self.upload_search_keys:
            return
        total_num = self.database.get_upload_num(*self.upload_search_keys)
        total_page = math.ceil(total_num / 20)
        self.mainWin.setTotalPage('upload', total_page)
        self.mainWin.showUploadNum(total_num)
        self.update_upload_table(keys=self.upload_search_keys)

    def update_user_table(self, keys, page_num=1):
        if self.database:
            offset = (page_num - 1) * 20
            table = self.database.search_user(*keys, limit=20, offset=offset)
            if table:
                self.mainWin.updateUserTable(table)
        else:
            QMessageBox.warning(self.mainWin, '警告', '请先链接至数据库！')

    def search_user(self):
        self.user_search_keys = self.mainWin.getUserSearchKey()
        if not self.user_search_keys:
            return
        total_num = self.database.get_user_num(*self.user_search_keys)
        total_page = math.ceil(total_num / 20)
        self.mainWin.setTotalPage('user', total_page)
        self.mainWin.showUserNum(total_num)
        self.update_user_table(keys=self.user_search_keys)

    def add_user(self):
        new_user_info = self.mainWin.getNewUserInfo()

        if self.database and new_user_info:
            try:
                self.database.add_user(new_user_info)
            except Exception as e:
                print(e)
            else:
                self.update_user_table(keys=self.user_search_keys)

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
        if self.database and new_user_info:
            try:
                self.database.update_user(*new_user_info)
            except Exception as e:
                print(e)
            else:
                self.update_user_table(keys=self.user_search_keys)

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
                    self.update_user_table(keys=self.user_search_keys)
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
            self.update_book_table(keys=self.book_search_keys, page_num=int(cur_page))
        elif type == 'paper':
            self.mainWin.paperPage.setText('{} / {}'.format(cur_page, total_page))
            self.update_paper_table(keys=self.paper_search_keys, page_num=int(cur_page))
        elif type == 'user':
            self.mainWin.userPage.setText('{} / {}'.format(cur_page, total_page))
            self.update_user_table(keys=self.user_search_keys, page_num=int(cur_page))
        elif type == 'buyer':
            self.mainWin.buyerPage.setText('{} / {}'.format(cur_page, total_page))
            self.update_buyer_table(keys=self.buyer_search_keys, page_num=int(cur_page))
        elif type == 'upload':
            self.mainWin.uploadPage.setText('{} / {}'.format(cur_page, total_page))
            self.update_upload_table(keys=self.upload_search_keys, page_num=int(cur_page))
        else:
            QMessageBox.critical(self.mainWin, '错误', '未知数据类型！')
            return


if __name__ == '__main__':
    app = QApplication([])
    admin = Admin()
    admin.mainWin.show()
    sys.exit(app.exec())
