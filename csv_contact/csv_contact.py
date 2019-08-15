# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 21:01
# @Author  : meng_zhihao
# @Email   : 312141830@qq.com
# @File    : csv_contact.py

import csv

import csv

filename = '1.csv' # 源文件 事先删除第一行
data_rows = []
data_dict = {}
data_dict2 = {}
with open(filename) as f:
    reader = csv.reader(f)
    #print(list(reader))
    for row in reader:
        name = row[1]
        data_dict[name] = row

filename = '2.csv' # 后面的合并文件  事先删除第一行
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[0]
        if name in data_dict and not name in data_dict2:
            data_dict2[name] = name
            data_dict[name] = data_dict[name]+row
filename = '3.csv'
with open(filename,'wb') as f:
    writer = csv.writer(f)
    writer.writerow(["#","Game","Release date","Price","Score rank(Userscore / Metascore)","Owners","Playtime (Median)","Developer(s)","Publisher(s)","name","url","languages","require_os","achievements","types","types_num","score"])
    for name in data_dict:
        writer.writerow(data_dict[name])

        print(name)