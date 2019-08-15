# -*- coding: utf-8 -*-
"""
File Name：     crawl_tool_for_py3
Description :
Author :       meng_zhihao
date：          2018/11/20

"""
import chardet
import requests
from lxml import etree
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}

#通用方法
class crawlerTool:
    default_charset = 'utf8'
    def __init__(self):
        self.session = requests.session()
        pass

    def __del__(self):
        self.session.close()

    @staticmethod
    def get(url):
        rsp = requests.get(url,timeout=10,headers=HEADERS)
        return rsp.content # 二进制返回

    @staticmethod
    def post(url,data):
        rsp = requests.post(url,data,timeout=10,headers=HEADERS)
        return rsp.content


    def sget(self,url,cookies={}):
        rsp = self.session.get(url,timeout=10,headers=HEADERS,cookies=cookies)
        return rsp.content # 二进制返回

    def spost(self,url,data):
        rsp = self.session.post(url,data,timeout=10,headers=HEADERS)
        return rsp.content



    # 获取xpath 要判断一下输入类型，或者异常处理
    @staticmethod
    def getXpath(xpath, content,charset = 'utf8',xml_type='HTML'):   #xptah操作貌似会把中文变成转码&#xxxx;  /text()变unicode编码
        if xml_type=='XML':
            tree = etree.XML(content)
        else:
            if type(content) != type(u''):
                content = unicode(content, encoding=charset)  # xpath传入必须是unicode，不然中文会乱码
            tree = etree.HTML(content)
        out = []
        results = tree.xpath(xpath)
        for result in results:
            if  'ElementStringResult' in str(type(result)) or 'ElementUnicodeResult' in str(type(result)) :
                out.append(result)
            else:
                out.append(etree.tostring(result,encoding =charset,method = xml_type)) # 加编码就不会变成html编码了 输入和输出都会被统一编码
        return out

    # 获取xpath 要判断一下输入类型，或者异常处理
    @staticmethod
    def getXpath1(xpath, content,charset = 'utf8',xml_type='HTML'):   #xptah操作貌似会把中文变成转码&#xxxx;  /text()变unicode编码
        if xml_type=='XML':
            tree = etree.XML(content)
        else:
            content = unicode(content, encoding=charset)  # xpath传入必须是unicode，不然中文会乱码
            tree = etree.HTML(content)

        out = []
        results = tree.xpath(xpath)
        for result in results:
            if  'ElementStringResult' in str(type(result)) or 'ElementUnicodeResult' in str(type(result)) :
                out.append(result)
            else:
                out.append(etree.tostring(result,encoding = charset,method = xml_type)) # 加编码就不会变成html编码了 输入和输出都会被统一编码
        if out:
            return out[0]
        else:
            return ''

    @staticmethod
    def getRegex(regex, content):
        rs = re.search(regex,content)
        if rs:
            return rs.group(1)
        else:
            return ''


if __name__ == '__main__':
    content = crawlerTool.get('http://data.eastmoney.com/soft/stock/StockDetail.aspx?code=000957&date=2019-01-11')
  #  print chardet.detect(content)
    print len(content)
    with open('1.html' ,'w') as f:
        f.write(content)
    #content=content.replace('gb2312','GB18030')
    #print chardet.detect(content)
   # rs = crawlerTool.getXpath("//td[@class='goscill22']/table[4]",content) # getXpath要用unicode！！

    name = crawlerTool.getXpath('//tr',
                                response_content)[0]
    #print name


    #print(rs,len(rs))
    #print(crawlerTool.getRegex(""))