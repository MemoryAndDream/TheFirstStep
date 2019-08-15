#! /usr/bin/python
#coding=utf8
import MySQLdb 
import re  
import os  
import shutil 
import logging 
import logging.handlers 
import time 
import string
import sys
import datetime

reload(sys)
sys.setdefaultencoding('utf8')
class BaseDAO:
    table_name1='origin_data'
    table_name2 = 'analyse_data'
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.logger = logging.getLogger(__name__)
        self.connect()

    def connect(self):
        self.logger.debug('connect db')
        try:
            self.conn = MySQLdb.connect(host=self.host, port=self.port, db=self.database, user=self.user, passwd=self.password,charset="utf8")
        except Exception, e:
            print('%s, %s' % (type(e), e))



    def Close(self):
        self.conn.cursor().close()
        self.conn.close()
    
    def Query(self, sql):
      for _ in range(1):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Exception, e:
            print('%s' % (sql))
            print('%s, %s' % (type(e), e))
        

    def Update(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            return
        except Exception, e:
            print ('%s' % (sql))
            print('%s, %s' % (type(e), e))
            self.connect()


    def create_table_1(self):
        cursor = self.conn.cursor()
        conn = self.conn
        query = """ CREATE TABLE IF NOT EXISTS %s (\
            id bigint(20) PRIMARY KEY AUTO_INCREMENT,
            qishu varchar(20),
            origin_data varchar(100) not null,
            daxiao varchar(10) not null,
            popstatus int DEFAULT 0,
            suan varchar(5),
            unique INDEX(qishu)
            ) ENGINE = InnoDB default charset utf8
        """ % self.table_name1


        cursor.execute(query)
        conn.commit()
        self.Close()

    def insert_origin_data(self,qishu,origin_data):
        daxiao = '大' if sum([int(x) for x in origin_data.split(',')])>=11 else '小'
        suan = '双' if sum([int(x) for x in origin_data.split(',')]) % 2 == 0 else '单'
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_format = 'replace into %s(qishu,origin_data,daxiao,suan,create_time) values("%s","%s","%s","%s","%s")' % (self.table_name1,qishu,origin_data,MySQLdb.escape_string(daxiao),suan,now)
        self.Update(sql_format)

    def get_qishu(self,qishu):
        sql_format = 'select * from %s where qishu="%s"'%(self.table_name1,qishu)
        data = self.Query(sql_format)
        return data

    def insert_analyse_data(self,data,suan):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql_format = 'insert into %s(data,suan,create_time) values("%s","%s","%s")' % (self.table_name2,data,suan,now)
        self.Update(sql_format)

if __name__ == '__main__':
    bao = BaseDAO('47.96.238.217',3306,'alcp','guest','123456')
    bao.create_table_1()