# -*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4.QtNetwork import *
'''
http://weibo.com/ http://www.baidu.com/ http://www.google.com/
'''
class BrowserWidget(QWidget):
    def __init__(self, HOMEPAGE, parent=None):
        super(self.__class__, self).__init__(parent)
        self.browser = QWebView()
        self.lineedit = QLineEdit()
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setMargin(0)
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.connect(self.lineedit, SIGNAL("returnPressed()"), self.entrytext)
        self.browser.load(QUrl(HOMEPAGE))
        self.browser.show()
        self.CookiesForUrl = 'http://tieba.baidu.com/p/3085259306'

    def entrytext(self):
        self.browser.load(QUrl(self.lineedit.text()))

    def CookieOk(self):
        self.cookies = []
        for citem in self.browser.page().networkAccessManager().cookieJar().cookiesForUrl(QUrl(self.CookiesForUrl)):
            self.cookies.append('%s=%s' % (citem.name(), citem.value()))
        # self.cookies = common.to_unicode('; '.join(self.cookiescookies))
        print self.cookies
        return self.cookies

class Window(QMainWindow):
    def __init__(self, TITLE, HOME, parent=None):
        super(self.__class__, self).__init__(parent)
        self.browserWindow = BrowserWidget(HOME)
        self.setCentralWidget(self.browserWindow)
        self.setWindowTitle(TITLE)
        status = self.statusBar()
        status.setSizeGripEnabled(True)
        self.label = QLabel("")
        status.addWidget(self.label, 1)
        self.connect(self.browserWindow.browser, SIGNAL("loadStarted(bool)"), self.loadStarted)
        self.connect(self.browserWindow.browser, SIGNAL("loadFinished(bool)"), self.loadFinished)
        self.connect(self.browserWindow.browser, SIGNAL("loadProgress(int)"), self.loading)
        self.loginFlag = 1

    def loadStarted(self, flag):
        print 'requestedUrl:' + self.browserWindow.browser.page().mainFrame().requestedUrl()

    def loadFinished(self, flag):
        '''
        findFirst里的参数语法#号开头的查找id名的，
        点号”.”开头的则是查找class名字的，
        如果没有前面符号的则是查找标准HTML标记比如findFirst(“body”)
        http://www.w3.org/TR/CSS2/selector.html#q1
        网页远代码:self.browserWindow.browser.page().currentFrame().toHtml().toUtf8()
        set value的方法:setText,setAttribute
        get 的方法:
        Text = TextInput.attribute("value")
        frame.findAllElements("input[name=submit]")
        updates.evaluateJavaScript("this.checked").toBool()   (check框)
        firstName.evaluateJavaScript("this.value").toString()   (普通)
        <div id=”in_nav”>
        上一篇：<a title=”新股中签的回报率” href=”/yobin/blog/item/86ad9223e5add74fad34de92.html”>新股中签的回报率</a>
        下一篇：<a title=”人民时评：且看美国的信息自由” href=”/yobin/blog/item/dc3491587b51cbd59c8204ba.html”>人民时评：且看美国的信息自由</a></div>
        QWebElement e_nav=m_blog.findFirst("#in_nav");
        QWebElement prev_nav=e_nav.findFirst("a");
        '''
        self.label.setText(u"加载完毕") # 加载完不成怎么破？

        self.browserWindow.CookieOk()
        print 'loadFinished' + str(self.browserWindow.browser.url().toString())
        if 'https://passport.baidu.com/v2/?login' == str(self.browserWindow.browser.url().toString()) and self.loginFlag:
            print 'passport.baidu.com load finish'
            self.CookieOk()

            frame = self.browserWindow.browser.page().mainFrame()
            # print doc.toPlainText().toUtf8()
            doc = frame.documentElement()
            # m_blog = doc.findFirst("#form1")
            # print m_blog.toPlainText().toUtf8()
        '''
        百度搜索
        baiduInput = doc.findFirst('input[id="kw1"]')
        baiduInput.setAttribute('value',u'我不知道')
        print baiduInput.attribute("value")
        #baiduinput.setFocus()
        baiduSearch = doc.findFirst('input[id="su1"]')
        baiduSearch.evaluateJavaScript("this.click()")
        #doc.evaluateJavaScript("document.getElementById('su1').click()")
        #baiduInput.evaluateJavaScript("javascript:F.call('ps/sug','pssubmit');")
        '''
        nameInput = doc.findFirst('input[id="TANGRAM__3__userName"]')
        # nameInput = doc.findFirst('#TANGRAM__3__userName')
        nameInput.setAttribute('value', u'harryide')
        passwordInput = doc.findFirst('input[id="TANGRAM__3__password"]')
        passwordInput.setAttribute('value', u'******')
        loginBtn = doc.findFirst('input[id="TANGRAM__3__submit"]')
        loginBtn.evaluateJavaScript("this.click()")
        self.loginFlag = 0

    def loading(self, percent):
        self.label.setText("Loading %d%%" % percent)
        self.browserWindow.lineedit.setText(self.browserWindow.browser.url().toString())



def main():
    app = QApplication(sys.argv)
    window = Window(TITLE=u"BaiduLogin", HOME='https://passport.baidu.com/v2/?login')
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()