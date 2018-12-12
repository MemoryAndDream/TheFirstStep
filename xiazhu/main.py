# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 23:25
# @Author  : meng_zhihao
# @Email   : 312141830@qq.com
# @File    : main.py
import requests
import time
import json

se = requests.session()

se.post('http://www.alcp118.com/api?Login' ,data={"Action":"Login","UserName":"tb07949","Password":"123456","SourceType":1},timeout=10)

while True:
    rs = se.get('http://www.alcp118.com/api?GetLotteryOpen',data={"Action":"GetLotteryOpen","LotteryCode":1407,"IssueNo":0,"DataNum":10,"SourceType":1})
    print rs.content
    response = rs.text
    data_dict=json.loads(response)
    BackDatas = data_dict['BackData']
    for data in BackDatas:
        print data['IssueNo'],data['LotteryOpen']
    # 获取最近10条数据，可以插入数据库
    time.sleep(60)
