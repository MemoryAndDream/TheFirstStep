# -*- coding: utf-8 -*-
"""
File Name：     url_convert
Description :
Author :       meng_zhihao
mail :       312141830@qq.com
date：          2018/12/21
"""

import requests
import sys,os
import json
import time

class UrlConvert(object):
    def __init__(self):
        self.cookies = self.get_cookie()

    def get_cookie(self):
        cookie_file_path = 'cookies.json'
        if not os.path.exists(cookie_file_path):
            raise Exception(u'未登录，请先手动登录')
        with open(cookie_file_path) as f:
            cookie_json = f.read()
            self.cookies = json.loads(cookie_json)
          #  print self.cookies

    def get_tkl(self,pid,num_iid):
        adzoneid = pid.split('_')[3]
        siteid = pid.split('_')[2]
        t = int(time.time() * 1000)
        url = "https://pub.alimama.com/common/code/getAuctionCode.json?auctionid=%s&adzoneid=%s&siteid=%s&scenes=1&tkFinalCampaign=1&t=%s" % (
            num_iid, adzoneid, siteid, t)

        headers = {'authority': 'pub.alimama.com','user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','accept-language':'zh-CN,zh;q=0.9',
                   }
        cookies = self.cookies
        print url,headers,cookies
        result = requests.get(url,headers=headers,cookies=cookies,timeout=10).content
        d = json.loads(result)
        #clickUrl = d['data']['clickUrl']
        return d['data']

    def get_item_info(self,num_iid):
      #  print
        url = 'http://item.taobao.com/item.htm?id=%s'%str(num_iid)
        rsp = requests.get(url,headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'})
        rsp_body = rsp.content

if __name__ == '__main__':
    obj = UrlConvert()
    obj.get_cookie()
    print obj.get_tkl('mm_131323015_144850188_44073150424','521477762631')
    # 应该有更多功能 比如商品信息 因为这个是有同类竞品的，要做的比别人好才行
    #

