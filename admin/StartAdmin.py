from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from frontend.mainWin import Ui_MainWindow
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
        self.database = None

        # initial signal slots
        self.mainWin.searchBookBtn.clicked.connect(self.update_book_table)
        self.mainWin.bookAddBtn.clicked.connect(self.add_book)

        self.create_connection('database/books.db')

    def create_connection(self, db_path):
        self.database = Database(db_path)
        self.database.create_connection()

    def update_book_table(self):
        if self.database:
            table = self.database.read_book()
            print('table: ', table)
            if table:
                self.mainWin.bookTbl.setRowCount(0)
                self.mainWin.bookTbl.clearContents()
                try:
                    for i, row in enumerate(table):
                        self.mainWin.bookTbl.insertRow(i)
                        self.mainWin.bookTbl.setItem(i, 0, QTableWidgetItem(row[0]))
                        self.mainWin.bookTbl.setItem(i, 1, QTableWidgetItem(row[1]))
                        self.mainWin.bookTbl.setItem(i, 2, QTableWidgetItem(row[2]))
                        self.mainWin.bookTbl.setItem(i, 3, QTableWidgetItem(row[3]))
                        self.mainWin.bookTbl.setItem(i, 4, QTableWidgetItem(row[4]))
                except Exception as e:
                    print(e)

        else:
            QMessageBox.warning(self.mainWin, '警告', '请先链接至数据库！')

    def add_book(self):
        name, author, press, release_date, ISBN = self.mainWin.getNewBookInfo()

        # 2022年11月23日 -> 2022-11-23
        # release_date = release_date.replace('年', '-').replace('月', '-').replace('日', '')
        if self.database:
            try:
                self.database.add_book(name, author, press, release_date, ISBN)
            except Exception as e:
                print(e)
            else:
                self.update_book_table()



if __name__ == '__main__':
    app = QApplication([])
    admin = Admin()
    admin.mainWin.show()
    sys.exit(app.exec())
