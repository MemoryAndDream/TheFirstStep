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
import threadpool
from rend_html import render_html
import math
if not os.path.exists(u'检测报告'):
    os.mkdir(u'检测报告')

if not os.path.exists(u'tmp'):
    os.mkdir(u'tmp')

# 分析单个文件 生成报告
class ArticleAnalyse:
    def __init__(self,filepath):
        self.filepath = filepath
        self.craw_result = []
        pass

    def doc_analyse(self): #最后需要异常处理
        #print 'doc_analyse'
        filepath = self.filepath
        file_name = os.path.basename(filepath)
        if filepath.endswith('DOC') or filepath.endswith('doc'):
            tmp_file_path =ur"C:\Windows\temp\tmp.docx" #windows 中文路径编码
            print tmp_file_path
            self.doc_to_docx(filepath, tmp_file_path)
            filepath = tmp_file_path

        # 提取docx中的文字
        doc = docx.Document(filepath)
        lines = []
        extra_info={}
        extra_info['name']=file_name
        analyse_lines = []
        for p in doc.paragraphs:
            analyse_lines.append(p.text)
        lines = self.multithread_craw(analyse_lines)
        extra_info['word_count']=0
        extra_info['similar_count'] = 0
        for line in lines:
            for sentence in line:
                extra_info['similar_count']+=sentence['similar_count']
                extra_info['word_count'] += sentence['word_count']
        html_path = os.path.join(u'检测报告\\', '.'.join(file_name.split('.')[:-1])+'.html') # 后面还是单独建个文件夹的好
        sum_similar_rate = self.save_html(html_path,lines,extra_info)



        return {"sum_similar_rate":sum_similar_rate,'sum_word_count':extra_info['word_count'] ,'sum_similar_count':extra_info['similar_count']}

    def txt_analyse(self):
        filepath = self.filepath
        file_name = os.path.basename(filepath)
        extra_info={}
        extra_info['name']=file_name
        extra_info['word_count']=0
        extra_info['similar_count'] = 0
        lines = []
        analyse_lines = []
        with open(filepath) as f:
            for line in f:
                analyse_lines.append(line)
        lines = self.multithread_craw(analyse_lines)
        for line in lines:
            for sentence in line:
                extra_info['similar_count'] += sentence['similar_count']
                extra_info['word_count'] += sentence['word_count']
        html_path = os.path.join(u'检测报告\\', '.'.join(file_name.split('.')[:-1])+'.html') # 后面还是单独建个文件夹的好
        sum_similar_rate = self.save_html(html_path,lines,extra_info)
        return {"sum_similar_rate":sum_similar_rate,'sum_word_count':extra_info['word_count'] ,'sum_similar_count':extra_info['similar_count']}

    def multithread_craw(self,lines):
        task_pool = threadpool.ThreadPool(8)
        parms = [([lines[i],i],None) for i in range(len(lines))]
        print parms
        requests = threadpool.makeRequests(self.baidu_analyse, parms)
        for req in requests:
            task_pool.putRequest(req)
        task_pool.wait()
        rs = sorted(self.craw_result,key = lambda d: d['line_no'])
        return [r['result'] for r in rs]


    def doc_to_docx(self,doc_path, docx_path):
        '''
        把doc文件转成docx文件方便解析
        :return:
        '''
        import pythoncom
        pythoncom.CoInitialize() #  Initialize the COM libraries for the calling thread. 子进程要单独加一个这个 不然报错

        word = wc.Dispatch('Word.Application')
        doc = word.Documents.Open(doc_path)  # 目标路径下的文件
        print docx_path
        doc.SaveAs(docx_path, 12, False, "", True, "", False, False, False, False)  # 转化后路径下的文件
        doc.Close()
        word.Quit()

    def save_html(self,html_path,lines,extra_info={}):
        with open(html_path,'w') as html:
            print html_path
            content, sum_similar_rate = render_html(lines,extra_info)
            html.write(content)
            return sum_similar_rate


    def baidu_analyse(self,line,line_no=0):
        from baidu_craw import BaiduCraw
        sentences = self.line_split(line)
        new_line = []
        while sentences:
            keyword = sentences.pop(0)
            while sentences and len(keyword+sentences[0])<= 38: # 这里有bug，一行丢掉最后一段算了
                keyword += sentences.pop(0)
            try:
                keyword.encode('utf8')
                keyword_result = BaiduCraw().keyword_search(keyword.encode('utf8'))
            except:
                keyword_result = BaiduCraw().keyword_search(keyword.decode('GBK').encode('utf8'))
            if not keyword_result:continue
            record,em,sim_url = keyword_result[0]
            score = 0
            try:
                keyword = keyword.decode('utf8')
            except:
                keyword = keyword.decode('GBK')
            keyword = keyword.replace('\n','').replace('\r','')
            for word in keyword:
                if word in em:
                    score+=1
            similar_rate = score*1.0/len(keyword)
            similar_rate =(math.pow(similar_rate*100, 1.5)) / 985
            print keyword,similar_rate,sim_url
            sentence = {}
            sentence['origin_content'] = keyword
            sentence['similar_content'] = record
            sentence['similar_url'] = sim_url
            sentence['similar_rate'] = similar_rate
            sentence['similar_count'] = score
            sentence['word_count'] = len(keyword)

            new_line.append(sentence)
        self.craw_result.append({"line_no":line_no,"result":new_line})
        return new_line

    def line_split(self,line):
        sentences = re.split(u'[,.，。？！]',line)
        split_char = re.findall(u'[,.，。？！]',line)
        new_sentences = [sentences[i]+split_char[i] for i in range(len(sentences)-1)]
        new_sentences.append(sentences[-1])
        return new_sentences


if __name__ == '__main__':
    #a = ArticleAnalyse(ur'D:\github\TheFirstStep\congfujiance\test_docs\1029-1023国学1200JZGA10-10国魏晋南北朝时期最厉害的家族.doc')
    #a.doc_analyse()
    a = ArticleAnalyse(ur'D:\github\TheFirstStep\congfujiance\test_docs\1.txt')
    a.txt_analyse()
    pass
    #a.baidu_analyse(u'蜀国刘备的手下有五大上将。分别是义字当头的关羽、英勇无畏的张飞和常胜将军常山赵子龙。还有两个就是黄忠老将军与本文的传奇人物__马超。作为刘备五将之一的马超也是有着一段传奇的人生经历。 ')


#congfujiance/检测报告/1029-1023国学1200JZGA10-10国魏晋南北朝时期最厉害的家族.html