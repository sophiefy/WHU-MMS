# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editUserWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormEditUser(object):
    def setupUi(self, FormEditUser):
        FormEditUser.setObjectName("FormEditUser")
        FormEditUser.resize(897, 621)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        FormEditUser.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(FormEditUser)
        self.gridLayout.setObjectName("gridLayout")
        self.label_21 = QtWidgets.QLabel(FormEditUser)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 0, 0, 1, 1)
        self.userNumEdit = QtWidgets.QLineEdit(FormEditUser)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.userNumEdit.setFont(font)
        self.userNumEdit.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"")
        self.userNumEdit.setReadOnly(True)
        self.userNumEdit.setObjectName("userNumEdit")
        self.gridLayout.addWidget(self.userNumEdit, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(FormEditUser)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 1, 0, 1, 1)
        self.userNameEdit = QtWidgets.QLineEdit(FormEditUser)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.userNameEdit.setFont(font)
        self.userNameEdit.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"")
        self.userNameEdit.setObjectName("userNameEdit")
        self.gridLayout.addWidget(self.userNameEdit, 1, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(FormEditUser)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 2, 0, 1, 1)
        self.userPasswordEdit = QtWidgets.QLineEdit(FormEditUser)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.userPasswordEdit.setFont(font)
        self.userPasswordEdit.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"")
        self.userPasswordEdit.setObjectName("userPasswordEdit")
        self.gridLayout.addWidget(self.userPasswordEdit, 2, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(FormEditUser)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 3, 0, 1, 1)
        self.userAgeEdit = QtWidgets.QLineEdit(FormEditUser)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.userAgeEdit.setFont(font)
        self.userAgeEdit.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"")
        self.userAgeEdit.setObjectName("userAgeEdit")
        self.gridLayout.addWidget(self.userAgeEdit, 3, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(FormEditUser)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 4, 0, 1, 1)
        self.userDPTEdit = QtWidgets.QLineEdit(FormEditUser)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.userDPTEdit.setFont(font)
        self.userDPTEdit.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"")
        self.userDPTEdit.setObjectName("userDPTEdit")
        self.gridLayout.addWidget(self.userDPTEdit, 4, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(FormEditUser)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 5, 0, 1, 1)
        self.userGradeEdit = QtWidgets.QLineEdit(FormEditUser)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.userGradeEdit.setFont(font)
        self.userGradeEdit.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"")
        self.userGradeEdit.setObjectName("userGradeEdit")
        self.gridLayout.addWidget(self.userGradeEdit, 5, 1, 1, 1)
        self.userEditBtn = QtWidgets.QPushButton(FormEditUser)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.userEditBtn.setFont(font)
        self.userEditBtn.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"background-color: rgb(85, 255, 127);")
        self.userEditBtn.setObjectName("userEditBtn")
        self.gridLayout.addWidget(self.userEditBtn, 6, 0, 1, 1)

        self.retranslateUi(FormEditUser)
        QtCore.QMetaObject.connectSlotsByName(FormEditUser)

    def retranslateUi(self, FormEditUser):
        _translate = QtCore.QCoreApplication.translate
        FormEditUser.setWindowTitle(_translate("FormEditUser", "编辑读者信息"))
        self.label_21.setText(_translate("FormEditUser", "读者号"))
        self.label_19.setText(_translate("FormEditUser", "用户名"))
        self.label_24.setText(_translate("FormEditUser", "密码"))
        self.label_25.setText(_translate("FormEditUser", "年龄"))
        self.label_26.setText(_translate("FormEditUser", "DPT"))
        self.label_27.setText(_translate("FormEditUser", "年级"))
        self.userEditBtn.setText(_translate("FormEditUser", "确定"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormEditUser = QtWidgets.QWidget()
    ui = Ui_FormEditUser()
    ui.setupUi(FormEditUser)
    FormEditUser.show()
    sys.exit(app.exec_())
