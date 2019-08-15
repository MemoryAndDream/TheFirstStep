# -*- coding: utf-8 -*-
# encoding: utf-8

"""
@author: Meng.ZhiHao
@contact: 312141830@qq.com
@file: cou_qian_spider.py
@time: 2018/1/10 13:45
"""
if __name__ == "__main__":
    from scrapy import cmdline
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

import scrapy

from chouqian.items import Caymanchem
import json
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from urlparse import urljoin
from scrapy.utils.response import get_base_url
from crawl_tool import crawlerTool
from HTMLParser import HTMLParser

cats={'Cancer ':'raptas%3ARAP000112','Cardiovascular Disease':'raptas%3ARAP000121',
      'Cell Biology':'raptas%3ARAP000128','Eicosanoids & Lipids':'raptas%3ARAP000143',
      'Epigenetics':'raptas%3ARAP000185','Immunology & Inflammation':'raptas%3ARAP000209',
      'Metabolism':'raptas%3ARAP000229','Neuroscience':'raptas%3ARAP000245',
      'Oxidative Stress & Reactive Species':'raptas%3ARAP000258',
      'Toxicology':'raptas%3ARAP000268'
      }
class CaymanchemSpider(scrapy.Spider):
    name = "caymanchem"  # 唯一标识
    # allowed_domains = ["csdn.net"]
    start_urls = [
    ]
#    数据总量23000条

    def start_requests(self): #测试cookie
        for cat_name, cat_id in cats.iteritems():
            #https://www.caymanchem.com/Search?q=*%3A*&fq=raptas%3ARAP000258
            url = 'https://www.caymanchem.com/solr/cchProduct/select?facet=true&facet.field=raptas'+\
                  '&facet.field=newProduct&facet.limit=100000&fl=isEUSellable%2Cname%2CmarkupName%2CcatalogNum%2CproductImage%2Csynonyms%2CcasNumber%2Ctagline%2Cscore%2CitemGroupId%2CprimaryVendorId&spellcheck=true&spellcheck.collate=true&spellcheck.count=10&spellcheck.extendedResults=true&spellcheck.onlyMorePopular=false&facet.mincount=1&rows=10&version=2.2&json.nl=map&'+\
                  'q=*%3A*&fq=('+cat_id+')AND(!raptas%3ARAP000101%20AND%20websiteNotSearchable%3Afalse)'
            yield scrapy.Request(url, callback=self.parse, meta={'cat_name': cat_name})

    def parse(self, response):
        base_url = get_base_url(response)
        response_content = response.body # 乱码处理 #像https://www.chemicalbook.com/ShowSupplierProductsList6187/51100.htm有9万多
        cat_name = response.meta.get('cat_name')
        segs = crawlerTool.getXpath('//doc', response_content,xml_type='XML')
        for seg in segs:
            name = crawlerTool.getXpath1('//str[@name="name"]/text()', seg)
            cas = crawlerTool.getXpath1('//str[@name="casNumber"]/text()',seg)
            function = crawlerTool.getXpath1('//str[@name="tagline"]/text()', seg)
           # primaryVendorId = crawlerTool.getXpath1('//str[@name="primaryVendorId"]/text()', seg)
            data_obj = Caymanchem()
            data_obj['name'] = name
            data_obj['cas'] = cas
            data_obj['function'] = function
            data_obj['cat'] = cat_name
            data_obj['url'] = name+cat_name+cas
            yield data_obj
        totalnum = int(crawlerTool.getXpath1('//result[@name="response"]//@numFound',response_content,xml_type='XML'))
        if not response.meta.get('depth'):
            print totalnum
            for i in range(1,totalnum,1):
                url = 'https://www.caymanchem.com/solr/cchProduct/select?facet=true&facet.field=raptas'+\
                      '&facet.field=newProduct&facet.limit=100000&fl=isEUSellable%2Cname%2CmarkupName%2CcatalogNum%2CproductImage%2Csynonyms%2CcasNumber%2Ctagline%2Cscore%2CitemGroupId%2CprimaryVendorId&spellcheck=true&spellcheck.collate=true&spellcheck.count=10&spellcheck.extendedResults=true&spellcheck.onlyMorePopular=false&facet.mincount=1&rows=10&version=2.2&json.nl=map&'+\
                      'q=*%3A*&start='+str(i)+'&fq=('+cats[cat_name]+')AND(!raptas%3ARAP000101%20AND%20websiteNotSearchable%3Afalse)'
                yield scrapy.Request(url, callback=self.parse, meta={'cat_name':cat_name,'depth':1})
        # next_page_url = crawlerTool.getXpath('//div[@align="center"]/a/@href',response_content)
        # if next_page_url:
        #     for page_url in next_page_url:  # 重试
        #         page_url = urljoin(base_url,page_url)
        #         yield scrapy.Request(url=page_url, callback=self.parse)



if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))
    print 'start spider'
    cmdline.execute("scrapy crawl caymanchem".split())


