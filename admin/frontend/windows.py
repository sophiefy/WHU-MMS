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

    def showInfo(self, msg):
        QMessageBox.information(self, '提示', msg)

    def showWarning(self, msg):
        QMessageBox.warning(self, '警告', msg)

    def showError(self, msg):
        QMessageBox.critical(self, '错误', msg)

    def getNewBookInfo(self):
        name = self.bookNameEdit.text()
        author = self.bookNameEdit.text()
        press = self.bookPressEdit.text()
        release_date = self.bookDateEdit.text()
        ISBN = self.bookISBNEdit.text()
        stock = self.bookStockEdit.text()
        if name and author and press and release_date and ISBN and stock:
            # TODO: 可以加入格式检查
            return name, author, press, release_date, ISBN
        else:
            self.showWarning('书本信息不完整!')
            return None

    def getSelectedBookInfo(self):
        row = self.bookTbl.currentRow()

        id = self.bookTbl.item(row, 0)  # primary key
        name = self.bookTbl.item(row, 1).text()
        author = self.bookTbl.item(row, 2).text()
        press = self.bookTbl.item(row, 3).text()
        release_date = self.bookTbl.item(row, 4).text()
        ISBN = self.bookTbl.item(row, 5).text()
        stock = self.bookTbl.item(row, 6).text()  # 在库

        return id, name, author, press, release_date, ISBN, stock

    def updateBookTable(self, table):
        assert table is not None
        self.bookTbl.setRowCount(0)  # TODO: 全部刷新太费资源，考虑按照一定顺序插入
        self.bookTbl.clearContents()
        try:
            for i, row in enumerate(table):
                # id, name, author, press, release_date, ISBN, stock
                self.bookTbl.insertRow(i)
                self.bookTbl.setItem(i, 0, QTableWidgetItem(row[0]))
                self.bookTbl.setItem(i, 1, QTableWidgetItem(row[1]))
                self.bookTbl.setItem(i, 2, QTableWidgetItem(row[2]))
                self.bookTbl.setItem(i, 3, QTableWidgetItem(row[3]))
                self.bookTbl.setItem(i, 4, QTableWidgetItem(row[4]))
                self.bookTbl.setItem(i, 5, QTableWidgetItem(row[4]))
                self.bookTbl.setItem(i, 6, QTableWidgetItem(row[4]))
        except Exception as e:
            print(e)

    def getNewPaperInfo(self):
        title = self.paperTitleEdit.text()  # 论文标题
        author = self.paperAuthorEdit.text()  # 论文作者
        release_date = self.paperDateEdit.text()  # 发表日期
        archive = self.paperArchiveEdit.text()  # 发表平台
        url = self.paperURLEdit.text()  # 论文地址
        if title and author and release_date and archive and url:
            return title, author, release_date, archive, url
        else:
            self.showWarning('论文信息不全！')
            return None

    def getSelectedPaperInfo(self):
        row = self.paperTbl.currentRow()

        id = self.paperTbl.item(row, 0).text()  # primary_key
        title = self.paperTbl.item(row, 1).text()
        author = self.paperTbl.item(row, 2).text()
        release_date = self.paperTbl.item(row, 3).text()
        archive = self.paperTbl.item(row, 4).text()
        url = self.paperTbl.item(row, 5).text()

        return id, title, author, release_date, archive, url

    def updatePaperTable(self, table):
        assert table is not None
        self.paperTbl.setRowCount(0)  # TODO: 全部刷新太费资源，考虑按照一定顺序插入
        self.paperTbl.clearContents()
        try:
            for i, row in enumerate(table):
                # title, author, release_date, archive, url, primary_key
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
        password = self.userPasswordEdit.text()
        age = self.userAgeEdit.text()
        dpt = self.userDPTEdit.text()
        grade = self.userGradeEdit.text()

        if name and password and age and dpt and grade:
            return name, password, age, dpt, grade
        else:
            self.showWarning('用户信息不全！')

    def getSelectedUserInfo(self):
        row = self.userTbl.currentRow()

        number = self.userTbl.item(row, 0).text()
        name = self.userTbl.item(row, 1).text()
        password = self.userTbl.item(row, 2).text()
        age = self.userTbl.item(row, 3).text()
        dpt = self.userTbl.item(row, 4).text()
        grade = self.userTbl.item(row, 5).text()

        return number, name, password, age, dpt, grade

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
                self.userTbl.setItem(i, 4, QTableWidgetItem(row[4]))
                self.userTbl.setItem(i, 5, QTableWidgetItem(row[5]))
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

        try:
            target_page = int(text)
        except:
            return -1  # 输入了非法页码

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

    def showInfo(self, msg):
        QMessageBox.information(self, '提示', msg)

    def showWarning(self, msg):
        QMessageBox.warning(self, '警告', msg)

    def showError(self, msg):
        QMessageBox.critical(self, '错误', msg)

    def putOldBookInfo(self, row):
        id, name, author, press, release_date, ISBN, stock = \
            row[0], row[1], row[2], row[3], row[4], row[5], row[6]

        self.bookKeyEdit.setText(id)
        self.bookNameEdit.setText(name)
        self.bookAuthorEdit.setText(author)
        self.bookPressEdit.setText(press)
        self.bookDateEdit.setText(release_date)
        self.bookISBNEdit.setText(ISBN)
        self.bookStockEdit.setText(stock)

    def getNewBookInfo(self):
        id = self.bookKeyEdit.text()
        name = self.bookNameEdit.text()
        author = self.bookAuthorEdit.text()
        press = self.bookPressEdit.text()
        release_date = self.bookDateEdit.text()
        ISBN = self.bookISBNEdit.text()
        stock = self.bookStockEdit.text()
        if id and name and author and press and release_date and ISBN and stock:
            return id, name, author, press, release_date, ISBN, stock
        else:
            self.showWarning('书本信息不完整!')
            return None


class EditPaperWin(QDialog, Ui_FormEditPaper):
    def __init__(self):
        super(EditPaperWin, self).__init__()

        self.setupUi(self)

    def showInfo(self, msg):
        QMessageBox.information(self, '提示', msg)

    def showWarning(self, msg):
        QMessageBox.warning(self, '警告', msg)

    def showError(self, msg):
        QMessageBox.critical(self, '错误', msg)

    def putOldPaperInfo(self, row):
        id, title, author, release_date, archive, url, primary_key = \
            row[0], row[1], row[2], row[3], row[4], row[5], row[6]

        self.paperKeyEdit.setText(id)
        self.paperTitleEdit.setText(title)
        self.paperAuthorEdit.setText(author)
        self.paperDateEdit.setText(release_date)
        self.paperArchiveEdit.setText(archive)
        self.paperURLEdit.setText(url)

    def getNewPaperInfo(self):
        id = self.paperKeyEdit.text()
        title = self.paperTitleEdit.text()
        author = self.paperAuthorEdit.text()
        release_date = self.paperDateEdit.text()
        archive = self.paperArchiveEdit.text()
        url = self.paperURLEdit.text()

        if id and title and author and release_date and archive and url:
            return id, title, author, release_date, archive, url
        else:
            self.showWarning('论文信息不全！')
            return None


class EditUserWin(QDialog, Ui_FormEditUser):
    def __init__(self):
        super(EditUserWin, self).__init__()

        self.setupUi(self)

    def showInfo(self, msg):
        QMessageBox.information(self, '提示', msg)

    def showWarning(self, msg):
        QMessageBox.warning(self, '警告', msg)

    def showError(self, msg):
        QMessageBox.critical(self, '错误', msg)

    def putOldUserInfo(self, row):
        number, name, password, age, dpt, grade = \
            row[0], row[1], row[2], row[3], row[4], row[5]
        self.userNumEdit.setText(number)
        self.userNameEdit.setText(name)
        self.userPasswordEdit.setText(password)
        self.userAgeEdit.setText(age)
        self.userDPTEdit.setText(dpt)
        self.userGradeEdit.setText(grade)

    def getNewUserInfo(self):
        number = self.userNumEdit.text()
        name = self.userNameEdit.text()
        password = self.userPasswordEdit.text()
        age = self.userAgeEdit.text()
        dpt = self.userDPTEdit.text()
        grade = self.userGradeEdit.text()

        if number and name and password and age and dpt and grade:
            return number, name, password, age, dpt, grade
        else:
            self.showWarning('用户信息不全！')
            return None
