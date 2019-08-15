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
import pdb
from chouqian.items import Trc_Item
import json
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from urlparse import urljoin
from scrapy.utils.response import get_base_url
from crawl_tool import crawlerTool
from HTMLParser import HTMLParser

class Trc_CandaSpider(scrapy.Spider):
    name = "trc_canda"  # 唯一标识
    # allowed_domains = ["*"]
    start_urls = ["https://www.trc-canada.com/impurity/#"
    ]


    def parse(self, response):
        response_content = response.body
        cats = crawlerTool.getXpath('//input[@type="checkbox"]/@value',response_content)
        print len(cats)
        # cats = ['Ether']
        for cat in cats:
            first_str = cat[0].lower()
            # if first_str in ('a','b','c'):continue
            yield scrapy.FormRequest(url='https://www.trc-canada.com/parentdrug-listing/',
                                     formdata={"keyword" : " %s "%cat, "t" : "product","advanced":"yes"},
                                     callback=self.parse1,meta = {'cat_name':cat})



    def parse1(self, response):
        base_url = get_base_url(response)

        response_content = response.body # 乱码处理 #像https://www.chemicalbook.com/ShowSupplierProductsList6187/51100.htm有9万多
        cat_name = response.meta.get('cat_name')
        segs = crawlerTool.getXpath('//div[@class="product_list_left_in"]//li', response_content)
        for seg in segs:
            ChemicalName,CASNumber,MolFormula,SearchImg,Synonyms,url = ['' for i in range(6)]
            SearchImg = crawlerTool.getXpath1('//div[@class="leftSearchImg"]/a/img/@src', seg)
            SearchImg = 'https://www.trc-canada.com' + SearchImg
            contents = crawlerTool.getXpath('//div[@class="ContentDesc"]', seg)
            for content in contents:
                content=content.replace('\r','').replace('\n','')
                if 'Chemical Name:' in content:
                    ChemicalName = crawlerTool.getRegex('</label>(.*?)<',content).strip()
                elif 'CAS number:' in content:
                    CASNumber = crawlerTool.getRegex('</label>(.*?)<', content).strip()
                elif 'Mol. Formula:' in content:
                    MolFormula = crawlerTool.getRegex('</label>(.*?)<', content).strip()
                elif 'Synonyms' in content:
                    Synonyms = crawlerTool.getRegex('</label>(.*?)<', content).strip()

           # primaryVendorId = crawlerTool.getXpath1('//str[@name="primaryVendorId"]/text()', seg)
            data_obj = Trc_Item()
            data_obj['ChemicalName'] = ChemicalName
            data_obj['CASNumber'] = CASNumber
            data_obj['MolFormula'] = MolFormula
            data_obj['SearchImg'] = SearchImg
            data_obj['Synonyms'] = Synonyms
            data_obj['api_name'] = cat_name
            data_obj['url'] = SearchImg
            yield data_obj
        # if response.meta['depth']>1:
        #     print '跳过'
        #     return
        # next_page_url = crawlerTool.getXpath('//div[@class="product-pagination"]//li/a/@href',response_content)
        # if next_page_url:
        #     print 'need_test',cat_name
        #     # pdb.set_trace()
        #     for page_url in next_page_url:  # 重试
        #         page_url = urljoin(base_url,page_url)
        #         yield scrapy.Request(url=page_url,meta={'cookiejar': page_url+cat_name,'cat_name':cat_name},callback=self.parse1
        #                            ) # 默认全用一个cookie所以要改 # 忽略多层翻页



if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))
    print 'start spider'
    cmdline.execute("scrapy crawl trc_canda".split())


# Chemical Name:CAS number:
# Mol. Formula:

