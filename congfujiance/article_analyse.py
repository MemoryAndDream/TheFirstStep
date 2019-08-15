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
from rend_html import render_html,render_html2
import datetime
import math
import zipfile
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
        extra_info['createtime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        analyse_lines = []
        word_count = 0
        for p in doc.paragraphs:
            word_count+=len(p.text)
            if word_count >5000:
                break
            analyse_lines.append(p.text)
        lines = self.multithread_craw(analyse_lines)
        extra_info['word_count']=0
        extra_info['similar_count'] = 0

        ref_dict = {}

        for line in lines:
            extra_info['similar_count'] += line['similar_count']
            extra_info['word_count'] += line['word_count']
            for similar_data in line['similar_datas']:
                title = similar_data['title']
                similar_count = similar_data['similar_count']
                ref_dict[title] = ref_dict.get(title,0) + similar_count
        ref_list = [{'title':title,'similar_count':round(ref_dict[title]*100.0/extra_info['word_count'] if extra_info['word_count'] else 0,2) } for title in ref_dict]
        ref_list = sorted(ref_list, key=lambda d: d['similar_count'],reverse=True)
        extra_info['ref_list'] = ref_list
        html_path = os.path.join(u'检测报告\\', '.'.join(file_name.split('.')[:-1])+'.html') # 后面还是单独建个文件夹的好
        sum_similar_rate = self.save_html(html_path,lines,extra_info)
        return {"sum_similar_rate":sum_similar_rate,'sum_word_count':extra_info['word_count'] ,'sum_similar_count':extra_info['similar_count']}

    def txt_analyse(self):
        filepath = self.filepath
        file_name = os.path.basename(filepath)
        extra_info={}
        extra_info['name']=file_name
        extra_info['word_count']=0
        extra_info['similar_rate'] = 0
        extra_info['similar_count'] = 0
        lines = []
        analyse_lines = []
        word_count = 0
        with open(filepath) as f:
            for line in f:
                analyse_lines.append(line)
                word_count += len(line)
                if word_count > 5000:
                    break
        lines = self.multithread_craw(analyse_lines)
        ref_dict = {}

        for line in lines:
            extra_info['similar_count'] += line['similar_count']
            extra_info['word_count'] += line['word_count']
            for similar_data in line['similar_datas']:
                title = similar_data['title']
                similar_count = similar_data['similar_count']
                ref_dict[title] = ref_dict.get(title, 0) + similar_count
        ref_list = [{'title': title, 'similar_count': round(ref_dict[title]*100.0/extra_info['word_count'] if extra_info['word_count'] else 0,2)} for title in ref_dict]
        ref_list = sorted(ref_list, key=lambda d: d['similar_count'], reverse=True)
        extra_info['ref_list'] = ref_list
        html_path = os.path.join(u'检测报告\\', '.'.join(file_name.split('.')[:-1]) + '.html')  # 后面还是单独建个文件夹的好
        sum_similar_rate = self.save_html(html_path, lines, extra_info)
        return {"sum_similar_rate":sum_similar_rate,'sum_word_count':extra_info['word_count'] ,'sum_similar_count':extra_info['similar_count']}

    def multithread_craw(self,lines):
        task_pool = threadpool.ThreadPool(32) #速度调节
        parms = [([lines[i],i],None) for i in range(len(lines))]
        print parms
        requests = threadpool.makeRequests(self.baidu_analyse, parms)
        for req in requests:
            task_pool.putRequest(req)
        task_pool.wait()
        rs = sorted(self.craw_result,key = lambda d: d['line_no'])
        return rs # "origin_data":line,"similar_data":new_line


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
        html_path1 = html_path.replace(u'.html',u'文本复制检测报告单（全文对照）.html')
        html_path2 = html_path.replace(u'.html',u'文本复制检测报告单（全文标明引文）.html')
        with open(html_path1,'w') as html:
            content, sum_similar_rate = render_html(lines,extra_info)
            html.write(content)
        with open(html_path2,'w') as html:
            content, sum_similar_rate = render_html2(lines,extra_info)
            html.write(content)
        self.make_tmp_dir([html_path1,html_path2])
        self.zip_dir('tmp',html_path.replace(u'.html',u'.zip'))
        return sum_similar_rate

    def make_tmp_dir(self,files,dest='tmp'):
        import shutil
        shutil.rmtree("tmp")
        os.mkdir(u'tmp')
        shutil.copytree("static", r"tmp\static")
        for file in files:
            shutil.copy(file, r"tmp")
            os.remove(file)





    def zip_dir(self,dirname, zipfilename): # 打包一整个文件夹
        filelist = []
        if os.path.isfile(dirname):
            filelist.append(dirname)
        else:
            for root, dirs, files in os.walk(dirname):
                for name in files:
                    filelist.append(os.path.join(root, name))
        zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
        for tar in filelist:
            arcname = tar[len(dirname):]
            # print arcname
            zf.write(tar, arcname)
        zf.close()


    def baidu_analyse(self,line,line_no=0):
        # 分析一行语句
        from baidu_craw import BaiduCraw
        sentences = self.line_split(line)
        try:
            line = line.decode('utf8')
        except:
            line = line.decode('GBK')
        if not line.strip():
            return
        sentence_results = []
        origin_line = ''
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
            record,em,sim_url,title = keyword_result[0]


            score = 0
            try:
                keyword = keyword.decode('utf8')
            except:
                keyword = keyword.decode('GBK')
            keyword = keyword.replace('\n','').replace('\r','')
            for word in keyword:
                if word in em:  # 判断相似 连续标红长度大于
                    score+=1
            similar_rate = score*1.0/len(keyword)
            if similar_rate>0.3:
                origin_line += '<em>' + keyword + '</em>'
            else:
                origin_line += keyword
            print keyword,similar_rate,sim_url
            sentence = {}
            sentence['origin_content'] = keyword
            sentence['similar_content'] = record
            sentence['similar_url'] = sim_url
            sentence['similar_count'] = score
            sentence['title'] = title
            sentence['word_count'] = len(keyword)
            sentence_results.append(sentence)

        title_dict = {}
        for sentence in sentence_results:
            title = sentence['title']
            if not title in title_dict:
                title_dict[title] = sentence
            else:
                title_dict[title]['similar_content'] += '\n' + sentence['similar_content']
                title_dict[title]['similar_count'] += sentence['similar_count']
        titles_data = [title_dict[title] for title in title_dict]

        new_line = {}
        similar_datas = sorted(titles_data, key=lambda d:d['similar_count'] , reverse=True)
        new_line['similar_datas'] = similar_datas
        new_line['origin_content'] = origin_line
        new_line["similar_count"] = 0
        for data in similar_datas:
            new_line["similar_count"] += data['similar_count']
        new_line['word_count'] = len(line)
        new_line['line_no'] = line_no
        self.craw_result.append(new_line)
        return new_line

    def line_split(self,line):
        sentences = re.split(u'[,.，。？！]',line)
        split_char = re.findall(u'[,.，。？！]',line)
        new_sentences = [sentences[i]+split_char[i] for i in range(len(sentences)-1)]
        new_sentences.append(sentences[-1])
        return new_sentences


if __name__ == '__main__':

    a = ArticleAnalyse(ur'F:\work\aliyun_meng\TheFirstStep\congfujiance\test_docs\1029-1023国学1200JZGA03-10五虎上将-马超.doc')
    a.doc_analyse()
    # a = ArticleAnalyse(ur'F:\github\TheFirstStep\congfujiance\test_docs\1.txt')
    # a.txt_analyse()
    pass
    #a.baidu_analyse(u'蜀国刘备的手下有五大上将。分别是义字当头的关羽、英勇无畏的张飞和常胜将军常山赵子龙。还有两个就是黄忠老将军与本文的传奇人物__马超。作为刘备五将之一的马超也是有着一段传奇的人生经历。 ')


#congfujiance/检测报告/1029-1023国学1200JZGA10-10国魏晋南北朝时期最厉害的家族.html