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

        self.close_flag = True  # 区分关闭窗体和登录

        self.initSignalSlots()

    def initSignalSlots(self):
        self.toLoginBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.toRegisterBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

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

        self.close_flag = True

        self.bookTbl.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.paperTbl.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.bookTbl.setColumnHidden(0, True)  # 隐藏primary key

        self.initSignalSlots()

    def initSignalSlots(self):
        self.toHomeBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.toSearchBookBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.toSearchPaperBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.aboutBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
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

    def getSelectedBookInfo(self):
        row = self.bookTbl.currentRow()

        id = self.bookTbl.item(row, 0)  # primary key, hidden
        name = self.bookTbl.item(row, 1).text()
        author = self.bookTbl.item(row, 2).text()
        press = self.bookTbl.item(row, 3).text()
        release_date = self.bookTbl.item(row, 4).text()
        ISBN = self.bookTbl.item(row, 5).text()

        return id, name, author, press, release_date, ISBN

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
