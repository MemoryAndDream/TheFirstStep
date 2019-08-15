# -*- coding: utf-8 -*-
"""
File Name：     web_server
Description :
Author :       meng_zhihao
mail :       312141830@qq.com
date：          2018/12/24
"""
# -*- coding: utf-8 -*-
"""
File Name：     run
Description :
Author :       meng_zhihao
date：          2018/10/10
"""
from flask import Flask,url_for,request,render_template
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from gevent import monkey
from gevent.pywsgi import WSGIServer
import json
monkey.patch_all()
from flask_cors import *
from flask import redirect
import time
from db_connect import BaseDAO
import os

app = Flask(__name__)

CORS(app, supports_credentials=True)

@app.route('/')
def list():
    result_dict = ananlyse_tems()

    return render_template('index.html',result_dict = result_dict)





def ananlyse_tems():
    dx_tems = ['大大大大','大大大小','大大小小','大小小小','大小大小','大小小大','大小大大','大大小大']
    dx_tems2 = ['小小小小','小小小大','小小大大','小大大大','小大小大','小大大小','小大小小','小小大小']
    ds1 = ["单单单单","单单单双","单单双双","单双双双","单双单双","单双双单","单双单单","单单双单"]
    ds2 = ["双双双双","双双双单","双双单单","双单单单","双单双单","双单单双","双单双双","双双单双"]
    result_row = {}
    bao = BaseDAO('47.96.238.217', 3306, 'alcp', 'guest', '123456')
    rows = bao.Query('select data,suan from analyse_data where create_time>date_add(now(), interval-5 day)') # 后面根据性能调整
    for row in rows:
        data, suan = row
        for key in dx_tems+dx_tems2:
            if data[:4] == key:
                if data[4] == '大':
                    result_row[key] = result_row.get(key, []) + ['正']
                else:
                    result_row[key] = result_row.get(key, []) + ['反']

        for key in ds1+ds2:
            if suan[:4] == key:
                if suan[4] == '单':
                    result_row[key] = result_row.get(key, []) + ['正']
                else:
                    result_row[key] = result_row.get(key, []) + ['反']
    min_len = 1000
    for key in result_row:
        row_len = len(result_row[key])
        if row_len<min_len:
            min_len = row_len
    if min_len>10:
        min_len=min_len-10
    for key in result_row:
        result_row[key] = result_row[key][min_len:]


    # for key in result_row:
    #     print result_row[key].
    result_dict={}
    result_dict['dx_tems'] = {}
    result_dict['dx_tems']['rpt'] = []
    result_dict['dx_tems']['diff'] = []
    for key in dx_tems:
        result_dict['dx_tems']['rpt'].append([key]+ result_row[key])

    for i in range(len(dx_tems)):
        data_key = dx_tems[i]
        bro_key = dx_tems[7-i]
        data_list = result_row[data_key]
        bro_list = result_row[bro_key]
        rs = []
        for j in range(len(data_list)):
            if len(bro_list)>j:
                if bro_list[j] == data_list[j]:
                    rs.append(1)
                else:
                    rs.append(0)
        result_dict['dx_tems']['diff'].append([ dx_tems[i]]+ rs)

    result_dict['dx_tems2'] = {}
    result_dict['dx_tems2']['rpt'] = []
    result_dict['dx_tems2']['diff'] = []
    for key in dx_tems2:
        result_dict['dx_tems2']['rpt'].append([key] + result_row[key])

    for i in range(len(dx_tems2)):
        data_key = dx_tems2[i]
        bro_key = dx_tems2[7 - i]
        data_list = result_row[data_key]
        bro_list = result_row[bro_key]
        rs = []
        for j in range(len(data_list)):
            if len(bro_list) > j:
                if bro_list[j] == data_list[j]:
                    rs.append(1)
                else:
                    rs.append(0)
        result_dict['dx_tems2']['diff'].append([dx_tems2[i]] + rs)


    result_dict['ds1'] = {}
    result_dict['ds1']['rpt'] = []
    result_dict['ds1']['diff'] = []
    for key in ds1:
        result_dict['ds1']['rpt'].append([key] + result_row[key])

    for i in range(len(ds1)):
        data_key = ds1[i]
        bro_key = ds1[7 - i]
        data_list = result_row[data_key]
        bro_list = result_row[bro_key]
        rs = []
        for j in range(len(data_list)):
            if len(bro_list) > j:
                if bro_list[j] == data_list[j]:
                    rs.append(1)
                else:
                    rs.append(0)
        result_dict['ds1']['diff'].append([ds1[i]] + rs)

    result_dict['ds2'] = {}
    result_dict['ds2']['rpt'] = []
    result_dict['ds2']['diff'] = []
    for key in ds2:
        result_dict['ds2']['rpt'].append([key] + result_row[key])

    for i in range(len(ds2)):
        data_key = ds2[i]
        bro_key = ds2[7 - i]
        data_list = result_row[data_key]
        bro_list = result_row[bro_key]
        rs = []
        for j in range(len(data_list)):
            if len(bro_list) > j:
                if bro_list[j] == data_list[j]:
                    rs.append(1)
                else:
                    rs.append(0)
        result_dict['ds2']['diff'].append([ds2[i]] + rs)

    print result_dict
    return  result_dict


def reload_data():
    bao = BaseDAO('47.96.238.217', 3306, 'alcp', 'guest', '123456')
    rows = bao.Query('select daxiao,suan from origin_data where id >= 126015') # 后面根据性能调整
    analyse_data = ''
    analyse_suan = ''
    len_num = 0
   # import pdb;pdb.set_trace()
    for row in rows:
        daxiao = row[0]
        suan = row[1]
        # qishus.append(qishu)
        analyse_data += daxiao
        analyse_suan += suan
        len_num += 1
        if len_num == 5:
            bao.insert_analyse_data(analyse_data, analyse_suan)
            analyse_data = ''
            analyse_suan = ''
            len_num = 0



#静态文件在模板里{{ url_for('static', filename='res/sheeta.jpg') }} # 默认就是包里或者应用里static文件夹

if __name__ == '__main__':
    #或者app.debug = True #代码修改了就自动运行
    #app.run(host='0.0.0.0',port=30006,debug=True)

   WSGIServer(('0.0.0.0', 30010), app).serve_forever()
    #ananlyse_tems()


#curl 'https://pub.alimama.com/common/code/getAuctionCode.json?auctionid=579077762277&adzoneid=72044740&siteid=21454360&scenes=1&tkFinalCampaign=1&t=1545037785000' -H 'authority: pub.alimama.com' -H 'pragma: no-cache' -H 'cache-control: no-cache' -H 'upgrade-insecure-requests: 1' -H 'user-agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: zh-CN,zh;q=0.9' -H 'cookie:cookie2=1e8da1d542a164f143cea00531f79ac8' --compressed