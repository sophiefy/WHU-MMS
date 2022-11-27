from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from mainWin import Ui_MainWindow
from editBookWin import Ui_FormEditBook
from editPaperWin import Ui_FormEditPaper
from editUserWin import Ui_FormEditUser

# NOTE: work in progress


class MainWin(QMainWindow, Ui_MainWindow):
    pageSignal = pyqtSignal(list)

    def __init__(self):
        super(MainWin, self).__init__()

        self.setupUi(self)

        self.initSignalSlots()

        self.bookTbl.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.paperTbl.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.userTbl.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def initSignalSlots(self):
        # NOTE: CRUD -> Create, Read, Update and Delete
        # menu bar
        self.actionHome.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.actionCbook.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.actionRbook.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.actionCpaper.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.actionRpaper.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.actionCuser.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.actionRuser.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        self.actionStats.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(7))

        # home page
        self.bookBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.paperBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.userBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        self.statsBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))

        self.bookFirstBtn.clicked.connect(lambda: self.firstPage('book'))
        self.bookPreBtn.clicked.connect(lambda: self.prePage('book'))
        self.bookNextBtn.clicked.connect(lambda: self.nextPage('book'))
        self.bookLastBtn.clicked.connect(lambda: self.lastPage('book'))
        self.bookJumpBtn.clicked.connect(lambda: self.jumpPage('book'))

        self.paperFirstBtn.clicked.connect(lambda: self.firstPage('paper'))
        self.paperPreBtn.clicked.connect(lambda: self.prePage('paper'))
        self.paperNextBtn.clicked.connect(lambda: self.nextPage('paper'))
        self.paperLastBtn.clicked.connect(lambda: self.lastPage('paper'))
        self.paperJumpBtn.clicked.connect(lambda: self.jumpPage('paper'))

        self.userFirstBtn.clicked.connect(lambda: self.firstPage('user'))
        self.userPreBtn.clicked.connect(lambda: self.prePage('user'))
        self.userNextBtn.clicked.connect(lambda: self.nextPage('user'))
        self.userLastBtn.clicked.connect(lambda: self.lastPage('user'))
        self.userJumpBtn.clicked.connect(lambda: self.jumpPage('user'))

        self.bookPage.setText('1 / 10')  # debug use

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

    def getNewPaperInfo(self):
        title = self.paperTitleEdit.text()
        author = self.paperAuthorEdit.text()
        institute = self.paperInsEdit.text()
        release_date = self.paperDateEdit.text()
        conference = self.paperConfEdit.text()
        DOI = self.paperDOIEdit.text()

        return title, author, institute, release_date, conference, DOI

    def getSelectedPaperInfo(self):
        row = self.paperTbl.currentRow()
        title = self.paperTbl.item(row, 0).text()
        author = self.paperTbl.item(row, 1).text()
        institute = self.paperTbl.item(row, 2).text()
        release_date = self.paperTbl.item(row, 3).text()
        conference = self.paperTbl.item(row, 4).text()
        DOI = self.paperTbl.item(row, 5).text()

        return title, author, institute, release_date, conference, DOI

    def updatePaperTable(self, table):
        assert table is not None
        self.paperTbl.setRowCount(0)  # TODO: 全部刷新太费资源，考虑按照一定顺序插入
        self.paperTbl.clearContents()
        try:
            for i, row in enumerate(table):
                self.paperTbl.insertRow(i)
                self.paperTbl.setItem(i, 0, QTableWidgetItem(row[0]))
                self.paperTbl.setItem(i, 1, QTableWidgetItem(row[1]))
                self.paperTbl.setItem(i, 2, QTableWidgetItem(row[2]))
                self.paperTbl.setItem(i, 3, QTableWidgetItem(row[3]))
                self.paperTbl.setItem(i, 4, QTableWidgetItem(row[4]))
                self.paperTbl.setItem(i, 5, QTableWidgetItem(row[4]))
        except Exception as e:
            print(e)

    def getNewUserInfo(self):
        name = self.userNameEdit.text()
        number = self.userNumEdit.text()
        password = self.userPasswordEdit.text()
        phone = self.userTelEdit.text()

        return name, number, password, phone

    def getSelectedUserInfo(self):
        row = self.userTbl.currentRow()
        name = self.userTbl.item(row, 0).text()
        number = self.userTbl.item(row, 1).text()
        password = self.userTbl.item(row, 3).text()
        phone = self.userTbl.item(row, 4).text()

        return name, number, password, phone

    def updateUserTable(self, table):
        assert table is not None
        self.userTbl.setRowCount(0)  # TODO: 全部刷新太费资源，考虑按照一定顺序插入
        self.userTbl.clearContents()
        try:
            for i, row in enumerate(table):
                self.userTbl.insertRow(i)
                self.userTbl.setItem(i, 0, QTableWidgetItem(row[0]))
                self.userTbl.setItem(i, 1, QTableWidgetItem(row[1]))
                self.userTbl.setItem(i, 2, QTableWidgetItem(row[2]))
                self.userTbl.setItem(i, 3, QTableWidgetItem(row[3]))
        except Exception as e:
            print(e)


    # SECTION: 翻页
    def firstPage(self, type):
        self.pageSignal.emit([type, 'first', self.curPage(type)])

    def lastPage(self, type):
        self.pageSignal.emit([type, 'last', self.curPage(type)])

    def prePage(self, type):
        self.pageSignal.emit([type, 'pre', self.curPage(type)])

    def nextPage(self, type):
        self.pageSignal.emit([type, 'next', self.curPage(type)])

    def jumpPage(self, type):
        self.pageSignal.emit([type, 'jump', self.targetPage(type)])

    def curPage(self, type):
        # text的格式为 'cur_page / total_page'
        if type == 'book':
            text = self.bookPage.text()
        elif type == 'paper':
            text = self.paperPage.text()
        elif type == 'user':
            text = self.userPage.text()
        else:
            QMessageBox.critical(self, '错误', '未知数据类型！')
            return

        cur_page = int(text.split('/')[0].strip(' '))
        return cur_page

    def totalPage(self, type):
        if type == 'book':
            text = self.bookPage.text()
        elif type == 'paper':
            text = self.paperPage.text()
        elif type == 'user':
            text = self.userPage.text()
        else:
            QMessageBox.critical(self, '错误', '未知数据类型！')
            return

        total_page = int(text.split('/')[1].strip(' '))
        return total_page

    def targetPage(self, type):
        if type == 'book':
            text = self.bookJumpEdit.text()
        elif type == 'paper':
            text = self.paperJumpEdit.text()
        elif type == 'user':
            text = self.userJumpEdit.text()
        else:
            QMessageBox.critical(self, '错误', '未知数据类型！')
            return

        target_page = int(text)
        return target_page

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


class EditPaperWin(QDialog, Ui_FormEditPaper):
    def __init__(self):
        super(EditPaperWin, self).__init__()

        self.setupUi(self)

    def putOldPaperInfo(self, row):
        title, author, institute, release_date, conference, DOI = \
            row[0], row[1], row[2], row[3], row[4], row[5]
        self.paperTitleEdit.setText(title)
        self.paperAuthorEdit.setText(author)
        self.paperInsEdit.setText(institute)
        self.paperDateEdit.setText(release_date)
        self.paperConfEdit.setText(conference)
        self.paperDOIEdit.setText(DOI)

    def getNewPaperInfo(self):
        title = self.paperTitleEdit.text()
        author = self.paperAuthorEdit.text()
        institute = self.paperInsEdit.text()
        release_date = self.paperDateEdit.text()
        conference = self.paperConfEdit.text()
        DOI = self.paperDOIEdit.text()

        return title, author, institute, release_date, conference, DOI


class EditUserWin(QDialog, Ui_FormEditUser):
    def __init__(self):
        super(EditUserWin, self).__init__()

        self.setupUi(self)

    def putOldUserInfo(self, row):
        name, password, phone, number = row[0], row[1], row[2], row[3]
        self.userNameEdit.setText(name)
        self.userPasswordEdit.setText(password)
        self.userTelEdit.setText(phone)
        self.userNameEdit.setText(number)

    def getNewUserInfo(self):
        name = self.userNameEdit.text()
        password = self.userPasswordEdit.text()
        phone = self.userTelEdit.text()
        number = self.userNumEdit.text()

        return name, password, phone, number
