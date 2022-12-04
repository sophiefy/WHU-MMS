# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\2022-2023大三上学习笔记\数据库系统\WHU-MMS\client\frontend\loginWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormLogin(object):
    def setupUi(self, FormLogin):
        FormLogin.setObjectName("FormLogin")
        FormLogin.resize(900, 600)
        FormLogin.setMinimumSize(QtCore.QSize(900, 600))
        FormLogin.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        FormLogin.setFont(font)
        FormLogin.setStyleSheet("#FormLogin{border-image: url(:/resources/common/bg.png);}")
        self.verticalLayout = QtWidgets.QVBoxLayout(FormLogin)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(FormLogin)
        self.stackedWidget.setStyleSheet("background-color: rgba(245, 245, 245, 100);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageLogin = QtWidgets.QWidget()
        self.pageLogin.setObjectName("pageLogin")
        self.gridLayout = QtWidgets.QGridLayout(self.pageLogin)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.pageLogin)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.loginNumEdit = QtWidgets.QLineEdit(self.pageLogin)
        self.loginNumEdit.setMinimumSize(QtCore.QSize(300, 50))
        self.loginNumEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.loginNumEdit.setFont(font)
        self.loginNumEdit.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.loginNumEdit.setObjectName("loginNumEdit")
        self.verticalLayout_2.addWidget(self.loginNumEdit)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 3, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.pageLogin)
        self.label.setMinimumSize(QtCore.QSize(400, 400))
        self.label.setMaximumSize(QtCore.QSize(400, 400))
        self.label.setStyleSheet("border-image: url(:/resources/common/login.png);\n"
"\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 4, 1)
        spacerItem2 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 5, 1, 1)
        self.toRegisterBtn = QtWidgets.QPushButton(self.pageLogin)
        self.toRegisterBtn.setMinimumSize(QtCore.QSize(300, 30))
        self.toRegisterBtn.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toRegisterBtn.setFont(font)
        self.toRegisterBtn.setStyleSheet("text-align: left;\n"
"color: rgb(0, 170, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.toRegisterBtn.setObjectName("toRegisterBtn")
        self.gridLayout.addWidget(self.toRegisterBtn, 5, 3, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.pageLogin)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.loginPasswordEdit = QtWidgets.QLineEdit(self.pageLogin)
        self.loginPasswordEdit.setMinimumSize(QtCore.QSize(300, 50))
        self.loginPasswordEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.loginPasswordEdit.setFont(font)
        self.loginPasswordEdit.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.loginPasswordEdit.setInputMask("")
        self.loginPasswordEdit.setText("")
        self.loginPasswordEdit.setMaxLength(32767)
        self.loginPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginPasswordEdit.setObjectName("loginPasswordEdit")
        self.verticalLayout_3.addWidget(self.loginPasswordEdit)
        self.gridLayout.addLayout(self.verticalLayout_3, 4, 3, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.pageLogin)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 5, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.loginBtn = QtWidgets.QPushButton(self.pageLogin)
        self.loginBtn.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.loginBtn.setFont(font)
        self.loginBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.loginBtn.setObjectName("loginBtn")
        self.verticalLayout_4.addWidget(self.loginBtn)
        self.gridLayout.addLayout(self.verticalLayout_4, 6, 3, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 2, 3, 1, 1)
        self.stackedWidget.addWidget(self.pageLogin)
        self.pageRegister = QtWidgets.QWidget()
        self.pageRegister.setObjectName("pageRegister")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.pageRegister)
        self.verticalLayout_6.setContentsMargins(50, -1, 50, -1)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(20, 99, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem6)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(50)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.pageRegister)
        self.label_5.setMinimumSize(QtCore.QSize(100, 0))
        self.label_5.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.regNameEdit = QtWidgets.QLineEdit(self.pageRegister)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.regNameEdit.setFont(font)
        self.regNameEdit.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.regNameEdit.setObjectName("regNameEdit")
        self.horizontalLayout.addWidget(self.regNameEdit)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.pageRegister)
        self.label_6.setMinimumSize(QtCore.QSize(100, 0))
        self.label_6.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.regPasswordEdit = QtWidgets.QLineEdit(self.pageRegister)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.regPasswordEdit.setFont(font)
        self.regPasswordEdit.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.regPasswordEdit.setObjectName("regPasswordEdit")
        self.horizontalLayout_2.addWidget(self.regPasswordEdit)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.pageRegister)
        self.label_7.setMinimumSize(QtCore.QSize(100, 0))
        self.label_7.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.regPhoneEdit = QtWidgets.QLineEdit(self.pageRegister)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.regPhoneEdit.setFont(font)
        self.regPhoneEdit.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.regPhoneEdit.setObjectName("regPhoneEdit")
        self.horizontalLayout_3.addWidget(self.regPhoneEdit)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 3)
        self.toLoginBtn = QtWidgets.QPushButton(self.pageRegister)
        self.toLoginBtn.setMinimumSize(QtCore.QSize(300, 30))
        self.toLoginBtn.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toLoginBtn.setFont(font)
        self.toLoginBtn.setStyleSheet("color: rgb(0, 170, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.toLoginBtn.setObjectName("toLoginBtn")
        self.gridLayout_2.addWidget(self.toLoginBtn, 1, 0, 1, 3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 2, 0, 1, 1)
        self.registerBtn = QtWidgets.QPushButton(self.pageRegister)
        self.registerBtn.setMinimumSize(QtCore.QSize(300, 60))
        self.registerBtn.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.registerBtn.setFont(font)
        self.registerBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.registerBtn.setObjectName("registerBtn")
        self.gridLayout_2.addWidget(self.registerBtn, 2, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 2, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 99, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem9)
        self.stackedWidget.addWidget(self.pageRegister)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(FormLogin)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FormLogin)

    def retranslateUi(self, FormLogin):
        _translate = QtCore.QCoreApplication.translate
        FormLogin.setWindowTitle(_translate("FormLogin", "Log in"))
        self.label_2.setText(_translate("FormLogin", "读者号"))
        self.toRegisterBtn.setText(_translate("FormLogin", "点我注册"))
        self.label_3.setText(_translate("FormLogin", "密码"))
        self.label_4.setText(_translate("FormLogin", "Welcome to WHU MMS!"))
        self.loginBtn.setText(_translate("FormLogin", "登          录"))
        self.label_5.setText(_translate("FormLogin", "用户名"))
        self.label_6.setText(_translate("FormLogin", "密码"))
        self.label_7.setText(_translate("FormLogin", "电话"))
        self.toLoginBtn.setText(_translate("FormLogin", "返回登录界面"))
        self.registerBtn.setText(_translate("FormLogin", "注          册"))
import resources_rc
