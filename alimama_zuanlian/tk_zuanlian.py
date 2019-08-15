#coding=utf8
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
import webbrowser
import time
import json
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
        self.CookiesForUrl = 'https://pub.alimama.com/'
        self.home_url = 'https://pub.alimama.com/'
        self.createLayout()
        self.createConnection()
        self.set_home_page()


    def search(self):
        address = str(self.addressBar.text())
        if address:
            if address.find('://') == -1:
                address = 'http://' + address
            url = QUrl(address)
            self.webView.load(url)
            self.webView.show()
            # time.sleep(5) # 等待页面加载 卡住主线程很不好！



    def set_home_page(self):
        self.webView.load(QUrl(self.home_url))
        self.webView.show()


    def get_cookie(self):
        self.cookies = {}
        for citem in self.webView.page().networkAccessManager().cookieJar().cookiesForUrl(QUrl(self.CookiesForUrl)):
           #self.cookies.append('%s=%s' % (citem.name(), citem.value()))
            self.cookies[str(citem.name())] = str(citem.value())
        # self.cookies = common.to_unicode('; '.join(self.cookiescookies))
        print self.cookies
        return self.cookies

    def linkClicked(self, url):
        self.webView.load(url)

    def createLayout(self):
        self.setWindowTitle(u"手动登录后点击完成登录")
        self.addressBar = QLineEdit()
        self.goButton = QPushButton(u"转到")
        self.complete = QPushButton(u"完成登录") # 后面做成自动检测的
        bl = QHBoxLayout()
        #bl.addWidget(self.addressBar)
       # bl.addWidget(self.goButton)
        bl.addWidget(self.complete)
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
        self.connect(self.complete, SIGNAL('clicked()'), self.complete_login)

        #self.connect(self.sendButton, SIGNAL('clicked()'), sendtest)

    def complete_login(self):
        cookie_dict = self.get_cookie()
        cookie_dict.update({"create":str(int(time.time()))})
        cookie = json.dumps(cookie_dict)
        with open('cookies.json','w') as f:
            f.write(cookie)
        self.close()


app = QApplication(sys.argv)
browser = MyBrowser()
browser.show()
sys.exit(app.exec_())
