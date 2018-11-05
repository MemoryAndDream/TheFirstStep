# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chacong_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(180, 30, 81, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 90, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 150, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(260, 90, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
       # self.label_3 = QtGui.QLabel(Form)
       # self.label_3.setGeometry(QtCore.QRect(190, 210, 54, 12))
        #self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pbar = QtGui.QProgressBar(self)               # 构建 QProgressBar
        self.pbar.setGeometry(140, 210, 171, 21)

        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 270, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showDialog)
        self.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showDialog2)
        self.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start_check)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "文章查重器", None))
        self.pushButton.setText(_translate("Form", "选择文件夹", None))
        self.pushButton_2.setText(_translate("Form", "开始分析", None))
        self.label_2.setText(_translate("Form", "未选择文件夹", None))
        self.pushButton_3.setText(_translate("Form", "查看报告", None))
      #  self.label_3.setText(_translate("Form", "。。。", None))

