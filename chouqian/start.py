# -*- coding: utf-8 -*-
"""
File Name：     start
Description :
Author :       meng_zhihao
date：          2018/11/30
"""
from scrapy import cmdline
import os,sys

if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
  
    print 'start spider'
    cmdline.execute("scrapy crawl cmocro -o result.csv -t csv".split())
#公司名	电话	详情链接	邮编	关于我们	手机	地址	电子邮箱	网址	联系人
