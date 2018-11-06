#coding=utf8
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from jihuoma_ui import Ui_Form
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import time

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
        s = time.time() # 激活码生成的有效时长由这里修改
        prp = prpcrypt('123454536f667445454d537973576562','1234577290ABCDEF1264147890ACAE45'[0:16])
        s= prp.encrypt(str(int(s)))
        print prp.decrypt(s)
        self.textEdit.setText(s)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    GUI = MyPyQT_Form() # 实例化
    GUI.show()
    sys.exit(app.exec_())