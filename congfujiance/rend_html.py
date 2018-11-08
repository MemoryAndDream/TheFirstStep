# -*- coding: utf-8 -*-
"""
File Name：     rend_html
Description :
Author :       meng_zhihao
date：          2018/11/7
"""
# 用于生成检测报告 后面要美化啥的也要用这个来改
from jinja2 import Template

template_str = u'''
<html>
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <title>分析报告</title>
</head>
<div >

<div class="artical f16" style="width:50%;float:left">
    <div class="tit_detail" style="padding:0 5px 40px 5px">
		<span class="block a_left f12 reportinfo tahoma"> <b class="f14">查重检测</b><br>
			<b><span class="vpcs-tips">检测结果： </span></b>总相似比：<b class="red tahoma">{{sum_similar_rate}}%</b><br>
			<b><span class="vpcs-tips">操作提示： </span></b>鼠标滑过带有颜色的文字查看相似片段详情 点击跳转相似内容位置
		</span>
    </div>
    <div class="detail">

{% for line in lines %}
        {% for sentence in line %}
            <a href="{{sentence.similar_url}}"  target="_blank" 
                 data-similar="{{sentence.similar_content}}" onmouseover="overShow(this)"><span style="color:{% if sentence.similar_rate>0.7 %}
                    red
                    {% elif sentence.similar_rate>0.4 %}
                    orange
                    {% else %}
                    green
                {% endif %}">{{sentence.origin_content}}</span></a><br/>
                <br/>
        {% endfor %}
{% endfor %}

</div>
</div>
<div class="side_bar" style="width:45%;float:left;padding:130px 20px 40px 5px">

    <div class="content">
        <div class="content-fixed" style="position: fixed;top:202px;">
            <div class="content-fixed1" id="show_similar">
                
            </div>
        </div>
    </div>

</div>
</div>
</body>
<script>

     function overShow(e) {
  var showDiv = document.getElementById('show_similar');
  //showDiv.style.left = event.clientX;
  //showDiv.style.top = event.clientY;
  //showDiv.style.display = 'block';
  showDiv.innerHTML = e.dataset.similar;
 }



</script>
</html>

'''


def render_html(lines):
    '''每一行数据都是一个dict'''
    template = Template(template_str)
    # 这里相似比计算就取平均算了
    sentence_count = 0
    similar_rate_sum = 0
    for line in lines:
        for sentence in line:
            similar_rate_sum += sentence['similar_rate']
            sentence_count+=1
    sum_similar_rate = round(100*similar_rate_sum/sentence_count,1) if sentence_count else 0
    rsp = (template.render(lines=lines,sum_similar_rate = sum_similar_rate ))
    return rsp,sum_similar_rate


if __name__ == '__main__':
    pass
    lines = []
    sentences = []
    sentence = {}
    sentence['origin_content'] = u'无人敢出面指责,但是司马昭却不敢称帝,还自己找了个曹家子孙当了魏元帝'
    sentence['similar_content'] = u'无人敢出面指责,但是司马昭却不敢称帝,还放了魏元帝'
    sentence[
        'similar_url'] = 'http://www.baidu.com/link?url=FBneBZXWW6kInMuLKdrQv6pbxCTCuTFA0xTE1e-fCSLOhFUOd8QGyUlKZ7uBgO_srQZFJFKf7mKWUP_fAPuXev29hVoGS0VkwDfoMSMMfPO'
    sentence['similar_rate'] = 0.658
    sentences.append(sentence)
    lines.append(sentences)
    render_html(lines)
