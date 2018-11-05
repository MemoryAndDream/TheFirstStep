#coding=utf8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')
from PyQt4 import QtGui
from PyQt4 import QtCore
from chacong_ui import Ui_Form
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import time
import win32api
from article_analyse import ArticleAnalyse


success_num = 0
total_file_num = 0
CODE_FILE_PATH = 'jihuoma.tmp'
class MyPyQT_Form(QtGui.QMainWindow,QtGui.QWidget,Ui_Form):
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)
        self.dir_path = ''
        self.step = 0
        self.timer = QtCore.QBasicTimer()
        if not os.path.exists(CODE_FILE_PATH):
            QtGui.QMessageBox.information(self, u"未激活", u"程序未激活，请先运行激活器激活程序")
            sys.exit()
        else:
            with open(CODE_FILE_PATH) as f:
                code = str(f.readlines()[0])
                print code
                pan_code = str(win32api.GetVolumeInformation("C:\\")[1])
                if not code == pan_code:
                    QtGui.QMessageBox.information(self, u"激活失败", u"程序激活失败")
                    sys.exit()

        #

    def showDialog(self):
        filename = QtGui.QFileDialog.getExistingDirectory(self, 'Open file', './')
        self.label_2.setText(filename[:5]+'..')
        self.dir_path = unicode(filename)
        self.pushButton_2.setDisabled(False)
        self.pushButton_2.setText(u'开始分析')

    def showDialog2(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('file:///' +  os.path.dirname(os.path.abspath(__file__)).decode('GB2312')+ur"/检测报告" ))

    def start_check(self):
        if not self.dir_path:
            QtGui.QMessageBox.information(self, u"错误", u"请先选择文件夹")
            return
        self.onStart()
        self.BigWork()
#        self.main(self.dir_path)
        # 接搜索主程序逻辑


    def main(self,dir_path): # pyqt不能把主进程卡死 工作进程要和主进程分离
        # 遍历文件夹下的所有doc docx text 文件

       # import pdb;pdb.set_trace()
        for i in range(5):
            time.sleep(1)

    def timerEvent(self, event):
        self.pbar.setValue(success_num*1.0*100/total_file_num if total_file_num else 0)

    def onStart(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(100, self)

    def BigWork(self):
        # 把按钮禁用掉
        self.pushButton_2.setDisabled(True)
        # 新建对象，传入参数
        self.bwThread = BigWorkThread(self.dir_path)
        # 连接子进程的信号和槽函数
        self.bwThread.finishSignal.connect(self.BigWorkEnd)
        # 开始执行 run() 函数里的内容
        self.bwThread.start()

    # 增加形参准备接受返回值 ls
    def BigWorkEnd(self, ls):
        print 'get!'
        # 使用传回的返回值
        for word in ls:
            print word,
        # 恢复按钮
       # self.pushButton_2.setDisabled(False)
        self.pushButton_2.setText(u'分析完成')


#继承 QThread 类 长时间工作需要另起工作线程
class BigWorkThread(QtCore.QThread):

    """docstring for BigWorkThread"""
    #声明一个信号，同时返回一个list，同理什么都能返回啦
    finishSignal = QtCore.pyqtSignal(list)
    #构造函数里增加形参
    def __init__(self,dir_path,parent=None):
        super(BigWorkThread, self).__init__(parent)
        self.dir_path = dir_path

    #重写 run() 函数，在里面干大事。
    def run(self):
        global success_num
        global total_file_num
        total_file_num = 0
        file_list  = os.walk(self.dir_path)
        for file_paths in file_list:
            sub_file_paths = file_paths[2]
            parent_path = file_paths[0]
            for file_path in sub_file_paths:
                lower_file_path = file_path.lower()
                if  lower_file_path.endswith(u'.doc')  or lower_file_path.endswith(u'.docx') : #or lower_file_path.endswith(u'pdf')
                    if '$' in file_path:  # 缓存文件
                        continue
                    tmpPath = os.path.join(parent_path, file_path)
                    total_file_num += 1
                    analyse = ArticleAnalyse(tmpPath)
                    analyse.doc_analyse()
                elif lower_file_path.endswith(u'.txt'):
                    tmpPath = os.path.join(parent_path, file_path)
                    total_file_num += 1
                    analyse = ArticleAnalyse(tmpPath)
                    analyse.txt_analyse()
        #干完了，发送一个信号告诉主线程窗口
        self.finishSignal.emit(['hello,','world','!'])





if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    GUI = MyPyQT_Form() # 实例化
    GUI.show()
    sys.exit(app.exec_())