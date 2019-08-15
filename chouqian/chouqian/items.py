# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime

class BaseItem(scrapy.Item):
    url = scrapy.Field()
    create_time = scrapy.Field()
    def __init__(self):
        super(self.__class__, self).__init__()
        self['create_time']=datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M')


class ChouqianItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    title = scrapy.Field()
    page_url = scrapy.Field()
    desc = scrapy.Field()
    img_url = scrapy.Field()
    pass


class AlibabaItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    category_id = scrapy.Field()
    QuickDetails = scrapy.Field()


class HxchemItem(scrapy.Item):
    '''
    关于我们
联系人
地　址
邮　编
电　话
手　机
网　址
电子邮件
    '''
    url = scrapy.Field()
    gywm = scrapy.Field()
    lxr = scrapy.Field()
    dz =  scrapy.Field()
    yb =  scrapy.Field()
    dh = scrapy.Field()
    sj = scrapy.Field()
    wz = scrapy.Field()
    dzyj = scrapy.Field()
    name = scrapy.Field()


class ChemicalBook(scrapy.Item):
    '''
    公司名称:
联系电话:
Email:
网址:
产品列表
    '''
    name = scrapy.Field()
    lxdh = scrapy.Field()
    email = scrapy.Field()
    url = scrapy.Field()
    wz = scrapy.Field()
    cplb = scrapy.Field()


class Caymanchem(scrapy.Item):
    cat = scrapy.Field()
    name = scrapy.Field()
    cas = scrapy.Field()
    url = scrapy.Field()
    function = scrapy.Field()


class Trc_Item(scrapy.Item):
    api_name = scrapy.Field()
    ChemicalName = scrapy.Field()
    CASNumber  = scrapy.Field()
    MolFormula = scrapy.Field()
    SearchImg = scrapy.Field()
    Synonyms = scrapy.Field()
    url = scrapy.Field()

class acccorporation_Item(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    MolecularFormula = scrapy.Field()
    MolecularWeight = scrapy.Field()
    image = scrapy.Field()
    cas = scrapy.Field()


class angenechemical_item(scrapy.Item):
    url = scrapy.Field() # 这里用url代替cas


class CmocroItem(scrapy.Item):
    url = scrapy.Field()  # 这里用url代替cas
    mail =  scrapy.Field()
    name =  scrapy.Field()


class ChemspaceItem(scrapy.Item):
    url = scrapy.Field()
    IUPACname = scrapy.Field()
    CAS = scrapy.Field()
    Chemspaceid = scrapy.Field()
    Molformula = scrapy.Field()
    Molweight = scrapy.Field()

class RovathinItem(scrapy.Item):
    url = scrapy.Field()
    cat_no = scrapy.Field()
    product_name =  scrapy.Field()
    cas = scrapy.Field()
    assay = scrapy.Field()

class SeekchemItem(scrapy.Item):
    url = scrapy.Field()
    cas = scrapy.Field()
    name = scrapy.Field()

class ParkersItem(scrapy.Item):
    url = scrapy.Field()
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
    taxcostBasic = scrapy.Field()