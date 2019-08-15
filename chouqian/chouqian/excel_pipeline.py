# -*- coding: utf-8 -*-
"""
File Name：     excel_pipeline
Description :
Author :       meng_zhihao
mail :       312141830@qq.com
date：          2018/12/24
"""
import openpyxl
import pipelines
class CdcspiderExcelPipeline(object):
    '''
    use Item Exporter
    save the item to excel
    '''

    def __init__(self):
        '''
        initialize the object
        '''
        self.spider = None
        self.count = 0

    def log(self, l):
        '''
        reload the log
        :return:
        '''
        msg = '========== CdcspiderExcelPipeline ==  %s' % l

        if self.spider is not None:
            # spider.logger -> return logging.LoggerAdapter(logger, {'spider': self})
            self.spider.logger.info(msg)

    def open_spider(self, spider):
        '''
        create a queue
        :return:
        '''
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.append(['name', 'url', 'mail'])

    def process_item(self, item, spider):
        '''
        save every
        :return:
        '''
        self.log('process %s, %s:' % (spider.name, self.count + 1))

        line = [item['name'],item['url'],item['mail']]
        self.ws.append(line)
        return item

    def close_spider(self, spider):
        '''
        save lines to excel
        :return:
        '''
        print 'ExcelPipline info:  items size: %s' % self.count
        self.wb.save('result.xls')


