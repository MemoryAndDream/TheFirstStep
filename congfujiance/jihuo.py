#coding=utf8
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from jihuo_ui import Ui_Form
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import time
import os
import win32api

CODE_FILE_PATH = 'jihuoma.tmp'
class prpcrypt():
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv
        self.mode = AES.MODE_CBC

        # 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 16
        count = len(text)
        if (count % length != 0):
            add = length - (count % length)
        else:
            add = 0
        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串 ,当然也可以转换为base64加密的内容，可以使用b2a_base64(self.ciphertext)
        return b2a_hex(self.ciphertext)

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')


class MyPyQT_Form(QtGui.QMainWindow,QtGui.QWidget,Ui_Form):
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)

    #实现pushButton_click()函数，textEdit是我们放上去的文本框的id
    def pushButton_click(self):
        print '触发点击'
        s = time.time()
        prp = prpcrypt('123454536f667445454d537973576562','1234577290ABCDEF1264147890ACAE45'[0:16])
        s= prp.encrypt(str(int(s)))
        print prp.decrypt(s)
        self.QLineEdit.setText(s)

    def input_code(self):
        code = self.QLineEdit.text() #QString
        if os.path.exists(CODE_FILE_PATH):
            QtGui.QMessageBox.information(self, u"激活失败", u"激活文件已存在") #b61129731b5ec530755a61815366ca29 一年有效的激活码
             #3c90f6a7073d20a56efecd68074fb441 12月6号前有效

        if code:
            prp = prpcrypt('123454536f667445454d537973576562', '1234577290ABCDEF1264147890ACAE45'[0:16])
            try:
                code = unicode(code)
                t = prp.decrypt(code)
                print t
                if int(t)<time.time()-60*15:
                    QtGui.QMessageBox.information(self, u"激活失败", u"激活失败,激活码已过期")
                else:
                    pan_code = str(win32api.GetVolumeInformation("C:\\")[1])
                    with open(CODE_FILE_PATH,'w') as f:
                        f.write(pan_code)
                    QtGui.QMessageBox.information(self, u"激活成功", u"激活成功，生成激活文件jihuoma.tmp，请勿删除")
            except Exception,e:
                print str(e)
                QtGui.QMessageBox.information(self, u"激活失败", u"激活失败")
        else:
            QtGui.QMessageBox.information(self, u"请输入激活码", u"请输入激活码")
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    GUI = MyPyQT_Form() # 实例化
    GUI.show()
    sys.exit(app.exec_())