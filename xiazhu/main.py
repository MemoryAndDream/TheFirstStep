# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 23:25
# @Author  : meng_zhihao
# @Email   : 312141830@qq.com
# @File    : main.py
import requests
import time
import json
from db_connect import BaseDAO
import sys
se = requests.session()

  # 连接貌似最久8小时
# 好像不能重复登录
qishus = []
len_num = 0
analyse_data = ''
analyse_suan = ''
while True:
    try:
        bao = BaseDAO('47.96.238.217', 3306, 'alcp', 'guest', '123456')
        try:
            se.post('http://www.alcp118.com/api?Login' ,data={"Action":"Login","UserName":"tb07949","Password":"123456","SourceType":1},timeout=10)
        except Exception,e:
            print str(e)


        for i in range(5): #暂定10分钟重连一次 因为一次能返回10分钟的数据

            try:
                rs = se.get('http://www.alcp118.com/api?GetLotteryOpen',data={"Action":"GetLotteryOpen","LotteryCode":1407,"IssueNo":0,"DataNum":10,"SourceType":1})
                print rs.content
                response = rs.text
                data_dict=json.loads(response)
                BackDatas = data_dict['BackData']
                BackDatas.reverse()
                for data in BackDatas:
                    print data['IssueNo'],data['LotteryOpen']
                    qishu = data['IssueNo']

                    origin_data = data['LotteryOpen']
                    daxiao = '大' if sum([int(x) for x in origin_data.split(',')]) >= 11 else '小'
                    suan = '双' if sum([int(x) for x in origin_data.split(',')]) %2 == 0 else '单'
                    if not bao.get_qishu(qishu):
                        bao.insert_origin_data(qishu, origin_data)
                        #qishus.append(qishu)
                        analyse_data += daxiao
                        analyse_suan += suan
                        len_num += 1
                        if len_num==5:
                            bao.insert_analyse_data(analyse_data, analyse_suan)
                            analyse_data = ''
                            analyse_suan = ''
                            len_num=0
                # if len(qishus)>1000:
                #     qishus = qishus[-1000:]

            except:
                pass

            # 获取最近10条数据，可以插入数据库
            time.sleep(60)
        bao.Close()
    except Exception,e:
        print str(e)

