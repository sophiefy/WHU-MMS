# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editPaperWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormEditPaper(object):
    def setupUi(self, FormEditPaper):
        FormEditPaper.setObjectName("FormEditPaper")
        FormEditPaper.resize(976, 644)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        FormEditPaper.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(FormEditPaper)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(FormEditPaper)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.paperTitleEdit = QtWidgets.QLineEdit(FormEditPaper)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.paperTitleEdit.setFont(font)
        self.paperTitleEdit.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"")
        self.paperTitleEdit.setObjectName("paperTitleEdit")
        self.gridLayout.addWidget(self.paperTitleEdit, 0, 2, 1, 2)
        self.label_8 = QtWidgets.QLabel(FormEditPaper)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.paperAuthorEdit = QtWidgets.QLineEdit(FormEditPaper)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.paperAuthorEdit.setFont(font)
        self.paperAuthorEdit.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"")
        self.paperAuthorEdit.setObjectName("paperAuthorEdit")
        self.gridLayout.addWidget(self.paperAuthorEdit, 1, 2, 1, 2)
        self.label_9 = QtWidgets.QLabel(FormEditPaper)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.paperInsEdit = QtWidgets.QLineEdit(FormEditPaper)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.paperInsEdit.setFont(font)
        self.paperInsEdit.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"")
        self.paperInsEdit.setObjectName("paperInsEdit")
        self.gridLayout.addWidget(self.paperInsEdit, 2, 2, 1, 2)
        self.label_10 = QtWidgets.QLabel(FormEditPaper)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.paperDateEdit = QtWidgets.QLineEdit(FormEditPaper)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.paperDateEdit.setFont(font)
        self.paperDateEdit.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"")
        self.paperDateEdit.setObjectName("paperDateEdit")
        self.gridLayout.addWidget(self.paperDateEdit, 3, 2, 1, 2)
        self.label_11 = QtWidgets.QLabel(FormEditPaper)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)
        self.paperConfEdit = QtWidgets.QLineEdit(FormEditPaper)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.paperConfEdit.setFont(font)
        self.paperConfEdit.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"")
        self.paperConfEdit.setObjectName("paperConfEdit")
        self.gridLayout.addWidget(self.paperConfEdit, 4, 2, 1, 2)
        self.label_13 = QtWidgets.QLabel(FormEditPaper)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(FormEditPaper)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)
        self.paperCombo = QtWidgets.QComboBox(FormEditPaper)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.paperCombo.setFont(font)
        self.paperCombo.setObjectName("paperCombo")
        self.gridLayout.addWidget(self.paperCombo, 6, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(756, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 3, 1, 1)
        self.paperEditBtn = QtWidgets.QPushButton(FormEditPaper)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.paperEditBtn.setFont(font)
        self.paperEditBtn.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"background-color: rgb(85, 255, 127);")
        self.paperEditBtn.setObjectName("paperEditBtn")
        self.gridLayout.addWidget(self.paperEditBtn, 7, 0, 1, 2)
        self.paperDOIEdit = QtWidgets.QLineEdit(FormEditPaper)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.paperDOIEdit.setFont(font)
        self.paperDOIEdit.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"")
        self.paperDOIEdit.setObjectName("paperDOIEdit")
        self.gridLayout.addWidget(self.paperDOIEdit, 5, 2, 1, 2)

        self.retranslateUi(FormEditPaper)
        QtCore.QMetaObject.connectSlotsByName(FormEditPaper)

    def retranslateUi(self, FormEditPaper):
        _translate = QtCore.QCoreApplication.translate
        FormEditPaper.setWindowTitle(_translate("FormEditPaper", "编辑论文信息"))
        self.label_7.setText(_translate("FormEditPaper", "标题"))
        self.label_8.setText(_translate("FormEditPaper", "作者"))
        self.label_9.setText(_translate("FormEditPaper", "机构"))
        self.label_10.setText(_translate("FormEditPaper", "发表日期"))
        self.label_11.setText(_translate("FormEditPaper", "会议/期刊"))
        self.label_13.setText(_translate("FormEditPaper", "DIO"))
        self.label_12.setText(_translate("FormEditPaper", "类别"))
        self.paperEditBtn.setText(_translate("FormEditPaper", "确定"))
