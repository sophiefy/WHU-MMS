from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from loginWin import Ui_FormLogin
from mainWin import Ui_MainWindow
from uploadWin import Ui_FormUpload


class LoginWin(QDialog, Ui_FormLogin):
    def __init__(self):
        super(LoginWin, self).__init__()

        self.setupUi(self)

        self.stackedWidget.setCurrentIndex(0)

        self.close_flag = True  # 区分关闭窗体和登录

        self.initSignalSlots()

    def initSignalSlots(self):
        self.toLoginBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.toRegisterBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

    def showInfo(self, msg):
        QMessageBox.information(self, '提示', msg)

    def showWarning(self, msg):
        QMessageBox.warning(self, '警告', msg)

    def showError(self, msg):
        QMessageBox.critical(self, '错误', msg)

    def getLoginInfo(self):
        number = self.loginNumEdit.text()
        password = self.loginPasswordEdit.text()

        if number and password:
            return number, password
        else:
            return None

    def getRegisterInfo(self):
        name = self.regNameEdit.text()
        password = self.regPasswordEdit.text()
        age = self.regAgeEdit.text()
        dpt = self.regDPTEdit.text()
        grade = self.regGradeEdit.text()

        if name and password and age and dpt and grade:
            return name, password, age, dpt, grade
        else:
            self.showWarning('注册信息不全！')
            return None

    def closeEvent(self, e):
        if self.close_flag:
            sys.exit(0)
        else:
            self.close()


class MainWin(QMainWindow, Ui_MainWindow):
    pageSignal = pyqtSignal(list)

    def __init__(self):
        super(MainWin, self).__init__()

        self.setupUi(self)

        self.stackedWidget.setCurrentIndex(0)

        self.close_flag = True

        self.bookTbl.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.paperTbl.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.bookTbl.setColumnHidden(0, True)  # 隐藏primary key
        self.paperTbl.setColumnHidden(0, True)  # 隐藏primary key

        self.initSignalSlots()

    def initSignalSlots(self):
        self.toHomeBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.toSearchBookBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.toSearchPaperBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.toProfileBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.toAboutBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.bookBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.paperBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

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

        self.bookPage.setText('1 / 10')  # debug use

    def showInfo(self, msg):
        QMessageBox.information(self, '提示', msg)

    def showWarning(self, msg):
        QMessageBox.warning(self, '警告', msg)

    def showError(self, msg):
        QMessageBox.critical(self, '错误', msg)

    def getBookSearchKey(self):
        name = self.searchBookNameEdit.text()
        author = self.searchBookAuthorEdit.text()
        press = self.searchBookPressEdit.text()
        release_date = self.searchBookDateEdit.text()
        ISBN = self.searchBookISBNEdit.text()

        return name, author, press, release_date, ISBN

    def getSelectedBookInfo(self):
        row = self.bookTbl.currentRow()

        id = self.bookTbl.item(row, 0)  # primary key, hidden
        name = self.bookTbl.item(row, 1).text()
        author = self.bookTbl.item(row, 2).text()
        press = self.bookTbl.item(row, 3).text()
        release_date = self.bookTbl.item(row, 4).text()
        ISBN = self.bookTbl.item(row, 5).text()
        stock = self.bookTbl.item(row, 6).text()

        return id, name, author, press, release_date, ISBN, stock

    def showBookNum(self, num):
        if num:
            self.bookNumLbl.setText(f'查询结果：共{num}条数据')
        else:
            self.bookNumLbl.setText(f'查询结果：共0条数据')

    def updateBookTable(self, table):
        assert table is not None
        self.bookTbl.setRowCount(0)  # TODO: 全部刷新太费资源，考虑按照一定顺序插入
        self.bookTbl.clearContents()
        try:
            for i, row in enumerate(table):
                # id, name, author, press, release_date, ISBN, stock
                self.bookTbl.insertRow(i)
                self.bookTbl.setItem(i, 0, QTableWidgetItem(str(row[0])))
                self.bookTbl.setItem(i, 1, QTableWidgetItem(row[1]))
                self.bookTbl.setItem(i, 2, QTableWidgetItem(row[2]))
                self.bookTbl.setItem(i, 3, QTableWidgetItem(row[3]))
                self.bookTbl.setItem(i, 4, QTableWidgetItem(str(row[4])))
                self.bookTbl.setItem(i, 5, QTableWidgetItem(row[5]))
                self.bookTbl.setItem(i, 6, QTableWidgetItem(str(row[6])))
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

    def getPaperSearchKey(self):
        title = self.searchPaperTitleEdit.text()
        author = self.searchPaperAuthorEdit.text()
        release_date = self.searchPaperDateEdit.text()
        archive = self.searchPaperArchiveEdit.text()

        return title, author, release_date, archive

    def getSelectedPaperInfo(self):
        row = self.paperTbl.currentRow()

        id = self.paperTbl.item(row, 0).text()  # primary_key
        title = self.paperTbl.item(row, 1).text()
        author = self.paperTbl.item(row, 2).text()
        release_date = self.paperTbl.item(row, 3).text()
        archive = self.paperTbl.item(row, 4).text()
        url = self.paperTbl.item(row, 5).text()

        return id, title, author, release_date, archive, url

    def showPaperNum(self, num):
        if num:
            self.paperNumLbl.setText(f'查询结果：共{num}条数据')
        else:
            self.paperNumLbl.setText(f'查询结果：共0条数据')

    def updatePaperTable(self, table):
        assert table is not None
        self.paperTbl.setRowCount(0)  # TODO: 全部刷新太费资源，考虑按照一定顺序插入
        self.paperTbl.clearContents()
        try:
            for i, row in enumerate(table):
                # id, title, author, release_date, archive, url
                self.paperTbl.insertRow(i)
                self.paperTbl.setItem(i, 0, QTableWidgetItem(str(row[0])))
                self.paperTbl.setItem(i, 1, QTableWidgetItem(row[1]))
                self.paperTbl.setItem(i, 2, QTableWidgetItem(row[2]))
                self.paperTbl.setItem(i, 3, QTableWidgetItem(str(row[3])))
                self.paperTbl.setItem(i, 4, QTableWidgetItem(row[4]))
                self.paperTbl.setItem(i, 5, QTableWidgetItem(row[5]))
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
        else:
            QMessageBox.critical(self, '错误', '未知数据类型！')
            return

        total_page = int(text.split('/')[1].strip(' '))
        return total_page

    def setTotalPage(self, total_page):


    def targetPage(self, type):
        if type == 'book':
            text = self.bookJumpEdit.text()
        elif type == 'paper':
            text = self.paperJumpEdit.text()
        else:
            QMessageBox.critical(self, '错误', '未知数据类型！')
            return
        try:
            target_page = int(text)
        except:
            return -1  # 输入了非法页码

        return target_page

    def closeEvent(self, e):
        if self.close_flag:
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
        else:
            self.close()


class UploadWin(QDialog, Ui_FormUpload):
    def __init__(self):
        super(UploadWin, self).__init__()

        self.setupUi(self)

    def getNewPaperInfo(self):
        title = self.paperTitleEdit.text()
        author = self.paperAuthorEdit.text()
        release_date = self.paperDateEdit.text()
        archive = self.paperArchiveEdit.text()
        url = self.paperURLEdit.text()

        if title and author and release_date and archive and url:
            # TODO: 后端要检查是否可以插入，并返回信息给用户
            return title, author, release_date, archive, url
        else:
            self.showWarning('论文信息不全！')
            return None
