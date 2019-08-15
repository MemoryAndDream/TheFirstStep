# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 21:43
# @Author  : meng_zhihao
# @Email   : 312141830@qq.com
# @File    : 1.py
def img_dl(url,img_path):
    import requests
    with open(img_path,'wb') as f:
        print url
        f.write(requests.get(url).content)

img_dl('https://i.ytimg.com/vi/kTJbE3sfvlI/hqdefault.jpg','1.jpg')