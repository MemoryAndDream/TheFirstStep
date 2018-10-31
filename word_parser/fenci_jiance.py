# -*- coding: utf-8 -*-
"""
File Name：     fenci_jiance
Description :
Author :       meng_zhihao
date：          2018/10/30
"""
# ! python3
# -*- coding: utf-8 -*-
import os, codecs
import jieba
from collections import Counter

#用来分词统计 看下哪些词可以用来当成机构的区分词
def get_words(txt):
    seg_list = jieba.cut(txt)
    c = Counter()
    for x in seg_list:
        if len(x) > 1 and x != '\r\n':
            c[x] += 1
    print('常用词频度统计结果')
    for (k, v) in c.most_common(100):
        print('%s%s %s  %d' % ('  ' * (5 - len(k)), k, '*' * int(v / 3), v))


if __name__ == '__main__':
    with codecs.open('company_stuff_rank', 'r', 'utf8') as f:
        txt = f.read()
    get_words(txt)
