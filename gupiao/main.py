# -*- coding: utf-8 -*-
"""
File Name：     main
Description :
Author :       meng_zhihao
mail :       312141830@qq.com
date：          2018/12/13
"""
import xlwt
import requests
import json
import datetime
import ConfigParser
import re
from crawl_tool import crawlerTool
content = open('main.conf').read()
#Window下用记事本打开配置文件并修改保存后，编码为UNICODE或UTF-8的文件的文件头
#会被相应的加上\xff\xfe（\xff\xfe）或\xef\xbb\xbf，然后再传递给ConfigParser解析的时候会出错
#，因此解析之前，先替换掉
content = re.sub(r"\xfe\xff","", content)
content = re.sub(r"\xff\xfe","", content)
content = re.sub(r"\xef\xbb\xbf","", content)
open('main.conf', 'w').write(content)
mainconf = ConfigParser.ConfigParser()
mainconf.read('main.conf')
run_date = mainconf.get('conf','date')

field_map = {"url":"帖子地址","reply_count":"帖子评论数","title":"帖子标题","created_at":"帖子创建时间"}
HEADERS = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'}
se = requests.session()
def gen_xls(data_list):
    wb = xlwt.Workbook(encoding='gbk')  # 设定编码类型为utf8
    sheet = wb.add_sheet(u'结果')  # excel里添加类别
    row = 1
    for data in data_list:
        for i in range(len(data)):
            print data[i]
            sheet.write(row, i, data[i])
        row += 1
    return wb


def extractor_page(page): # 解析搜索页
   # import pdb;pdb.set_trace()
    segs = re.findall('"SECURITYCODE":"(.*?)"',page)

    codes = [seg.split('.')[0] for seg in segs]
    result = []
    codes = list(set(codes)) # 去重
    print '总数',len(codes)
    code_content = []
    for code in codes:
        url = 'http://data.eastmoney.com/soft/stock/StockDetail.aspx?code=%s&date=%s'%(code,run_date)
        print url
        page_buf = se.get(url,timeout=10, headers=HEADERS).content
        try:
            code_content.extend(extractor_page2(page_buf,code))
        except Exception,e:
            print str(e)
    return code_content


def extractor_page2(page,code): # 解析详情页
    # 买入前5名
    content_table = crawlerTool.getXpath('//table',page,charset='gbk')[0]
    trs = crawlerTool.getXpath('//tr',content_table,charset='gbk')
    rows = [[],[u'股票代码',code]]
    for tr in trs:
        row = []
        for td in crawlerTool.getXpath('//th',tr,charset='gbk'):
            row.append(re.sub('(<.*?>)',"",td).strip())
        for td in crawlerTool.getXpath('//td',tr,charset='gbk'):
            row.append(re.sub('(<.*?>)',"",td).strip())
        rows.append(row)
    #卖出前5名
    content_table = crawlerTool.getXpath('//table',page,charset='gbk')[1]
    trs = crawlerTool.getXpath('//tr',content_table,charset='gbk')
    for tr in trs:
        row = []
        for td in crawlerTool.getXpath('//th',tr,charset='gbk'):
            row.append(re.sub('(<.*?>)',"",td).strip())
        for td in crawlerTool.getXpath('//td',tr,charset='gbk'):
            row.append(re.sub('(<.*?>)',"",td).strip())
        rows.append(row)

    return rows


if __name__ == '__main__':
   # import pdb;pdb.set_trace()
    #start_url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&count=15&category=105'
    csv_rows=[]
    cookie = {}
    result = se.get('http://data.eastmoney.com/soft/stock/TradeDetail.aspx?date=%s'%run_date, timeout=10, headers=HEADERS)
    result = result.content
    data_list = extractor_page(result)
    csv_rows.extend(data_list)
    wb = gen_xls(csv_rows)
    wb.save('result.xls' )




