import traceback

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from frontend.mainWin import Ui_MainWindow
from frontend.editBookWin import Ui_FormEditBook
from backend.CRUD import Database


class MainWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWin, self).__init__()

        self.setupUi(self)

        self.initSignalSlots()

        self.bookTbl.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.paperTbl.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

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

    def getNewBookInfo(self):
        name = self.bookNameEdit.text()
        author = self.bookNameEdit.text()
        press = self.bookPressEdit.text()
        release_date = self.bookDateEdit.text()
        ISBN = self.bookISBNEdit.text()

        return name, author, press, release_date, ISBN

    def getSelectedBookInfo(self):
        row = self.bookTbl.currentRow()
        name = self.bookTbl.item(row, 0).text()
        author = self.bookTbl.item(row, 1).text()
        press = self.bookTbl.item(row, 2).text()
        release_date = self.bookTbl.item(row, 3).text()
        ISBN = self.bookTbl.item(row, 4).text()

        return name, author, press, release_date, ISBN

    def updateBookTable(self, table):
        assert table is not None
        self.bookTbl.setRowCount(0)  # TODO: 全部刷新太费资源，考虑按照一定顺序插入
        self.bookTbl.clearContents()
        try:
            for i, row in enumerate(table):
                self.bookTbl.insertRow(i)
                self.bookTbl.setItem(i, 0, QTableWidgetItem(row[0]))
                self.bookTbl.setItem(i, 1, QTableWidgetItem(row[1]))
                self.bookTbl.setItem(i, 2, QTableWidgetItem(row[2]))
                self.bookTbl.setItem(i, 3, QTableWidgetItem(row[3]))
                self.bookTbl.setItem(i, 4, QTableWidgetItem(row[4]))
        except Exception as e:
            print(e)

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


class EditBookWin(QDialog, Ui_FormEditBook):
    def __init__(self):
        super(EditBookWin, self).__init__()

        self.setupUi(self)

    def putOldBookInfo(self, row):
        name, author, press, release_date, ISBN = row[0], row[1], row[2], row[3], row[4]
        self.bookNameEdit.setText(name)
        self.bookAuthorEdit.setText(author)
        self.bookPressEdit.setText(press)
        self.bookDateEdit.setText(release_date)
        self.bookISBNEdit.setText(ISBN)

    def getNewBookInfo(self):
        name = self.bookNameEdit.text()
        author = self.bookAuthorEdit.text()
        press = self.bookPressEdit.text()
        release_date = self.bookDateEdit.text()
        ISBN = self.bookISBNEdit.text()

        return name, author, press, release_date, ISBN


class Admin:
    def __init__(self):
        self.mainWin = MainWin()
        self.editBookWin = EditBookWin()
        self.database = None

        # initial signal slots
        self.mainWin.searchBookBtn.clicked.connect(self.update_book_table)
        self.mainWin.bookAddBtn.clicked.connect(self.add_book)
        self.mainWin.bookEditBtn.clicked.connect(self.edit_book)
        self.mainWin.bookDeleteBtn.clicked.connect(self.delete_book)

        self.editBookWin.bookAddBtn.clicked.connect(self.confirm_edit_book)

        self.create_connection('database/books.db')

    def create_connection(self, db_path):
        self.database = Database(db_path)
        self.database.create_connection()

    def update_book_table(self):
        if self.database:
            table = self.database.read_book()
            print('table: ', table)
            if table:
                self.mainWin.updateBookTable(table)
        else:
            QMessageBox.warning(self.mainWin, '警告', '请先链接至数据库！')

    def add_book(self):
        name, author, press, release_date, ISBN = self.mainWin.getNewBookInfo()

        if self.database:
            try:
                self.database.add_book(name, author, press, release_date, ISBN)
            except Exception as e:
                print(e)
            else:
                self.update_book_table()

    def edit_book(self):
        try:
            row = self.mainWin.getSelectedBookInfo()
        except:
            QMessageBox.warning(self.mainWin, '警告', '请先选择要编辑的书籍！')
        else:
            self.editBookWin.putOldBookInfo(row)
            self.editBookWin.exec()

    def confirm_edit_book(self):
        name, author, press, release_date, ISBN = self.editBookWin.getNewBookInfo()
        if self.database:
            try:
                self.database.update_book(name, author, press, release_date, ISBN)
            except Exception as e:
                print(e)
            else:
                self.update_book_table()

        self.editBookWin.close()

    def delete_book(self):
        if self.database:
            reply = QMessageBox.question(self.mainWin,
                                 '询问',
                                 '确定要删除该书籍吗？',
                                 QMessageBox.Yes | QMessageBox.No,
                                 QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    _, _, _, _, ISBN = self.mainWin.getSelectedBookInfo()
                except:
                    QMessageBox.warning(self.mainWin, '警告', '请先选择要删除的书籍！')
                else:
                    self.database.delete_book(ISBN)
                    self.update_book_table()
            else:
                pass



if __name__ == '__main__':
    app = QApplication([])
    admin = Admin()
    admin.mainWin.show()
    sys.exit(app.exec())
