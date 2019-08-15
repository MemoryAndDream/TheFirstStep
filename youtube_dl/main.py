# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 18:42
# @Author  : meng_zhihao
# @Email   : 312141830@qq.com
# @File    : main.py

import urllib
from crawl_tool import crawlerTool as ct
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def keyword_search(keyword):
    keywords = urllib.quote(keyword)
    url = 'https://www.youtube.com/results?search_query=' + keywords
    page = ct.get(url)
    imgurl0 = ct.getXpath('//div[@id="img-preload"]/img/@src',page)[0]
    vid = ct.getRegex('i.ytimg.com/vi/(.*?)/',imgurl0)
    video_url = 'https://www.youtube.com/watch?v=' + vid
    print video_url
    return video_url,imgurl0

def extractor_info(video_url):
    page = ct.get(video_url)
    artist = ct.getRegex('歌手.*?[tT]ext":"(.*?)"',page)
    if not artist:
        artist = ct.getRegex('艺术家.*?[tT]ext":"(.*?)"', page)
    if not artist:
        artist = ct.getRegex('"Artist".*?[tT]ext":"(.*?)"', page)

    album = ct.getRegex('专辑.*?[tT]ext":"(.*?)"',page)
    label = ct.getRegex('由以下相关方许可给.*?[tT]ext":"(.*?)"',page)
    if not label: label = ct.getRegex('獲以下人士授權.*?[tT]ext":"(.*?)"',page)
    if not label: label = ct.getRegex('Licensed to YouTube.*?[tT]ext":"(.*?)"',page)
    song =  ct.getRegex('"Song".*?[tT]ext":"(.*?)"',page)
    if not song:
        song = ct.getRegex('"歌曲".*?[tT]ext":"(.*?)"', page)


    title = ct.getRegex(',"title":"(.*?)"',page).replace('\\u0026','&')
    title = re.sub(u"([/\\\\:*?<>|])","",title) # 标题特殊符号过滤
    print title
    return title,artist,album,label,song

def img_dl(url,img_path):
    import requests
    with open(unicode(img_path),'wb') as f:
        print url
        f.write(requests.get(url).content)

if __name__ == '__main__':
    import xlwt
    import datetime

    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = u'result%s.xls'%now
    wbk = xlwt.Workbook(encoding="utf-8")
    sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
    row = 0
    sheet.write(row, 0, u'song')
    sheet.write(row, 1, u'artist')
    sheet.write(row, 2, u'cover')
    sheet.write(row, 3, u'audio')
    sheet.write(row, 4, u'audio_link')
    sheet.write(row, 5, u'label')
    sheet.write(row, 6, u'keyword')

    with open('title_list.txt','r') as f:
        for line in f:
            row += 1
            keyword = line.strip()
            # keyword = keyword.replace(' ','+')
            if not keyword:
                continue
            try:
                video_url,imgurl0 = keyword_search(keyword)
                title, artist, album, label,song = extractor_info(video_url)
                img_path = 'img/'+title+'.jpg'
                imgurl0 = ct.getRegex('(http.*?)\?',imgurl0)
                img_dl(imgurl0,img_path)
            except Exception,e:
                print e
                video_url, imgurl0,title, artist, album, label,song = '','','','','','',keyword
            print(video_url, imgurl0,title, artist, album, label )
            sheet.write(row, 0, song)
            sheet.write(row, 1, artist)
            sheet.write(row, 2, title)
            sheet.write(row, 3, title+'.mp3')
            sheet.write(row, 4, video_url)
            sheet.write(row, 5, label)
            sheet.write(row, 6, keyword)
    wbk.save(filename)

# 需要过滤广告
# 代理需要是香港的，不然不会有中文


