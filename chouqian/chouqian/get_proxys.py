# -*- coding: utf-8 -*-
"""
File Name：     get_proxys
Description :
Author :       meng_zhihao
mail :       312141830@qq.com
date：          2018/12/29
"""

from spiders.crawl_tool import crawlerTool as ct
import requests
import time
class MyProxy():

    def __init__(self,check_url):
        url = 'http://www.kuaidaili.com/free/'
        self.check_url = check_url
        self.check_pattern = check_url

    def get_proxy(self):
        valid_proxys = []
        for i in range(5):

            page = ct.get('http://www.kuaidaili.com/free/?page=%s'%(i+1))
            ips = ct.getXpath('//tbody//tr',page)

            for ip in ips :
                tds = ct.getXpath('//td/text()', ip)
                url,port = tds[0],tds[1]
                proxy_url = '%s:%s'%(url,port)
                print 'test',proxy_url
                if self.check_proxy(proxy_url):
                    valid_proxys.append(proxy_url)
        return valid_proxys


    def check_proxy(self,proxy,url=''):
        proxies = {'http':proxy,'https':proxy}
        try:
            if url:
                rp = requests.get(url, timeout=10, proxies=proxies)
            else:
                rp = requests.get(self.check_url,timeout=10,proxies=proxies)
            print rp.text
            if rp.status_code==200:
                print proxy
                return True
            else:
                print rp.status_code,
        except:
            return False

    def check_proxys(self,proxys):
        for proxy in proxys:
            if self.check_proxy(proxy):
                print proxy,'valid'


    def check_proxy_by_time(self,proxy,times=10):
        for i in range(times):
            time.sleep(1)
            print i
            self.check_proxy(proxy,url='https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/%s/JSON/?'%str(18187432+i))


if __name__ == '__main__':
    mp = MyProxy(check_url='https://www.amazon.com/s?k=womendress')
    print mp.get_proxy()
  #  mp.check_proxys()
   # mp.check_proxy_by_time('112.85.168.234:9999',100)
