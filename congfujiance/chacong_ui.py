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
        Form.resize(483, 477)
        Form.resize(504, 470)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 30, 81, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 100, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 160, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(280, 100, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 210, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(150, 260, 181, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 320, 411, 101))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 340, 61, 21))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(430, 380, 61, 21))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.tableWidget.setHorizontalHeaderLabels([u'文件名', u'重复率(%)'])
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1)
        self.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showDialog)
        self.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showDialog2)
        self.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start_check)
        self.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.export_excel)
        self.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clear_excel)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)




    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "九爪文件查重器", None))
        self.label.setText(_translate("Form", "文章查重器", None))
        self.pushButton.setText(_translate("Form", "选择文件夹", None))
        self.pushButton_2.setText(_translate("Form", "开始分析", None))
        self.label_2.setText(_translate("Form", "未选择文件夹", None))
        self.pushButton_3.setText(_translate("Form", "查看报告", None))
        self.pushButton_4.setText(_translate("Form", "导出报告", None))
        self.pushButton_5.setText(_translate("Form", "清空报告", None))


