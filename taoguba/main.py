# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 21:01
# @Author  : meng_zhihao
# @Email   : 312141830@qq.com
# @File    : main.py
import requests
from lxml import etree
import xlwt

# 获取xpath 要判断一下输入类型，或者异常处理

def getXpath(xpath, content):
    tree = etree.HTML(content)
    out = []
    results = tree.xpath(xpath)
    for result in results:
        if 'ElementStringResult' in str(type(result)) or 'ElementUnicodeResult' in str(type(result)):
            out.append(result)
        else:
            out.append(etree.tostring(result))
    return out

first_url = 'https://www.taoguba.com.cn/index?blockID=1'
filename = u'结果.xls'
wbk = xlwt.Workbook()
sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
row = 0
sheet.write(row, 0, u'标题')
sheet.write(row, 1, u'链接')
sheet.write(row, 2, u'日期')
sheet.write(row, 3, u'点赞数')
row += 1
for num in range(1,20,1):
    try:
        url = 'https://www.taoguba.com.cn/index?pageNo=%s&blockID=1&flag=1&pageNum=23812'%str(num)
        page = requests.get(url,timeout=10).content
        segs = getXpath('//div[@class="Notspmatch"]//div/ul',page)
        for seg in segs:
            title = getXpath('//li[@class="pcdj02"]/a/@title',seg)[0]
            url = 'https://www.taoguba.com.cn/'+ getXpath('//li[@class="pcdj02"]/a/@href',seg)[0]
            date = getXpath('//li[@class="pcdj06"]/text()',seg)[0]
            zan = getXpath('//li[@class="pcdj05"]/text()', seg)[1]
            sheet.write(row, 0, title)
            sheet.write(row, 1, url)
            sheet.write(row, 2, date)
            sheet.write(row, 3, zan)
            row += 1
    except:
        pass
wbk.save(filename)


