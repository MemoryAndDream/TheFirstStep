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
        Form.resize(740, 594)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 190, 761, 411))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 50, 125, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))


        self.pushButton_7 = QtGui.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(125, 50, 125, 61))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))

        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 50, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 50, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 110, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(370, 110, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(660, 10, 71, 28))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(0, 170, 741, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.tableWidget.setHorizontalHeaderLabels([u'文件名', u'字数',u'重复字数',u'整体重复率(%)'])
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)

        self.tableWidget.setColumnWidth(0,400)
        self.tableWidget.setColumnWidth(3, 130)
        self.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showDialog)
        self.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showDialog4)
        self.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showDialog2)
        self.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showDialog3)
        self.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start_check)
        self.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.export_excel)
        self.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clear_excel)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)




    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "大麦全网文章查重工具", None))
        # self.label.setToolTip(_translate("Dialog", "作者:回忆与梦 qq:312141830", None))
        self.label.setText(_translate("Form", "大麦全网文章查重工具", None))
        self.pushButton.setText(_translate("Form", "选择文件夹", None))
        self.pushButton_7.setText(_translate("Form", "选择文件", None))
        self.pushButton_2.setText(_translate("Form", "开始分析", None))
       # self.label_2.setText(_translate("Form", "未选择文件夹", None))
        self.pushButton_3.setText(_translate("Form", "查看详细分析报告", None))
        self.pushButton_4.setText(_translate("Form", "导出报告", None))
        self.pushButton_5.setText(_translate("Form", "清空报告", None))
        self.pushButton_6.setText(_translate("Dialog", "使用说明", None))


