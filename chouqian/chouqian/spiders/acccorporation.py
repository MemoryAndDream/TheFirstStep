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

from chouqian.items import acccorporation_Item
import json
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from urlparse import urljoin
from scrapy.utils.response import get_base_url
from crawl_tool import crawlerTool
from HTMLParser import HTMLParser
import re,pdb

class AcccorporationSpider(scrapy.Spider):
    name = "acccorporation"  # 唯一标识
    # allowed_domains = ["*"]

    start_urls = ["https://www.acccorporation.com/compounds.html?p=%s"%str(i) for i in range(7000,19695,1) #(1,3940,1)总共19695 已经跑了1594
    ]

    def parse(self, response):
        base_url = get_base_url(response)
        response_content = response.body # 乱码处理 #像https://www.chemicalbook.com/ShowSupplierProductsList6187/51100.htm有9万多
        cat_name = response.meta.get('cat_name')
        segs = crawlerTool.getXpath('//table[@id="product-list"]/tbody/tr', response_content)

        for seg in segs:
            name,MolecularFormula,MolecularWeight,image,cas,url = ['' for i in range(6)]
            SearchImg = crawlerTool.getXpath1('//img[@class="dg-picture-zoom  acc_img_container acc_zoomer"]/@src', seg)
            contents = crawlerTool.getXpath('//table//tr', seg)
            for content in contents:
                content=content.replace('\r','').replace('\n','')
                if 'Name' in content:
                    name = crawlerTool.getXpath1('//td[2]', content)
                    name = crawlerTool.getRegex('>(.*?)<',name).strip()
                elif 'CAS No' in content:
                    cas =crawlerTool.getXpath1('//td[2]', content)
                    cas = crawlerTool.getRegex('>(.*?)<', cas).strip()
                elif 'Molecular Formula' in content:
                    MolecularFormula = crawlerTool.getXpath1('//td[2]', content)
                    MolecularFormula = re.sub('<.*?>','',MolecularFormula).strip()
                elif 'Molecular Weight' in content:
                    MolecularWeight = crawlerTool.getXpath1('//td[2]', content)
                    MolecularWeight = crawlerTool.getRegex('>(.*?)<', MolecularWeight).strip()


           # primaryVendorId = crawlerTool.getXpath1('//str[@name="primaryVendorId"]/text()', seg)
            data_obj = acccorporation_Item()
            data_obj['url'] = name
            data_obj['name'] = name
            data_obj['MolecularFormula'] = MolecularFormula
            data_obj['MolecularWeight'] = MolecularWeight
            data_obj['image'] = SearchImg
            data_obj['cas'] = cas
            yield data_obj
        # next_page_url = crawlerTool.getXpath('//div[@align="center"]/a/@href',response_content)
        # if next_page_url:
        #     for page_url in next_page_url:  # 重试
        #         page_url = urljoin(base_url,page_url)
        #         yield scrapy.Request(url=page_url, callback=self.parse)



if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))
    print 'start spider'
    cmdline.execute("scrapy crawl acccorporation".split())


# Chemical Name:CAS number:
# Mol. Formula:

#http://www.acccorporation.com/compounds/halochemicals.html?dir=asc&limit=200&order=name&p=1457