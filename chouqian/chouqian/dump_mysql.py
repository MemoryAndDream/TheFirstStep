# -*- coding: utf-8 -*-
"""
File Name：     dump_mysql
Description :
Author :       meng_zhihao
mail :       312141830@qq.com
date：          2018/12/25
"""

import pipelines
import openpyxl
import sys
import re
import time
class dump_obj(object):
    def __init__(self):
        self.pipeline = pipelines.MysqlPipeline3()

    def get_datas(self):
        items = self.pipeline.get_data_list()
        return items

    def myencode(self,s):
        return s.encode('unicode-escape').decode('string_escape')

    def export_execl(self):
        companys_dict = {}
        total = self.pipeline.get_count()
        page_size = 10000
        page_no = total/page_size+1
        print page_no # test的话就写成1
        chunk_size = 20
        chunck = page_no/chunk_size+1 #100w数据分一个文件
        for j in range(chunck):
            wb = openpyxl.Workbook()
            ws = wb.active
            '''   url = scrapy.Field()
    name = scrapy.Field()
    model = scrapy.Field()
    title = scrapy.Field()
    power = scrapy.Field()
    TopSpeed  = scrapy.Field()
    zerotosixty =  scrapy.Field()
    co2Emissions = scrapy.Field()
    EuroEmissionsStandard = scrapy.Field()
    Fuelconsumption  = scrapy.Field()
    Length =  scrapy.Field()
    Width =  scrapy.Field()
    Torque  =  scrapy.Field()
    Height  =  scrapy.Field()
    EngineSize = scrapy.Field()
    Cylinders = scrapy.Field()
    FuelType = scrapy.Field()
    Seats = scrapy.Field()
    Transmission= scrapy.Field()
    Doors = scrapy.Field()
    taxcostBasic = scrapy.Field()'''
            ws.append(['url','name','model','title','power','TopSpeed','0-60','co2Emissions','EuroEmissionsStandard','Fuelconsumption',
                       'Length','Width','Torque','Height','EngineSize','Cylinders','FuelType','Seats','Transmission','Doors','taxcostBasic'])
            print j
            for i in range(page_no)[j*chunk_size:j*chunk_size+chunk_size]:
                datas = self.pipeline.get_data_list(page_size,i)
                for item in datas:
                    line = [item.get('url'),
                            item.get('name'),
                            item.get('model'),
                            item.get('title'),
                            item.get('power'),
                            item.get('TopSpeed'),
                            item.get('zerotosixty'),
                            item.get('co2Emissions'),
                            item.get('EuroEmissionsStandard'),
                            item.get('Fuelconsumption'),
                            item.get('Length'),
                            item.get('Width'),
                            item.get('Torque'),
                            item.get('Height'),
                            item.get('EngineSize'),
                            item.get('Cylinders'),
                            item.get('FuelType'),
                            item.get('Seats'),
                            item.get('Transmission'),
                            item.get('Doors'),
                            item.get('taxcostBasic'),



                            ]
                    ws.append(line)
                # datas = self.pipeline.get_data_list2(page_size,i)
                # for data in datas:
                #     line = [data[0]
                #             ]
                #     ws.append(line)

                    {"MolFormula": "C\u2083\u2083H\u2083\u2086N\u2082O\u2083", "Synonyms": "",
                     "SearchImg": "https://www.trc-canada.com/prod-img/H945930.png", "api_name": "Benzamide",
                     "url": "https://www.trc-canada.com/prod-img/H945930.png", "CASNumber": "75615-55-3",
                     "ChemicalName": "[R-(R*,R*)]-5-[1-Hydroxy-2-[(1-methyl-3-phenylpropyl)(phenylmethyl)amino]ethyl]-2-(phenylmethoxy)benzamide"}

            # for company_name in companys_dict:
            #     line =companys_dict[company_name][:5]
            #     cplb = companys_dict[company_name][5]
            #     for i in range(len(cplb)/10+1):
            #         print cplb[i*10:10*(i+1)]
            #         line.append('|'.join(cplb[i*10:10*(i+1)]))

            wb.save('parkers.xls') # 有分页的话要加j参数



if __name__ == '__main__':
 #   import pdb;pdb.set_trace()
    obj = dump_obj()
#    datas= obj.get_datas()
    obj.export_execl() # 导出execel非常慢！ 可以定位下是哪个慢，可能是转换数据慢？
    # 不需要去重的情况下最好不用mysql
