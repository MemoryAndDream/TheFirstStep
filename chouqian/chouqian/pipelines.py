# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import settings
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import json
import time

class MysqlPipeline3(object):
    '''
    CREATE TABLE IF NOT EXISTS spider (id bigint(20) PRIMARY KEY AUTO_INCREMENT,unique_value varchar(250) not null ,
    json_data TEXT,unique INDEX(unique_value)) ENGINE = InnoDB

    '''
    #
    '''
    CREATE TABLE IF NOT EXISTS error_log (id bigint(20) PRIMARY KEY AUTO_INCREMENT,unique_value varchar(250) not null ,
    json_data TEXT) ENGINE = InnoDB
    '''
    def __init__(self):
        # 连接数据库
        self.table_name = 'spider_test'
        self.connect()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def connect(self):
        self.conn = MySQLdb.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.conn.cursor();


    def process_item(self, item, spider):
        json_data = json.dumps(dict(item))
        unique_value = item['url'] # 默认用url区分
        website_domain = spider.crawler.spidercls.name # 有很多好东西
        self.insert_into_table(unique_value,json_data,website_domain)
        return item

    def insert_into_table(self, unique_value,json_data,website_domain):
        try:
            # sql =  'replace into '+self.table_name +'(unique_value,json_data,website_domain) values(%s,%s,%s)'
            # values=(
            #     unique_value,json_data,website_domain
            #        )
            # 大数据时
            sql =  'replace into '+self.table_name +'(unique_value,json_data) values(%s,%s)'
            values=(
                unique_value,
                json_data
                   )
            self.cursor.execute(sql,values)
            self.conn.commit()
        except Exception,e:
            print str(e)
            if 'gone away' in str(e):
                time.sleep(10)
                self.connect()

    def get_data_list(self,page_size=1000,page_no=0):
        cursor = self.cursor
        sql =  'select json_data from %s limit %s,%s'%(self.table_name ,page_size*page_no,page_size) # offectset limit
        cursor.execute(sql)
        rows = self.cursor.fetchall()
        return [self._row_to_dict(row) for row in rows if row]

    def get_data_list2(self,page_size=1000,page_no=0):
        cursor = self.cursor
        sql =  'select unique_value from %s where id limit %s,%s'%(self.table_name ,page_size*page_no,page_size) # offectset limit
        cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def get_count(self):
        cursor = self.cursor
        sql =  'select count(*) from %s where id '%self.table_name # offectset limit
        cursor.execute(sql)
        row = self.cursor.fetchone()
        return row[0]

    def get_by_unique_value(self,unique_value):
        cursor = self.cursor
        sql =  'select * from %s where unique_value=%%s '%self.table_name # offectset limit
        values = (
            unique_value,

        )
        cursor.execute(sql,values)
        rows = self.cursor.fetchall()
        return rows

    def _row_to_dict(cls,row):
        (json_data,) = row
        doc = {}
        try:
            doc = json.loads(json_data)
        except:
            print json_data
        return doc




class MysqlPipeline4(object):
    '''
    CREATE TABLE IF NOT EXISTS spider (id bigint(20) PRIMARY KEY AUTO_INCREMENT,unique_value varchar(250) not null ,
    json_data TEXT,unique INDEX(unique_value)) ENGINE = InnoDB

    '''
    #记录访问过的东西
    '''
CREATE TABLE `requested_url` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(500) NOT NULL,
  `website_domain` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
    '''
    def __init__(self):
        # 连接数据库
        self.conn = MySQLdb.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.conn.cursor();

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def insert_into_table(self, url,website_domain):
        sql =  'replace into requested_url(url,website_domain) values(%s,%s)'
        values=(
            url, website_domain
               )
        self.cursor.execute(sql,values)
        self.conn.commit()

    def get_data_list(self,url,website_domain=''):
        cursor = self.cursor
        sql =  'select * from requested_url where url='+url # offectset limit
        cursor.execute(sql)
        rows = self.cursor.fetchall()
        return [self._row_to_dict(row) for row in rows]


    def _row_to_dict(cls,row):
        (id,url,domain) = row
        return id

