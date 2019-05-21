# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 15:24
# @Author  : meng_zhihao
# @Email   : 312141830@qq.com
# @File    : auto_complete.py

from selenium_operate import ChromeOperate

import re
import time

cop_list = []
new_url_list = []
url_couple_dict = {}

def get_Complete_url(url_in):
    url_in = url_in.split('?')[0]
    with open('url_duiying.txt','r') as url_f:
        for line in url_f:
            line = line.strip()
            from_url ,to_url = line.split(',')[:2]
            from_url=   from_url.split('?')[0]
            if url_in == from_url:
                return to_url
    return ''

# with open('url_input.txt' ,'r') as url_f:
#     for line in url_f:
#         line = line.strip()
#         new_url = get_Complete_url(line)
#         if not new_url:
#             url_info =re.search('table=([\w-]+)',line)
#             if not url_info:
#                 url_info =re.search('ProjectToken=([\w-]+)',line)
#             if url_info:
#                 key_id = url_info.group(1)
#                 new_url = 'https://s.cint.com/Survey/Complete?ProjectToken=' + key_id
#         if new_url:
#             print(new_url)
#             cop = ChromeOperate(executable_path=r'chromedriver.exe')
#             cop.open('https://www.lifepointspanel.com/')
#             cop_list.append(cop)
#             new_url_list.append(new_url)

cop = ChromeOperate(executable_path=r'chromedriver.exe')
cop.open('https://www.lifepointspanel.com/')
while True:
    time.sleep(1)
    page_source = cop.driver.page_source
    if '很高兴见到您' in page_source:
        break

page_source = cop.driver.page_source
urls = re.findall('survey-link="(https:.*?)"',page_source)
links = [url for url in urls]

print(links)

for link in links:
#     'https://router.cint.com/survey/AQAAAL7nugAAAAAAmG-5FA@AQAAAHtb29WspZP0tE42GLad1uZV0jb-oDFne7DJ21JKNo_8'
#     'https://enter.ipsosinteractive.com/landingSafe/?0&p=9I8VwQQR6KT91RlcTWSerakvwUwOYIGuf1ut0E6MvFv5/CCCUS%2BQNTV8BeTqu49BDul8iEWIa5lnLxpGitpTwA%3D%3D&routerID=0&id=c9a04bcd-5e9b-ee39-a803-7d8bd15dcd06&groupcode=0001'
# '4eef320a-9dbe-ab3e-53de-04c4162482c1'
#118f40f1-7174-46a1-863f-76a4ed56e23a
# 'https://s.cint.com/Survey/Complete?ProjectToken=118f40f1-7174-46a1-863f-76a4ed56e23a  '
    try:
        cop.open(link)
        time.sleep(5)
        redirect_url = cop.driver.current_url
        time.sleep(20)
        keyid = re.search('(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})',redirect_url)
        if keyid:
            time.sleep(60*15)
            keyid = keyid.group(1)
            result_url = 'https://s.cint.com/Survey/Complete?ProjectToken=' + keyid
            print(result_url)
            cop.open(result_url)

    except Exception as e:
        print(e)
    print('finished')
    cop.quit()







