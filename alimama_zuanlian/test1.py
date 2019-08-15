#coding=utf8
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
import webbrowser
import time

class WebPage(QWebPage):
    def __init__(self):
        super(WebPage, self).__init__()

    def acceptNavigationRequest(self, frame, request, type):
        if (type == QWebPage.NavigationTypeLinkClicked):
            if (frame == self.mainFrame()):
                self.view().load(request.url())
                print "local window"
            else:
                # webbrowser.open(request.url().toString())
                self.view().load(request.url())
                return False
        return QWebPage.acceptNavigationRequest(self, frame, request, type)


class MyBrowser(QWidget):
    def __init__(self, parent=None):
        super(MyBrowser, self).__init__(parent)
        self.createLayout()
        self.createConnection()
        self.CookiesForUrl = 'http://www.baidu.com'

    def search(self):
        address = str(self.addressBar.text())
        if address:
            if address.find('://') == -1:
                address = 'http://' + address
            url = QUrl(address)
            self.webView.load(url)
            self.webView.show()
            #time.sleep(5) # 等待页面加载 卡住主线程很不好！
            self.get_cookie()

    def get_cookie(self):
        self.cookies = []
        for citem in self.webView.page().networkAccessManager().cookieJar().cookiesForUrl(QUrl(self.CookiesForUrl)):
            self.cookies.append('%s=%s' % (citem.name(), citem.value()))
        # self.cookies = common.to_unicode('; '.join(self.cookiescookies))
        print self.cookies
        return self.cookies

    def linkClicked(self, url):
        self.webView.load(url)

    def createLayout(self):
        self.setWindowTitle("keakon's browser")
        self.addressBar = QLineEdit()
        self.goButton = QPushButton("&GO")
        self.sendButton = QPushButton("&Send")
        bl = QHBoxLayout()
        bl.addWidget(self.addressBar)
        bl.addWidget(self.goButton)
        bl.addWidget(self.sendButton)

        self.webView = QWebView()
        self.webView.setPage(WebPage())
        self.webSettings = self.webView.settings()
        self.webSettings.setAttribute(QWebSettings.PluginsEnabled, True)
        self.webSettings.setAttribute(QWebSettings.JavascriptEnabled, True)
        self.webView.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
        self.webView.page().linkClicked.connect(self.linkClicked)

        layout = QVBoxLayout()
        layout.addLayout(bl)
        layout.addWidget(self.webView)
        self.setLayout(layout)

    def createConnection(self):
        self.connect(self.addressBar, SIGNAL('returnPressed()'), self.search)
        self.connect(self.addressBar, SIGNAL('returnPressed()'), self.addressBar, SLOT('selectAll()'))
        self.connect(self.goButton, SIGNAL('clicked()'), self.search)
        self.connect(self.goButton, SIGNAL('clicked()'), self.addressBar, SLOT('selectAll()'))
        #self.connect(self.sendButton, SIGNAL('clicked()'), sendtest)


# def sendtest():
#     import socket, sys
#     import struct
#     import binascii
#     host = "42.51.132.111"
#     port = 8000
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print s.getsockname()
#     senddata = binascii.a2b_hex("000000220004313030370A183534386665356637306366323332316432653162383762331006")
#     print senddata
#     print repr(senddata[36])
#     s.send(senddata)


app = QApplication(sys.argv)

browser = MyBrowser()
browser.show()

sys.exit(app.exec_())
