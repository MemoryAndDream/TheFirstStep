# -*- coding: utf-8 -*-
"""
File Name：     baidu_craw
Description :
Author :       meng_zhihao
date：          2018/11/5
"""
import requests,urllib
from lxml import etree
# 百度爬虫程序 只输出每条记录的结构 不负责分析逻辑
import random,re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class BaiduCraw:

    def __init__(self):
        pass

    def keyword_search(self,keyword):
        baidu_record_list = self.baidu_keyword_search(keyword)
        # sogou_record_list = self.sougou_search(keyword)
        # if sogou_record_list and len(sogou_record_list[0][1])>len(baidu_record_list[0][1]):
        #     return sogou_record_list
        return baidu_record_list

    def baidu_keyword_search(self,keyword):
        record_list = []
        url = 'http://www.baidu.com/s?wd=%s'%urllib.quote(keyword)
        r = requests.get(url,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'},timeout=10)
        rsp = r.text
        segments = self.getXpath('//div[@class="result c-container "]', rsp)  #
        for segment in segments:
            records = self.getXpath('//div[@class ="c-abstract"]',segment)
            # record = self.extractorText(records)
            record = ''.join(records)
            title = self.extractorText( self.getXpath('//div[@class="result c-container "]/h3/a',segment))
            ems = self.getXpath('//div[@class ="c-abstract"]//em/text()',segment)
            # 标红的过滤一下才是相似的
            ems = [em for em in ems if len(em)>4 ]

            em = self.extractorText(ems)
            sim_url = self.getXpath('//div[@class="f13"]/a[@class="c-showurl"]/@href',segment)
            sim_url = sim_url[0] if sim_url else ''
            record_list.append((record,em,sim_url,title))

        return record_list


    def sougou_search(self,keyword):

        record_list = []
        url = 'https://www.sogou.com/web?query=%s&ie=utf8'%urllib.quote(keyword)
        r = requests.get(url,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'},timeout=10)
        rsp = r.text
        segments = self.getXpath('//div[@class="rb"]', rsp)  #
        for segment in segments:
            records = self.getXpath('//div[@class="ft"]//text()',segment)
            record = self.extractorText(records)

            ems = self.getXpath('//div[@class="ft"]//em/text()',segment)
            em = self.extractorText(ems)
            sim_url = self.getXpath('//h3/a/@href',segment)
            sim_url = 'https://www.sogou.com'+sim_url[0] if sim_url else ''
            record_list.append((record,em,sim_url))

        return record_list

    # 获取xpath 要判断一下输入类型，或者异常处理
    @staticmethod
    def getXpath(xpath, content):   #xptah操作貌似会把中文变成转码&#xxxx;  /text()变unicode编码
        tree = etree.HTML(content)
        out = []
        results = tree.xpath(xpath)
        for result in results:
            if  'ElementStringResult' in str(type(result)) or 'ElementUnicodeResult' in str(type(result)) :
                out.append(result)
            else:
                out.append(etree.tostring(result))
        return out

    #去掉<>里的内容  这个方法会导致转义字符变回去！！！坑爹
    @staticmethod
    def extractorText(content):
        if type(content)==type([]):
            rs=''
            for record in content:
                rs+=(re.sub('(<[^>]*?>)',"",record))
            return rs
        return re.sub('(<[^>]*?>)',"",content)

if __name__ == '__main__':
    rs = BaiduCraw().keyword_search('在《三国》中，司马懿一出场就自命非凡')
    for r in rs :
        print r[0],r[1],r[2],r[3]
    pass