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
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import scrapy
import os
from chouqian.items import ChemspaceItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from urlparse import urljoin
from scrapy.utils.response import get_base_url
from crawl_tool import crawlerTool
from pipelines import MysqlPipeline3
from HTMLParser import HTMLParser
class ChemspaceSpider(scrapy.Spider):
    name = "chemspace"  # 唯一标识
    # allowed_domains = ["csdn.net"]
    db_connect = MysqlPipeline3()



    def start_requests(self):
        sdf_dir = 'compounds'
        sdf_files = os.listdir(sdf_dir)
        for sdf_file in sdf_files:
            with open('compounds/'+sdf_file,'r') as fout:
                print 'sdf_file',sdf_file
                for line in fout:
                   url = crawlerTool.getRegex('(https://chem-space.com/\w+)',line)

                   if url and  not self.db_connect.get_by_unique_value(url): # 由于内存不够会被kill掉！
                       yield scrapy.Request(url, callback=self.parse)





    def parse(self,response):
        base_url = get_base_url(response)
        response_content = response.body # 乱码处理
        url= response.url
        '''
    url = scrapy.Field()
    IUPACname = scrapy.Field()
    CAS = scrapy.Field()
    Chemspaceid = scrapy.Field()
    Molformula = scrapy.Field()
    Molweight = scrapy.Field()
        '''
        data_obj = ChemspaceItem()
        data_obj['url'] = url
        data_obj['IUPACname'] = crawlerTool.getXpath1('//div[@class="iupac-name"]//text()',response_content)
        data_obj['CAS'] = crawlerTool.getRegex('<dt>CAS</dt>[^<]?<dd>([\d-]+)</dd>',response_content)
        data_obj['Molformula'] = crawlerTool.getRegex('<dt>Mol formula</dt>[^<]?<dd>([\d\w]+)</dd>',response_content.replace('</sub>','').replace('<sub>',''))
        data_obj['Molweight']  = crawlerTool.getRegex('<dt>Mol weight</dt>[^<]?<dd>([\d\.]+)</dd>',response_content)
        print data_obj
        yield data_obj





if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))
    print 'start spider'
    cmdline.execute("scrapy crawl chemspace".split())


