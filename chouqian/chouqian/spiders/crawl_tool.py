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

            # content = unicode(content, encoding=charset)  # xpath传入必须是unicode，不然中文会乱码
            tree = etree.HTML(content)
        out = []
        results = tree.xpath(xpath)
        for result in results:
            if  'ElementStringResult' in str(type(result)) or 'ElementUnicodeResult' in str(type(result)) :
                out.append(result)
            else:
                out.append(etree.tostring(result,encoding = charset,method = xml_type)) # 加编码就不会变成html编码了
        return out

    # 获取xpath 要判断一下输入类型，或者异常处理
    @staticmethod
    def getXpath1(xpath, content,charset = 'utf8',xml_type='HTML'):   #xptah操作貌似会把中文变成转码&#xxxx;  /text()变unicode编码
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
                out.append(etree.tostring(result,encoding = charset,method = xml_type)) # 加编码就不会变成html编码了
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
    content = crawlerTool.get('https://item.jd.com/33891466302.html')
  #  print chardet.detect('C₂₁H₂₆Cl₂N₂OS')
  #   content = content[:10000]
    print len(content)
   # print content
    #content = content.encode('utf8')
    # content = content[:4817]+ content[4819:]
    new_content = content
    for i in range(10): # 乱码处理 之后要把xpath里的unicode去掉
        try:
            content = unicode(content, 'gbk')
            break
        except Exception, e:
            print str(e)
            if 'position' in str(e):
                error_str = crawlerTool.getRegex('position\s+(\d+-\d+)', str(e))
                start_index, end_index = int(error_str.split('-')[0]), int(error_str.split('-')[1]) + 1
                print start_index, end_index
                print content[start_index-10:start_index]
                content = content[:start_index] + content[end_index:]

    with open('1.html' ,'w') as f:
        f.write(content)
    #content=content.replace('gb2312','GB18030')
    #print chardet.detect(content)
   # rs = crawlerTool.getXpath("//td[@class='goscill22']/table[4]",content) # getXpath要用unicode！！
    name = crawlerTool.getXpath("//div[@class='sku-name']/text()",
                                content,charset='gbk')[0]
    print name
    # cplb_div = crawlerTool.getXpath('//div[@id="ContentPlaceHolder1_ProductSupplier"]//table', content)[3:-1]
    # for cp in cplb_div:
    #     chinese_name = crawlerTool.getXpath('//tr/td[2]/text()', cp)
    #     chinese_name = chinese_name[0] if chinese_name else ''
    #   #  print chardet.detect(chinese_name)
    #     print chinese_name

    #print(rs,len(rs))
    #print(crawlerTool.getRegex(""))