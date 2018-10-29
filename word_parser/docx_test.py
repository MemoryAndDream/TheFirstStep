# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 22:42
# @Author  : meng_zhihao
# @Email   : 312141830@qq.com
# @File    : docx_test.py
import docx

def docx_try():

    doc=docx.Document(r'C:\Users\ASUS\Desktop\1.docx')
    for p in doc.paragraphs:

        print(p.text)

    for t in doc.tables:

        for r in t.rows:

            for c in r.cells:

                print(c.text)

if __name__ == '__main__':
    docx_try()