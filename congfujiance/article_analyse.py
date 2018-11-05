# -*- coding: utf-8 -*-
"""
File Name：     article_analyse
Description :
Author :       meng_zhihao
date：          2018/11/5
"""
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')
from win32com import client as wc
import docx
import re

if not os.path.exists(u'检测报告'):
    os.mkdir(u'检测报告')

if not os.path.exists(u'tmp'):
    os.mkdir(u'tmp')

# 分析单个文件 生成报告
class ArticleAnalyse:
    def __init__(self,filepath):
        self.filepath = filepath
        pass

    def doc_analyse(self): #最后需要异常处理
        #print 'doc_analyse'
        filepath = self.filepath
        file_name = os.path.basename(filepath)
        if filepath.endswith('DOC') or filepath.endswith('doc'):
            tmp_file_path = os.path.dirname(os.path.abspath(__file__)).decode('GB2312')+ur"\tmp\tmp.docx" #windows 中文路径编码
            self.doc_to_docx(filepath, tmp_file_path)
            filepath = tmp_file_path

        # 提取docx中的文字
        doc = docx.Document(filepath)
        lines = []
        for p in doc.paragraphs:
            lines.append(p.text)
        html_path = os.path.join(u'检测报告\\', '.'.join(file_name.split('.')[:-1])+'.html') # 后面还是单独建个文件夹的好
        self.render_html(html_path,lines)

    def txt_analyse(self):
        filepath = self.filepath
        file_name = os.path.basename(filepath)
        lines = []
        with open(filepath) as f:
            for line in f:
                lines.append(line)
        html_path = os.path.join(u'检测报告\\', '.'.join(file_name.split('.')[:-1])+'.html') # 后面还是单独建个文件夹的好
        self.render_html(html_path,lines)


    def doc_to_docx(self,doc_path, docx_path):
        '''
        把doc文件转成docx文件方便解析
        :return:
        '''
        import pythoncom
        pythoncom.CoInitialize() #  Initialize the COM libraries for the calling thread. 子进程要单独加一个这个 不然报错

        word = wc.Dispatch('Word.Application')
        doc = word.Documents.Open(doc_path)  # 目标路径下的文件
        doc.SaveAs(docx_path, 12, False, "", True, "", False, False, False, False)  # 转化后路径下的文件
        doc.Close()
        word.Quit()

    def render_html(self,html_path,lines):
        with open(html_path,'w') as html:
            print html_path
            html.write('<html>')
            for line in lines:
                html.write(line)
                # 这里可以插入百度识别逻辑了
                html.write('<br/>'+'\n')
            html.write('</html>')


    def baidu_analyse(self,line):
        from baidu_craw import BaiduCraw

        sentences = self.line_split(line)
        while sentences:
            keyword = ''
            while len(keyword)<20 and sentences: # 这里有bug，一行丢掉最后一段算了
                keyword += sentences.pop(0)
                #BaiduCraw().keyword_search(keyword)
            print keyword
        return line

    def line_split(self,line):
        sentences = re.split(u'[,.，。？！]',line)
        for sentence in sentences:
         print sentence


if __name__ == '__main__':
    a = ArticleAnalyse(ur'D:\用户目录\我的文档\GitHub\TheFirstStep\congfujiance\test_docs\1029-1023国学1200JZGA10-10国魏晋南北朝时期最厉害的家族.doc')
    #a.doc_analyse()
    pass
    a.baidu_analyse('蜀国刘备的手下有五大上将。分别是义字当头的关羽、英勇无畏的张飞和常胜将军赵子龙。还有两个就是黄忠老将军与本文的传奇人物__马超。作为刘备五将之一的马超也是有着一段传奇的人生经历。 ')



