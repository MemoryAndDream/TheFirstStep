# -*- coding: utf-8 -*-
"""
File Name：     rend_html
Description :
Author :       meng_zhihao
date：          2018/11/7
"""
# 用于生成检测报告 后面要美化啥的也要用这个来改
from jinja2 import Template
import cgi
template_str = u'''

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>report</title>
    <!-- <script src="https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.min.js"></script> -->
    <script src="https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"></script>
</head>

<body>
  {% raw %}
    <div id="app">
        <div class="n_title">
            <div class="n_print">

            </div>
            <table width="640" border="0" cellspacing="0" cellpadding="0">
                <tbody>
                    <tr>
                        <td class="n_logo_left">
                            <a href="http://check.cnki.net/" target="_blank">
                                <img alt="" src="./static/jie_amlc.gif">
                            </a>
                        </td>
                        <td class="n_logo_right">
                            <a href="http://check.cnki.net/" target="_blank">
                                <img alt="" src="./static/jie_zw.gif">
                            </a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="n_bodytop">
            <div class="n_bt">文本复制检测报告单<span class="n_jie">(<span id="Label_Report_Type_Name">全文对照</span>)</span>
            </div>
            <table width="100%" class="n_table_a"
                style="border-top-color: rgb(3, 93, 3); border-top-width: 2px; border-top-style: solid;" border="0"
                cellspacing="0" cellpadding="0">
                <tbody>
                    <tr class="n_table_a_cos">
                        <td colspan="2">
                            <table width="640" border="0" cellspacing="0" cellpadding="0">
                                <tbody>
                                    <tr>
                                        <td width="420" class="n_text_red_a">№:<span
                                                id="Label_ReportID">{{report_number}}</span>

                                        </td>
                                        <td width="60" class="t_text_red_a">检测时间：
                                        </td>
                                        <td><span id="Label_Apply_Time">{{createtime}}</span>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="padding-left: 10px;" colspan="3"><span
                                                class="t_text_red_a">检测单位：</span><span id="Label_Company"></span>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td class="n_text_green" style="width: 100px;">检测文献：
                        </td>
                        <td class="n_text_block_a" style="width: 539px;"><span
                                id="Label_Title">{{article_name}}</span>
                        </td>
                    </tr>
                    <tr>
                        <td class="n_text_green" style="width: 100px;">作者：
                        </td>
                        <td class="n_text_block_a"><span id="Label_Author">{{article_author}}</span>
                        </td>
                    </tr>
                    <tr>
                        <td class="n_text_green" style="width: 100px; vertical-align: top;">检测范围：
                        </td>
                        <td class="n_text_block_bm"><span
                                id="Label_Check_Range">中国学术期刊网络出版总库<br>中国博士学位论文全文数据库/中国优秀硕士学位论文全文数据库<br>中国重要会议论文全文数据库<br>中国重要报纸全文数据库<br>中国专利全文数据库<br>图书资源<br>优先出版文献库<br>互联网资源(包含贴吧等论坛资源)<br>英文数据库(涵盖期刊、博硕、会议的英文数据以及德国Springer、英国Taylor&amp;Francis
                                期刊数据库等)<br>港澳台学术文献库<br>互联网文档资源<br>CNKI大成编客-原创作品库<br>个人比对库</span>
                        </td>
                    </tr>
                    <tr>
                        <td class="n_text_green" style="width: 100px;">时间范围：
                        </td>
                        <td class="n_text_block_a"><span id="Label_Time_Range">{{time_range}}</span>
                        </td>
                    </tr>
                </tbody>
            </table>
            <div class="item_title">检测结果 </div>
            <div class="n_bgd_k2">
                <table width="640" class="n_table_b" id="p1" border="0" cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr class="n_table_b_cos">
                            <td width="95" class="n_text_red_a" v-for="item in report_result">
                                {{item.key}}{{item.value}}
                            </td>
                        </tr>
                    </tbody>
                </table>
                <table width="640" id="Table2" border="0" cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr class="n_table_b_cos">
                            <td width="26" height="25"><img style="border: currentColor; border-image: none;" alt=""
                                    src="./static/jie_yins.gif">
                            </td>
                            <td width="184" class="n_text_block_b6">去除引用文献复制比：<span class="n_red_bold"><span
                                        id="Label_Quote">23.5%</span></span>
                            </td>
                            <td width="27"><img style="border: currentColor; border-image: none;" alt=""
                                    src="./static/jie_bens.gif">
                            </td>
                            <td class="n_text_block_b6">去除本人已发表文献复制比：<span class="n_red_bold"><span
                                        id="Label_SameAuthor">27%</span></span>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <table width="640" id="Table3" border="0" cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr class="n_table_b_cos">
                            <td width="26"><img style="border: currentColor; border-image: none;" alt=""
                                    src="./static/jie_dans.gif">
                            </td>
                            <td class="n_text_block_b6" colspan="3">单篇最大文字复制比：<span class="n_red_bold"><span
                                        id="Label_Single_Max_Similar">5.9%</span></span><a class="maxlink"
                                    id="HyperLink_MaxCopy" target="_blank"></a> </td>
                        </tr>
                    </tbody>
                </table>
                <table width="640" class="n_table_a1" border="0" cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr class="n_qubr_fzb">
                            <td width="52" height="25" class="n_text_Gm">&nbsp;
                            </td>
                            <td width="158" class="n_text_Gm">重复字数：<span
                                    class="n_text_block_bss">&nbsp;&nbsp;&nbsp;&nbsp;[&nbsp;<span
                                        id="Label_All_CopyWords">776</span>
                                    &nbsp;]</span>
                            </td>
                            <td width="176" class="n_text_Gm">总字数：<span
                                    class="n_text_block_bss">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[&nbsp;<span
                                        id="Label_All_Words">2869</span>&nbsp;]</span>
                            </td>
                            <td width="133" class="n_text_Gm"><span id="Label1">单篇最大重复字数：</span>
                            </td>
                            <td width="110" class="n_text_Gm"><span class="n_text_block_bss">[&nbsp;<span
                                        id="Label_Single_Max_Length">168</span>&nbsp;]</span>
                            </td>
                        </tr>
                        <tr class="n_qubr_fzb">
                            <td width="52" height="25" class="n_text_Gm">&nbsp;
                            </td>
                            <td width="158" class="n_text_Gm">总段落数：<span
                                    class="n_text_block_bss">&nbsp;&nbsp;&nbsp;&nbsp;[&nbsp;<span
                                        id="Label_All_Section">1</span>
                                    &nbsp;]</span>
                            </td>
                            <td width="176" class="n_text_Gm">前部重合字数：<span class="n_text_block_bss">[&nbsp;<span
                                        id="lb_qcf">267</span>&nbsp;]</span>
                            </td>
                            <td width="133" class="n_text_Gm"><span id="Label2">疑似段落最大重合字数：</span>
                            </td>
                            <td width="110" class="n_text_Gm"><span class="n_text_block_bss">[&nbsp;<span
                                        id="lb_yszdcf">776</span>&nbsp;]</span> </td>
                        </tr>
                        <tr class="n_qubr_fzb">
                            <td width="52" height="25" class="n_text_Gm">&nbsp;
                            </td>
                            <td width="158" class="n_text_Gm">疑似段落数：<span class="n_text_block_bss">[&nbsp;<span
                                        id="lb_yszj">1</span>
                                    &nbsp;]</span> </td>
                            <td width="176" class="n_text_Gm">后部重合字数：<span class="n_text_block_bss">[&nbsp;<span
                                        id="lb_hcf">509</span>&nbsp;]</span>
                            </td>
                            <td width="243" class="n_text_Gm" colspan="2">
                                <div id="danpian">疑似段落最小重合字数：&nbsp;<span class="n_text_block_bss">[&nbsp;<span
                                            id="lb_yszxcf">776</span>&nbsp;]</span>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <table width="640" class="n_table_a2" border="0" cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr class="n_qubr_fzb">
                            <td width="101" height="25" class="n_text_red_a_zb">指&nbsp;&nbsp;&nbsp;&nbsp;标：
                            </td>
                            <td width="20"><img id="Image_Standard5" style="border-width: 0px;" src="./static/wu.gif">
                            </td>
                            <td width="80" class="n_text_Gm">疑似剽窃观点 </td>
                            <td width="20"><img id="Image_Standard4" style="border-width: 0px;" src="./static/you.gif">
                            </td>
                            <td width="80" class="n_text_Gm ">疑似剽窃文字表述 </td>
                            <td width="20"><img id="Image_Standard3" style="border-width: 0px;" src="./static/wu.gif">
                            </td>
                            <td width="80" class="n_text_Gm ">疑似自我剽窃 </td>
                            <td width="20"></td>
                            <td class="n_text_Gm "></td>
                        </tr>
                        <tr class="n_qubr_fzb">
                            <td>&nbsp; </td>
                            <td><img id="Image_Standard6" style="border-width: 0px;" src="./static/wu.gif">
                            </td>
                            <td class="n_text_Gm">一稿多投 </td>
                            <td><img id="Image_Standard7" style="border-width: 0px;" src="./static/wu.gif">
                            </td>
                            <td class="n_text_Gm">过度引用 </td>
                            <td><img id="Image_Standard1" style="border-width: 0px;" src="./static/wu.gif">
                            </td>
                            <td class="n_text_Gm ">疑似整体剽窃 </td>
                            <td width="20"><img id="Image_Standard2" style="border-width: 0px;" src="./static/wu.gif">
                            </td>
                            <td class="n_text_Gm">重复发表
                            </td>
                        </tr>
                    </tbody>
                </table>
                <table width="640" class="n_table_a3" border="0" cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr>
                            <td width="101" class="n_table_a3_l">表格： </td>
                            <td width="73" class="n_table_a3_r"><span id="Label_Table_Number">0</span>
                            </td>
                            <td width="90" class="n_table_a3_l">脚注与尾注： </td>
                            <td width="237" class="n_table_a3_r"><span id="Label_Note_Number">0</span>
                            </td>
                            <td width="117" class="n_table_a3_l">&nbsp; </td>
                            <td width="22" class="n_table_a3_r">&nbsp;
                            </td>
                        </tr>
                    </tbody>
                </table>
                <table class="n_table_a" border="0" cellspacing="0" cellpadding="0"></table>
                <div class="n_k3" id="imgdiv">
                    <div class="n_pic"><img id="Image1" style="border-width: 0px;" src="./static/RedImage5AZJL5B7.png">
                    </div>
                    <table width="640" class="n_table_zs" border="0" cellspacing="0" cellpadding="0">
                        <tbody>
                            <tr id="huanse">
                                <td class="n_text_block_b">（注释： </td>
                                <td width="6"><img alt="" src="./static/20120320_b.gif" border="0">
                                </td>
                                <td width="150" class="n_text_block_b">无问题部分
                                </td>
                                <td width="6"><img alt="" src="./static/20120320_c.gif" border="0">
                                </td>
                                <td width="150" class="n_text_block_b">文字复制比部分
                                </td>
                                <td width="6"><img alt="" src="./static/20120320_a.gif" border="0">
                                </td>
                                <td width="150" class="n_text_block_b">引用部分）
                                </td>
                                <td width="60" class="n_text_block_b"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="n_bodymid">
            <div class="n_bodymid_bf">
                <table width="640" class="n_table_jiebf" border="0" cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr>
                            <td width="25" height="30" class="n_bf_bt">
                            </td>
                            <td width="499" class="n_text_block_bs"><a name="65166928_000"></a>
                                {{report_reference.reference_title}}
                            </td>
                            <td width="116" class="n_table_jiebf_zzs">总字数：<span
                                    class="n_text_block_bs">{{report_reference.reference_wordnumber}}</span>
                            </td>
                        </tr>
                        <tr>
                            <td colspan="3">
                                <table width="640" class="n_table_jiebfs" border="0" cellspacing="0" cellpadding="0">
                                    <tbody>
                                        <tr>
                                            <td width="90" style="text-indent: 1em;">相似文献列表
                                            </td>
                                            <td width="150" class="n_table_jiebf_fzb"
                                                v-for="item in report_reference.reference_data">
                                                {{item.key}}{{item.value}}
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <div class="n_xu" v-for="(item,index) in report_reference.reference_list">
                    <table class="n_table_a" border="0" cellspacing="0" cellpadding="0">
                        <tbody>
                            <tr>
                                <td width="20" class="n_xu_a n_text_back_a">
                                    {{index+1}}
                                </td>
                                <td width="500" class="n_text_G2" v-html="item.title">
                                </td>
                                <td width="100" class="n_xu_d n_text_red_d">{{item.percent}}
                                </td>
                            </tr>
                            <tr>
                                <td></td>
                                <td class="n_text_block_b">
                                    {{item.book}}
                                </td>
                                <td width="100" class="n_xu_da">
                                    是否引证：
                                    <span class="n_text_yz" v-if="item.is_reference">是</span>
                                    <span class="n_text_yz" v-else>否</span>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>

            </div>
            <div class="n_qwdz_ywnr">
                <table class="n_bgd_biao" id="table2" style="border-collapse: collapse; table-layout: fixed;" border="0"
                    cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr id="Repeater1_ctl00_tr_item">
                            <td width="330" class="n_bgd_biao_b" colspan="2">原文内容
                            </td>
                            <td width="310" class="n_bgd_biao_bs">相似内容来源
                            </td>
                        </tr>
                    </tbody>
                </table>
                <table class="n_bgd_biao" id="table3" style="border-collapse: collapse; table-layout: fixed;" border="0"
                    cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr v-for="(item,index) in report_diff">
                            <td class="n_table_xu_a">
                                {{index+1}}
                            </td>
                            <td class="n_bgd_biao_KU" style="width: 309px; vertical-align: top;">
                                <div class="n_text_red_ax" v-html="item.origin_tips">

                                </div>
                                <div class="n_bgd_biao_KUa n_red huanhang" v-html="item.origin_html">

                                </div>
                            </td>
                            <td class="n_bgd_biao_KU" style="width: 310px; vertical-align: top;">
                                <table v-for="(subitem,subindex) in item.similar">
                                    <tbody>
                                        <tr>
                                            <td class="n_bgd_biao_c" v-html="subitem.similar_tips">
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <div class="n_bgd_biao_KUa huanhang n_red"
                                                    v-html="subitem.similar_html">

                                                </div>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>

                            </td>
                        </tr>

                    </tbody>
                </table>
            </div>
            <table width="640" class="n_table_jiebf" border="0" cellspacing="0" cellpadding="0">
                <tbody>
                    <tr>
                        <td colspan="3">
                            <table width="640" class="n_table_jiebfs" border="0" cellspacing="0" cellpadding="0">
                                <tbody>
                                    <tr>
                                        <td width="120" class="n_table_jiebf_fzb">跨语言检测结果：
                                        </td>
                                        <td width="58">
                                            <div class="n_jcjg_am">0%
                                            </div>
                                        </td>
                                        <td width="61">&nbsp;
                                        </td>
                                        <td width="25">&nbsp;
                                        </td>
                                        <td width="388">&nbsp;
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                </tbody>
            </table>
            <div class="n_qwdz_ywnr">
                <table class="n_bgd_biao" id="table_item_list" style="border-collapse: collapse; table-layout: fixed;"
                    border="0" cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr id="Repeater1_ctl00_Repeater13_ctl00_ff">
                            <td width="330" class="n_bgd_biao_b" colspan="2">原文内容
                            </td>
                            <td width="310" class="n_bgd_biao_bs">相似内容来源
                            </td>
                        </tr>
                    </tbody>
                </table>
                <table class="n_bgd_biao" id="table_ce_list" style="border-collapse: collapse; table-layout: fixed;"
                    border="0" cellspacing="0" cellpadding="0"></table>
            </div>
            <div class="n_ymnr_bz" id="Repeater1_ctl00_Standard_Content">
                <div class="n_ymnr_top">指&nbsp;&nbsp;&nbsp;&nbsp;标
                </div>
                <div class="n_ymnr_top_s">
                    <table width="620" class="n_table_bz" border="0" cellspacing="0" cellpadding="0">
                    </table>
                    <table width="620" class="n_table_bz" border="0" cellspacing="0" cellpadding="0">
                        <tbody>
                            <tr>
                                <td class="n_table_bz_gdh" colspan="2">疑似剽窃文字表述
                                </td>
                            </tr>
                            <tr v-for="(item,index) in report_similar">
                                <td width="25" class="n_table_bz_mark" style="vertical-align: top;">{{index+1}}.
                                </td>
                                <td class="n_table_bz_gd">
                              
                                   {{item}}
                                   
                                </td>
                            </tr>

                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="n_bodyfooter">
            <div id="isjianjieY"></div>
            <table width="640" class="n_sm_table" border="0" cellspacing="0" cellpadding="0">
                <tbody>
                    <tr>
                        <td width="43" class="n_sm">说明： </td>
                        <td class="n_sms" colspan="5">1.仅可用于检测期刊编辑部来稿，不得用于其他用途。
                        </td>
                    </tr>
                    <tr>
                        <td width="43" class="n_sm"></td>
                        <td class="n_sms" colspan="5">2.总文字复制比：被检测文章总重合字数在总字数中所占的比例。
                        </td>
                    </tr>
                    <tr>
                        <td width="43" class="n_sm"></td>
                        <td class="n_sms" colspan="5">3.去除引用文献复制比：去除系统识别为引用的文献后，计算出来的重合字数在总字数中所占的比例。
                        </td>
                    </tr>
                    <tr>
                        <td width="43" class="n_sm"></td>
                        <td class="n_sms" colspan="5">4.去除本人已发表文献复制比：去除作者本人已发表文献后，计算出来的重合字数在总字数中所占的比例。
                        </td>
                    </tr>
                    <tr>
                        <td width="43" class="n_sm"></td>
                        <td class="n_sms" colspan="5">5.指标是由系统根据《学术期刊论文不端行为的界定标准》自动生成的。
                        </td>
                    </tr>
                    <tr>
                        <td width="43" class="n_sm"></td>
                        <td class="n_sms" colspan="5">6.<span class="n_red2">红色</span>文字表示文字复制部分<span
                                id="huansequchu">;<span class="n_yes">绿色</span>文字表示引用部分</span>。
                        </td>
                    </tr>
                    <tr>
                        <td width="43" class="n_sm"></td>
                        <td class="n_sms" colspan="5">7.本报告单仅对您所选择比对资源范围内检测结果负责。
                        </td>
                    </tr>
                    <tr>
                        <td width="43" class="n_sm"></td>
                        <td width="160" class="n_sms">8.Email：<a href="mailto:amlc@cnki.net"
                                target="_blank">amlc@cnki.net</a> </td>
                        <td width="25" class="n_sms"><img src="./static/sina.gif">
                        </td>
                        <td width="200" class="n_sms"><a href="http://e.weibo.com/u/3194559873"
                                target="_blank">http://e.weibo.com/u/3194559873</a>
                        </td>
                        <td width="25" class="n_sms"><img src="./static/tx.gif">
                        </td>
                        <td class="n_sms"><a href="http://t.qq.com/CNKI_kycx"
                                target="_blank">http://t.qq.com/CNKI_kycx</a>
                        </td>
                    </tr>
                </tbody>
            </table>
            <table width="640" class="n_sm_tables" border="0" cellspacing="0" cellpadding="0">
                <tbody>
                    <tr>
                        <td width="40"></td>
                        <td width="20"><img title="打印" class="n_print" src="./static/n_btn_print.gif">
                        </td>
                        <td width="40"><a class="n_table_prints n_print" href="javascript:print();">打印</a>
                        </td>
                        <td width="20"><img title="保存" class="n_print" src="./static/n_btn_save.gif">
                        </td>
                        <td width="40"><a class="n_table_prints  n_print" href="javascript:s();">保存</a> </td>
                        <td width="340"></td>
                        <td><a class="n_dz" href="http://check.cnki.net/" target="_blank">http://check.cnki.net/</a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
   {% endraw %}
    <script>
        var mockdata = {
            "success": true,
            "data": {
                "createtime": "{{extra_info.createtime}}",
                "report_number": "",
                "article_name": "{{extra_info.name}}",
                "article_author": "",
                "time_range": "1900-01-01至2019-07-26",
                "report_result": [
                    {
                        "key": "总文字复制比",
                        "value": "24.2%"
                    },
                    {
                        "key": "跨语言检测结果",
                        "value": "0%"
                    },
                    {
                        "key": "总文字复制比",
                        "value": "{{extra_info.similar_rate}}%"
                    }
                ],
                "report_diff": [
                   {% for line in lines %}
                        {
                            "origin_html": `{{line.origin_content}}`,
                            "origin_tips": `此处有{{line.similar_count}}字相似`,
                            "similar_html": ``,
                            "similar_tips": `来源：{{line.title}}`,
                            "similar": [
                                     {% for similar_data in line.similar_datas %}
                                {
                                    "similar_html": `{{similar_data.similar_content}}`,
                                    "similar_tips": `来源：{{similar_data.title}}`
                                },
                                           {% endfor %}
                            ]
                        },
                 {% endfor %}
                    ],
                "report_reference": {
                    "reference_title": "全文",
                "reference_wordnumber": "{{extra_info.word_count}}",
                "reference_data": [

                ],
                "reference_list": [
                {% for ref in extra_info.ref_list[:10] %}
                {
                       
                        "title": "{{ref.title}}",
                        "percent": "{{ref.similar_count}}%"
                    },
                {% endfor %}
                    
                ]
                },
                "report_similar":[
                    "",
                ]
            }
        }
        var app = new Vue({
            el: '#app',
            data() {
                return {
                    createtime: "",
                    report_number: "",
                    article_name: "",
                    article_author: "",
                    time_range: "",
                    report_result: [],
                    report_diff: [],
                    report_reference: {},
                    report_similar:[]
                }
            },
            methods: {
                init: function () {
                    if (mockdata.success) {
                        this.createtime = mockdata.data.createtime
                        this.report_number = mockdata.data.report_number
                        this.article_name = mockdata.data.article_name
                        this.article_author = mockdata.data.article_author
                        this.time_range = mockdata.data.time_range
                        this.report_result = mockdata.data.report_result
                        this.report_diff = mockdata.data.report_diff
                        this.report_reference = mockdata.data.report_reference
                        this.report_similar = mockdata.data.report_similar
                    }
                    console.log('init')
                }
            },
            created() {

            },
            mounted() {
                this.init()

            }
        })
    </script>
</body>
<style>
    body {
        text-align: left;
        font-size: 12px;
        color: #292929;
        background: url(images/n_bg.gif) repeat;
        font-family: Arial, Helvetica, sans-serif;
        margin: 0;
        padding: 0;
    }
     em {
    color:red;
    font-style:normal
    }

    #app {
        width: 640px;
        min-height: 600px;
        background-color: #FFF;
        background-repeat: repeat-y;
        height: auto !important;
        margin: 0px auto 0 auto;
    }

    .n_main {
        width: 640px;
        min-height: 600px;
        background-color: #FFF;
        background-repeat: repeat-y;
        height: auto !important;
        margin: 0px auto 0 auto;
    }

    * {
        text-align: left;
    }

    html,
    body {
        text-align: left;
        font-size: 12px;
        color: #292929;
        background: url(images/n_bg.gif) repeat;
        font-family: Arial, Helvetica, sans-serif;
    }

    @media print {
        .n_print {
            display: none;
        }
    }

    .n_table_prints {
        font-weight: bold;
        font-size: 12px;
        color: #2e2f2e;
    }

    .n_table_prints:hover {
        color: #760605;
    }

    .n_title {
        padding-top: 12px;
        padding-bottom: 12px;
        width: 640px;
    }

    .n_logo_left {
        text-align: left;
        padding-left: 20px;
    }

    .n_logo_left img {
        border: none;
    }

    .n_logo_right img {
        border: none;
    }

    .n_bfb {
        font-weight: bold;
    }

    .n_logo_right {
        text-align: right;
        padding-right: 20px;
    }

    .n_title_left {
        float: left;
        width: 190px;
        height: 46px;
        background: url(images/jie_amlc.gif) no-repeat;
        margin-left: 10px;
        display: inline;
    }

    .n_title_right {
        float: right;
        width: 185px;
        height: 62px;
        background: url(images/jie_zw.gif) no-repeat;
        margin-right: 10px;
        display: inline;
    }

    .n_bodytop {
        width: 640px;
        margin: 0px auto;
    }

    .n_clear {
        clear: both;
    }

    .n_bt {
        text-align: center;
        height: 30px;
        line-height: 30px;
        overflow: hidden;
        font-size: 24px;
        font-weight: bold;
        border-bottom: solid 1px #035d03;
        margin-bottom: 1px;
    }

    .n_jie {
        font-size: 12px;
        font-weight: normal;
    }

    .n_no {
        height: 30px;
        background: #f4f9ef;
        width: 640px;
        margin: 0px auto;
        line-height: 30px;
        color: #750606;
        text-align: left;
        font-size: 12px;
    }

    .n_bgd_k1 {
        width: 640px;
        height: auto;
        padding-top: 10px;
        font-size: 12px;
    }

    .n_yes {
        color: #009900;
    }

    .n_table_a {
        color: #000;
        font-size: 12px;
        border: 0;
    }

    .n_table_a_cos {
        background-color: #f4f9ef;
        height: 26px;
    }

    .n_table_a_cosa {
        background-color: #f4f9ef;
        height: 20px;
    }

    .n_text_green {
        color: #1a5f02;
        text-align: right;
        line-height: 26px;
        font-weight: bold;
    }

    .n_text_block_b {
        line-height: 20px;
        padding-left: 8px;
        color: #7a7a7a;
    }

    .n_text_block_bm {
        line-height: 20px;
        font-size: 12px;
        text-align: left;
    }

    .n_text_block_a {
        text-align: left;
        line-height: 26px;
    }

    .n_bgd_k2 {
        font-size: 12px;
    }

    .n_table_b {
        width: 640px;
        border-top: 2px #035d03 solid;
    }

    .n_text_Gm {
        color: #035d03;
    }

    .n_text_Gm a {
        color: #035d03;
    }

    .n_text_Gm a:hover {
        color: #7bab7c;
    }

    .s_new_hui {
        color: #666;
    }

    .n_text_red_a {
        color: #860505;
        line-height: 26px;
        font-size: 12px;
        font-weight: bold;
        text-align: left;
        padding-left: 10px;
    }

    .n_text_red_a_zb {
        color: #860505;
        line-height: 26px;
        font-size: 12px;
        font-weight: bold;
        text-align: left;
        text-align: right;
    }

    .n_text_Gs {
        color: #860505;
        border-top: 1px #035d03 dotted;
    }

    .n_table_b_cos {
        background: #f3f9ef;
    }

    .n_red_bold {
        color: #000;
        font-weight: bold;
    }

    .n_text_block_b6 {
        color: #7e7c7c;
        font-weight: bold;
        text-align: left;
    }

    .n_table_b1 {
        background: #f3f9ef;
    }

    .n_table_a1 {
        background: #f3f9ef;
        line-height: 20px;
        border-bottom: 1px #035d03 dotted;
    }

    .n_table_a2 {
        background: #f3f9ef;
        line-height: 20px;
    }

    .n_table_a3 {
        background: #f3f9ef;
        line-height: 25px;
        border-bottom: 1px #035d03 solid;
        border-top: 1px #035d03 solid;
    }

    .n_table_a3_l {
        text-align: right;
    }

    .n_table_a3_r {
        text-align: left;
        font-weight: bold;
    }

    .n_table_a3_ra {
        color: #292929;
    }

    .n_table_a3_ra:hover {
        color: #750606;
    }

    .n_text_block_bs {
        text-align: left;
        font-weight: bold;
        font-size: 14px;
    }

    .n_text_block_bss {
        text-align: left;
        color: #666;
    }

    .n_text_block_bsm {
        font-weight: bold;
    }

    .n_text_GT {
        border-bottom: 1px #035d03 dotted;
        font-weight: bold;
        padding-left: 6px;
        color: #860505;
    }

    .n_text_GTs {
        font-weight: bold;
        padding-left: 10px;
    }

    .n_qubr_fzb {
        border-bottom: 1px #1a5f02 solid;
    }

    .n_table_a_cosa {
        border-bottom: 1px #1a5f02 solid;
    }

    .n_biao {
        text-align: right;
    }

    .n_bgd_biao {
        width: 640px;
    }

    .n_text_block_a2 a {
        color: #292929;
    }

    .n_text_block_a2 a:hover {
        color: #860505;
    }

    .n_jcjg_a {
        width: 48px;
        height: 17px;
        background-image: url(images/pmlc12_icon1.gif);
        background-repeat: no-repeat;
        text-align: left;
        line-height: 17px;
        padding-left: 10px;
        color: #333;
    }

    .n_jcjg_ap {
        width: 48px;
        height: 17px;
        background-image: url(images/n_re.gif);
        background-repeat: no-repeat;
        text-align: left;
        line-height: 17px;
        padding-left: 10px;
        color: #333;
    }

    .n_jcjg_am {
        width: 48px;
        height: 17px;
        /*background-image: url(images/n_ye.gif);*/
        background-repeat: no-repeat;
        text-align: left;
        line-height: 17px;
        color: #333;
    }

    .n_jcjg_al {
        width: 48px;
        height: 17px;
        background-image: url(images/n_jh.gif);
        background-repeat: no-repeat;
        text-align: left;
        line-height: 17px;
        padding-left: 10px;
        color: #333;
    }

    .n_k3 {
        background: #f7f7f7;
        overflow: hidden;
    }

    .n_pic {
        width: 602px;
        height: 15px;
        margin: 5px auto 10px auto;
    }

    .n_table_zs {
        margin: 0px auto;
    }

    .n_bodymid {
        width: 640px;
        margin: 0px auto;
        font-size: 12px;
        overflow: hidden;
    }

    .n_bodymid_bf {
        margin-top: 5px;
    }

    .n_table_jiebf {
        background: #f3f9ef;
        border-top: 2px #035d03 solid;
    }

    .n_table_jiebfs {
        background: #f3f9ef;
        border-top: 1px #035d03 solid;
        border-bottom: 1px #035d03 solid;
    }

    .n_table_jiebf_zzs {
        padding-left: 40px;
    }

    .n_table_jiebf_fzb {
        font-weight: bold;
        text-align: right;
        color: #760605;
        height: 25px;
        line-height: 25px;
    }

    .n_jcjg_as {
        float: left;
        width: 48px;
        height: 17px;
        background-image: url(images/pmlc12_icon1.gif);
        background-repeat: no-repeat;
        text-align: center;
        line-height: 17px;
        color: #333;
    }

    .n_xu {
        width: 640px;
        border-bottom-width: 1px;
        border-bottom-style: solid;
        border-bottom-color: #CCCCCC;
    }

    .n_xu_a {
        width: 20px;
        height: 20px;
        background-color: #fcfaf1;
        text-align: center;
        border-bottom: 1px #ccc solid;
        border-right: 1px #ccc solid;
    }

    .n_text_back_a {
        font-size: 12px;
        text-align: center;
        color: #333;
        padding-left: 2px;
        line-height: 20px;
    }

    .n_text_G2 {
        color: #333;
        font-size: 12px;
        text-align: left;
        padding-left: 8px;
        line-height: 20px;
    }

    .n_text_G2 a {
        color: #2e2f2e;
    }

    .n_text_G2 a:hover {
        color: #800613;
    }

    .n_xu_a {
        width: 20px;
        height: 20px;
        background-color: #fcfaf1;
        text-align: center;
        border-right-width: 1px;
        border-bottom-width: 1px;
        border-right-style: solid;
        border-bottom-style: solid;
        border-right-color: #CCCCCC;
        border-bottom-color: #CCCCCC;
    }

    .n_text_red_d {
        color: #8b0411;
        font-size: 12px;
        text-align: center;
    }

    .n_xu_d {
        width: 100px;
        height: 20px;
        text-align: center;
        border-left-width: 1px;
        border-left-style: solid;
        border-left-color: #CCCCCC;
        border-bottom: 1px #ccc dotted;
    }

    .n_xu_da {
        width: 100px;
        height: 20px;
        text-align: center;
        border-left-width: 1px;
        border-left-style: solid;
        border-left-color: #CCCCCC;
        color: #7a7a7a;
    }

    .n_bodylast {
        width: 640px;
        margin: 5px auto;
        height: 30px;
        background-color: #f3f9ef;
    }

    .n_bodyfooter {
        color: #666;
        border-top: 2px #1b5e01 solid;
        height: auto;
        width: 640px;
        margin: 5px auto;
        font-size: 12px;
        line-height: 20px;
    }

    .n_footer_sm {
        float: left;
        font-weight: bold;
    }

    .n_footer_sms {
        float: left;
    }

    .n_footer_smr {
        float: right;
    }

    .n_footer_smr:hover {
        color: #800811;
    }

    .n_bodymid_ywnr {
        border-top: 1px #1b5e01 solid;
        height: auto;
        margin-top: 5px;
    }

    .n_table_ywtop {
        background: #ddf0ce;
    }

    .n_ywnr {
        height: 26px;
        line-height: 26px;
        font-weight: bold;
        padding-left: 22px;
    }

    .n_ywnr_content {
        line-height: 180%;
        height: auto;
        padding-left: 20px;
        padding-right: 20px;
        margin-top: 5px;
    }

    .n_ywnr_content p {
        text-indent: 2em;
        margin: 0px auto;
    }

    .n_ywnr_content p.n_new_hui {
        color: #666;
    }

    .n_ywnr_content p img {
        width: 550px;
        height: 250px;
    }

    .n_new_red {
        color: red;
    }

    .n_new_ye {
        color: #e28a05;
    }

    .n_red2 {
        color: Red;
    }

    .red_font {
        color: #d90808;
    }

    .n_ymnr_bz {
        border-top: 1px #1b5e01 solid;
        height: auto;
    }

    .n_ymnr_top {
        height: 26px;
        background: #ddf0ce;
        line-height: 26px;
        font-weight: bold;
        text-indent: 15px;
    }

    .n_ymnr_top_s {
        width: 620px;
        margin: 5px auto;
        background: #f7f7f7;
    }

    .n_table_bz_gd {
        background: #f7f7f7;
        padding: 5px;
        line-height: 150%;
        color: #8b0411;
    }

    .n_table_bz_mark {
        background: #f7f7f7;
        line-height: 25px;
        font-weight: bold;
        text-indent: 18px;
    }

    .n_jz {
        border-top: 1px #1b5e01 solid;
        height: auto;
    }

    .n_jz_nr {
        background: #ddf0ce;
        font-weight: bold;
        padding-left: 10px;
    }

    .n_jz_nrs {
        padding-left: 10px;
        line-height: 180%;
    }

    .n_xzgf_bg {
        margin: 5px auto 5px 0px;
    }

    .n_xzgf_bgs {
        margin: 5px auto;
    }

    .content01 {
        background: #ffffff;
        line-height: 20px;
        font-weight: bold;
    }

    .content02 {
        text-align: center;
        background: #ffffff;
        line-height: 20px;
    }

    .content05 {
        text-align: left;
        background: #ffffff;
        line-height: 20px;
    }

    .content03 {
        background: #ffffff;
        line-height: 20px;
    }

    .n_ywnr_pic {
        width: 482px;
        margin: auto;
    }

    .n_table_bz_gds {
        padding-left: 10px;
        padding-top: 5px;
        padding-bottom: 5px;
    }

    .n_ye {
        color: #aeb81b;
    }

    .n_sm {
        color: #000;
        font-weight: bold;
    }

    .n_sm_tables {
        background: #f7f7f7;
        line-height: 30px;
    }

    .n_dz {
        color: #2e2f2e;
    }

    .n_dz:hover {
        color: #79100d;
        font-size: 12px;
    }

    .n_bgd_biao_b,
    .n_bgd_biao_bs {
        overflow: hidden;
        background: #ddf0ce;
        border-bottom: 1px #999 solid;
        line-height: 26px;
        font-weight: bold;
        text-align: center;
    }

    .n_bgd_biao_bs {
        border-left: 1px #999 solid;
    }

    .n_qwdz_ywnr {
        border-top: 1px #999 solid;
        margin-top: 5px;
    }

    .n_text_red_ax {
        color: #860505;
        line-height: 26px;
        font-size: 12px;
        font-weight: bold;
        text-align: center;
    }

    .n_table_xu_a {
        width: 20px;
        background: #fdfaf3;
        font-weight: bold;
        text-align: center;
        border-bottom: 1px #999 solid;
    }

    .n_qwdz_k {
        background: #f3f9ef;
        border-bottom: 1px #999 solid;
    }

    .n_bgd_biao_KU {
        overflow: hidden;
        border-left: 1px #999 solid;
        border-bottom: 1px #999 solid;
    }

    .n_bgd_biao_c {
        background: #fef4f5;
        line-height: 150%;
        padding: 5px;
        margin: 5px;
    }

    .n_text_Gr {
        border-bottom: 1px #1d5e02 dotted;
    }

    .n_bgd_biao_KUa {
        margin: 6px;
        margin-top: 0px;
        line-height: 18px;
    }

    .n_bgd_biao_KUas {
        line-height: 180%;
        text-align: center;
    }

    .n_bgd_biao_KUas a {
        color: #2e2f2e;
    }

    .n_bgd_biao_KUas a:hover {
        color: #7b100a;
    }

    .n_bgd_biao_KUm {
        font-weight: bold;
        text-align: center;
        background: #ddf0ce;
        line-height: 26px;
    }

    .n_bgd_biao_KUr {
        height: auto;
        min-height: 30px;
        border-bottom: 1px #999 solid;
        border-left: 1px #999 solid;
    }

    .n_bgd_biao_KUu {
        border-bottom: 1px #999 solid;
    }

    .n_qwdz_bz {
        line-height: 180%;
        color: #d90808;
    }

    .n_qwdz_bz a {
        color: #2e2f2e;
    }

    .n_qwdz_bz a:hover {
        color: #7b100a;
    }

    .n_qwdz_xxdz {
        font-size: 12px;
    }

    .n_jcxxjg {
        font-weight: bold;
        line-height: 25px;
    }

    .n_bgxxjc {
        background: #f3f9ef;
        line-height: 30px;
        border-top: 2px #1d5e02 solid;
    }

    .n_bz {
        font-weight: bold;
    }

    .n_bgxxjcs {
        text-align: center;
        padding: 5px;
    }

    .n_bgxxjcm {
        background: #fef4f5;
        line-height: 18px;
    }

    .n_pic_dz {
        text-align: right;
    }

    .n_bf_bt {
        text-align: center;
        font-weight: bold;
    }

    .n_table_bz_gdh {
        color: #2d2d2c;
        height: 20px;
        line-height: 20px;
        text-indent: 18px;
        font-weight: bold;
        border-bottom: 1px #1b5e01 dotted;
    }

    .n_table_pqbt {
        font-weight: bold;
        text-align: center;
    }

    .n_new_czb {
        text-align: center;
    }

    .n_new_czb_red {
        text-align: center;
        color: #ff0000;
    }

    .n_new_bgl {
        font-weight: bold;
        text-align: right;
        line-height: 22px;
    }

    .n_text_block_b6 a {
        color: #666;
    }

    .n_text_block_b6 a:hover {
        color: #860505;
    }

    .n_new_pqgdims {
        background: #f3f9ef;
        font-weight: bold;
        padding-left: 10px;
        border-top: 2px #1a5f02 solid;
        line-height: 25px;
    }

    .n_new_pqgdimx {
        width: 620px;
        margin: 5px auto;
        background: #f7f7f7;
    }

    .n_new_bg_lb table {
        text-align: left;
    }

    .n_new_bgx {
        border-bottom: 1px #1d5e02 dotted;
    }

    .n_new_bgx img {
        float: left;
    }

    .n_new_pqgd_lie {
        text-align: right;
    }

    .n_sms a {
        color: #666;
    }

    .n_sms a:hover {
        color: #90050b;
    }

    /******************全文*******************/
    .n_qwdz_ywnr {
        border-top: 1px #999 solid;
        margin-top: 5px;
    }

    .qw_bgd_biao {
        width: 640px;
        border-collapse: collapse;
        table-layout: fixed;
    }

    .qw_bgd_biao_b {
        height: 25px;
        text-align: center;
        border-top: 1px solid #999;
        border-right: 1px solid #999;
        border-bottom: 1px solid #999;
        line-height: 25px;
        background-color: #DDF0CE;
        color: #000;
    }

    .qw_bgd_biao_bs {
        height: 25px;
        text-align: center;
        border-top: 1px solid #999;
        border-left: 1px solid #999;
        border-bottom: 1px solid #999;
        line-height: 25px;
        background-color: #DDF0CE;
        color: #000;
    }

    .qw_bgd_biao_KU {
        border-right: 1px solid #999;
        border-bottom: 1px solid #999;
        padding-left: 5px;
        padding-right: 5px;
        vertical-align: top;
        text-align: left;
    }

    .qw_bgd_biao_KUa {
        width: 280px;
        padding: 5px;
        vertical-align: top;
        text-align: left;
    }

    .qw_text_red_b {
        color: #d90808;
        line-height: 20px;
        font-size: 12px;
        text-align: left;
    }

    .qw_bgd_biao_c {
        line-height: 18px;
        background-color: #FDF4F2;
        text-align: left;
        margin-top: 5px;
        color: #000;
    }

    .qw_table_xu_a {
        background-color: #fcfaf1;
        text-align: center;
        border-right: 1px dashed #999;
        border-top: 1px solid #999;
        border-left: 1px solid #999;
        border-bottom: 1px solid #999;
    }

    .qw_table_xu_b {
        width: 18px;
        background-color: #DDF0CE;
        text-align: center;
        border-top: 1px solid #999;
        border-left: 1px solid #999;
        border-bottom: 1px solid #999;
    }

    .qw_text_red_ax {
        color: #860505;
        line-height: 26px;
        font-size: 12px;
        font-weight: bold;
        text-align: center;
        padding-left: 10px;
    }

    /******************全文*******************/
    .table_check_rsR table {
        border: solid 1px #cccccc;
        border-collapse: collapse;
        word-break: break-all;
        word-wrap: break-word;
    }

    .table_check_rsR table td,
    th {
        border: solid 1px #cccccc;
        padding: 0px;
        padding-left: 5px;
        padding-right: 5px;
    }

    .t_text_red_a {
        color: #920e0a;
    }

    .Font_Color_Red {
        text-decoration: underline;
    }

    .Font_Color_Green {
        text-decoration: underline;
        font-style: oblique;
    }

    .item_title {
        border-top: 2px #035d03 solid;
        font-size: 14px;
        font-weight: bold;
        padding-left: 10px;
        line-height: 24px;
        background-color: #f4f9ef;
    }

    .n_text_green_normal {
        color: #1a5f02;
        line-height: 26px;
    }

    a.maxlink {
        color: #860505;
    }

    a.maxlink:visited {
        color: #860505;
    }
</style>

</html>
'''
template_str2 = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>report</title>
    <!-- <script src="https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.min.js"></script> -->
    <script src="https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"></script>
</head>

<body>
{% raw %}
    <div id="app">
        <div class="n_title">
            <div class="n_print">

            </div>
            <table width="640" border="0" cellspacing="0" cellpadding="0">
                <tbody>
                    <tr>
                        <td class="n_logo_left">
                            <a href="http://check.cnki.net/" target="_blank">
                                <img alt="" src="./static/jie_amlc.gif">
                            </a>
                        </td>
                        <td class="n_logo_right">
                            <a href="http://check.cnki.net/" target="_blank">
                                <img alt="" src="./static/jie_zw.gif">
                            </a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="n_bodytop">
            <div class="n_bt">文本复制检测报告单<span class="n_jie">(<span id="Label_Report_Type_Name">全文对照</span>)</span>
            </div>
            <table width="100%" class="n_table_a"
                style="border-top-color: rgb(3, 93, 3); border-top-width: 2px; border-top-style: solid;" border="0"
                cellspacing="0" cellpadding="0">
                <tbody>
                    <tr class="n_table_a_cos">
                        <td colspan="2">
                            <table width="640" border="0" cellspacing="0" cellpadding="0">
                                <tbody>
                                    <tr>
                                        <td width="420" class="n_text_red_a">№:<span
                                                id="Label_ReportID">{{report_number}}</span>

                                        </td>
                                        <td width="60" class="t_text_red_a">检测时间：
                                        </td>
                                        <td><span id="Label_Apply_Time">{{createtime}}</span>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="padding-left: 10px;" colspan="3"><span
                                                class="t_text_red_a">检测单位：</span><span id="Label_Company"></span>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td class="n_text_green" style="width: 100px;">检测文献：
                        </td>
                        <td class="n_text_block_a" style="width: 539px;"><span id="Label_Title">{{article_name}}</span>
                        </td>
                    </tr>
                    <tr>
                        <td class="n_text_green" style="width: 100px;">作者：
                        </td>
                        <td class="n_text_block_a"><span id="Label_Author">{{article_author}}</span>
                        </td>
                    </tr>
                    <tr>
                        <td class="n_text_green" style="width: 100px; vertical-align: top;">检测范围：
                        </td>
                        <td class="n_text_block_bm"><span
                                id="Label_Check_Range">中国学术期刊网络出版总库<br>中国博士学位论文全文数据库/中国优秀硕士学位论文全文数据库<br>中国重要会议论文全文数据库<br>中国重要报纸全文数据库<br>中国专利全文数据库<br>图书资源<br>优先出版文献库<br>互联网资源(包含贴吧等论坛资源)<br>英文数据库(涵盖期刊、博硕、会议的英文数据以及德国Springer、英国Taylor&amp;Francis
                                期刊数据库等)<br>港澳台学术文献库<br>互联网文档资源<br>CNKI大成编客-原创作品库<br>个人比对库</span>
                        </td>
                    </tr>
                    <tr>
                        <td class="n_text_green" style="width: 100px;">时间范围：
                        </td>
                        <td class="n_text_block_a"><span id="Label_Time_Range">{{time_range}}</span>
                        </td>
                    </tr>
                </tbody>
            </table>
            <div class="item_title">检测结果 </div>
            <div class="n_bgd_k2">
                <table width="640" class="n_table_b" id="p1" border="0" cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr class="n_table_b_cos">
                            <td width="95" class="n_text_red_a" v-for="item in report_result">
                                {{item.key}}{{item.value}}
                            </td>
                        </tr>
                    </tbody>
                </table>
                <table width="640" id="Table2" border="0" cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr class="n_table_b_cos">
                            <td width="26" height="25"><img style="border: currentColor; border-image: none;" alt=""
                                    src="./static/jie_yins.gif">
                            </td>
                            <td width="184" class="n_text_block_b6">去除引用文献复制比：<span class="n_red_bold"><span
                                        id="Label_Quote">23.5%</span></span>
                            </td>
                            <td width="27"><img style="border: currentColor; border-image: none;" alt=""
                                    src="./static/jie_bens.gif">
                            </td>
                            <td class="n_text_block_b6">去除本人已发表文献复制比：<span class="n_red_bold"><span
                                        id="Label_SameAuthor">27%</span></span>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <table width="640" id="Table3" border="0" cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr class="n_table_b_cos">
                            <td width="26"><img style="border: currentColor; border-image: none;" alt=""
                                    src="./static/jie_dans.gif">
                            </td>
                            <td class="n_text_block_b6" colspan="3">单篇最大文字复制比：<span class="n_red_bold"><span
                                        id="Label_Single_Max_Similar">5.9%</span></span><a class="maxlink"
                                    id="HyperLink_MaxCopy" target="_blank"></a> </td>
                        </tr>
                    </tbody>
                </table>
                <table width="640" class="n_table_a1" border="0" cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr class="n_qubr_fzb">
                            <td width="52" height="25" class="n_text_Gm">&nbsp;
                            </td>
                            <td width="158" class="n_text_Gm">重复字数：<span
                                    class="n_text_block_bss">&nbsp;&nbsp;&nbsp;&nbsp;[&nbsp;<span
                                        id="Label_All_CopyWords">776</span>
                                    &nbsp;]</span>
                            </td>
                            <td width="176" class="n_text_Gm">总字数：<span
                                    class="n_text_block_bss">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[&nbsp;<span
                                        id="Label_All_Words">2869</span>&nbsp;]</span>
                            </td>
                            <td width="133" class="n_text_Gm"><span id="Label1">单篇最大重复字数：</span>
                            </td>
                            <td width="110" class="n_text_Gm"><span class="n_text_block_bss">[&nbsp;<span
                                        id="Label_Single_Max_Length">168</span>&nbsp;]</span>
                            </td>
                        </tr>
                        <tr class="n_qubr_fzb">
                            <td width="52" height="25" class="n_text_Gm">&nbsp;
                            </td>
                            <td width="158" class="n_text_Gm">总段落数：<span
                                    class="n_text_block_bss">&nbsp;&nbsp;&nbsp;&nbsp;[&nbsp;<span
                                        id="Label_All_Section">1</span>
                                    &nbsp;]</span>
                            </td>
                            <td width="176" class="n_text_Gm">前部重合字数：<span class="n_text_block_bss">[&nbsp;<span
                                        id="lb_qcf">267</span>&nbsp;]</span>
                            </td>
                            <td width="133" class="n_text_Gm"><span id="Label2">疑似段落最大重合字数：</span>
                            </td>
                            <td width="110" class="n_text_Gm"><span class="n_text_block_bss">[&nbsp;<span
                                        id="lb_yszdcf">776</span>&nbsp;]</span> </td>
                        </tr>
                        <tr class="n_qubr_fzb">
                            <td width="52" height="25" class="n_text_Gm">&nbsp;
                            </td>
                            <td width="158" class="n_text_Gm">疑似段落数：<span class="n_text_block_bss">[&nbsp;<span
                                        id="lb_yszj">1</span>
                                    &nbsp;]</span> </td>
                            <td width="176" class="n_text_Gm">后部重合字数：<span class="n_text_block_bss">[&nbsp;<span
                                        id="lb_hcf">509</span>&nbsp;]</span>
                            </td>
                            <td width="243" class="n_text_Gm" colspan="2">
                                <div id="danpian">疑似段落最小重合字数：&nbsp;<span class="n_text_block_bss">[&nbsp;<span
                                            id="lb_yszxcf">776</span>&nbsp;]</span>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <table width="640" class="n_table_a2" border="0" cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr class="n_qubr_fzb">
                            <td width="101" height="25" class="n_text_red_a_zb">指&nbsp;&nbsp;&nbsp;&nbsp;标：
                            </td>
                            <td width="20"><img id="Image_Standard5" style="border-width: 0px;" src="./static/wu.gif">
                            </td>
                            <td width="80" class="n_text_Gm">疑似剽窃观点 </td>
                            <td width="20"><img id="Image_Standard4" style="border-width: 0px;" src="./static/you.gif">
                            </td>
                            <td width="80" class="n_text_Gm ">疑似剽窃文字表述 </td>
                            <td width="20"><img id="Image_Standard3" style="border-width: 0px;" src="./static/wu.gif">
                            </td>
                            <td width="80" class="n_text_Gm ">疑似自我剽窃 </td>
                            <td width="20"></td>
                            <td class="n_text_Gm "></td>
                        </tr>
                        <tr class="n_qubr_fzb">
                            <td>&nbsp; </td>
                            <td><img id="Image_Standard6" style="border-width: 0px;" src="./static/wu.gif">
                            </td>
                            <td class="n_text_Gm">一稿多投 </td>
                            <td><img id="Image_Standard7" style="border-width: 0px;" src="./static/wu.gif">
                            </td>
                            <td class="n_text_Gm">过度引用 </td>
                            <td><img id="Image_Standard1" style="border-width: 0px;" src="./static/wu.gif">
                            </td>
                            <td class="n_text_Gm ">疑似整体剽窃 </td>
                            <td width="20"><img id="Image_Standard2" style="border-width: 0px;" src="./static/wu.gif">
                            </td>
                            <td class="n_text_Gm">重复发表
                            </td>
                        </tr>
                    </tbody>
                </table>
                <table width="640" class="n_table_a3" border="0" cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr>
                            <td width="101" class="n_table_a3_l">表格： </td>
                            <td width="73" class="n_table_a3_r"><span id="Label_Table_Number">0</span>
                            </td>
                            <td width="90" class="n_table_a3_l">脚注与尾注： </td>
                            <td width="237" class="n_table_a3_r"><span id="Label_Note_Number">0</span>
                            </td>
                            <td width="117" class="n_table_a3_l">&nbsp; </td>
                            <td width="22" class="n_table_a3_r">&nbsp;
                            </td>
                        </tr>
                    </tbody>
                </table>
                <table class="n_table_a" border="0" cellspacing="0" cellpadding="0"></table>
                <div class="n_k3" id="imgdiv">
                    <div class="n_pic"><img id="Image1" style="border-width: 0px;" src="./static/RedImage5AZJL5B7.png">
                    </div>
                    <table width="640" class="n_table_zs" border="0" cellspacing="0" cellpadding="0">
                        <tbody>
                            <tr id="huanse">
                                <td class="n_text_block_b">（注释： </td>
                                <td width="6"><img alt="" src="./static/20120320_b.gif" border="0">
                                </td>
                                <td width="150" class="n_text_block_b">无问题部分
                                </td>
                                <td width="6"><img alt="" src="./static/20120320_c.gif" border="0">
                                </td>
                                <td width="150" class="n_text_block_b">文字复制比部分
                                </td>
                                <td width="6"><img alt="" src="./static/20120320_a.gif" border="0">
                                </td>
                                <td width="150" class="n_text_block_b">引用部分）
                                </td>
                                <td width="60" class="n_text_block_b"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="n_bodymid">
            <div class="n_bodymid_bf">
                <table width="640" class="n_table_jiebf" border="0" cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr>
                            <td width="25" height="30" class="n_bf_bt">
                            </td>
                            <td width="499" class="n_text_block_bs"><a name="65166928_000"></a>
                                {{report_reference.reference_title}}
                            </td>
                            <td width="116" class="n_table_jiebf_zzs">总字数：<span
                                    class="n_text_block_bs">{{report_reference.reference_wordnumber}}</span>
                            </td>
                        </tr>
                        <tr>
                            <td colspan="3">
                                <table width="640" class="n_table_jiebfs" border="0" cellspacing="0" cellpadding="0">
                                    <tbody>
                                        <tr>
                                            <td width="90" style="text-indent: 1em;">相似文献列表
                                            </td>
                                            <td width="150" class="n_table_jiebf_fzb"
                                                v-for="item in report_reference.reference_data">
                                                {{item.key}}{{item.value}}
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <div class="n_xu" v-for="(item,index) in report_reference.reference_list">
                    <table class="n_table_a" border="0" cellspacing="0" cellpadding="0">
                        <tbody>
                            <tr>
                                <td width="20" class="n_xu_a n_text_back_a">
                                    {{index+1}}
                                </td>
                                <td width="500" class="n_text_G2" v-html="item.title">
                                </td>
                                <td width="100" class="n_xu_d n_text_red_d">{{item.percent}}
                                </td>
                            </tr>
                            <tr>
                                <td></td>
                                <td class="n_text_block_b">
                                    {{item.book}}
                                </td>
                                <td width="100" class="n_xu_da">
                                    是否引证：
                                    <span class="n_text_yz" v-if="item.is_reference">是</span>
                                    <span class="n_text_yz" v-else>否</span>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>

            </div>

            <table width="640" class="n_table_jiebf" border="0" cellspacing="0" cellpadding="0">
                <tbody>
                    <tr>
                        <td colspan="3">
                            <table width="640" class="n_table_jiebfs" border="0" cellspacing="0" cellpadding="0">
                                <tbody>
                                    <tr>
                                        <td width="120" class="n_table_jiebf_fzb">跨语言检测结果：
                                        </td>
                                        <td width="58">
                                            <div class="n_jcjg_am">0%
                                            </div>
                                        </td>
                                        <td width="61">&nbsp;
                                        </td>
                                        <td width="25">&nbsp;
                                        </td>
                                        <td width="388">&nbsp;
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                </tbody>
            </table>
            <div id="Repeater1_ctl03_Red_Content" class="bgdBodyMid_main">
                <div class="bmH">原文内容</div>
                <div class="n_ywnr_content" style="word-break: break-all; word-wrap: break-word;" v-html="report_origin_html">

                </div>
            </div>
            <div class="n_ymnr_bz" id="Repeater1_ctl00_Standard_Content">
                <div class="n_ymnr_top">指&nbsp;&nbsp;&nbsp;&nbsp;标
                </div>
                <div class="n_ymnr_top_s">
                    <table width="620" class="n_table_bz" border="0" cellspacing="0" cellpadding="0">
                    </table>
                    <table width="620" class="n_table_bz" border="0" cellspacing="0" cellpadding="0">
                        <tbody>
                            <tr>
                                <td class="n_table_bz_gdh" colspan="2">疑似剽窃文字表述
                                </td>
                            </tr>
                            <tr v-for="(item,index) in report_similar">
                                <td width="25" class="n_table_bz_mark" style="vertical-align: top;">{{index+1}}.
                                </td>
                                <td class="n_table_bz_gd">
                                    {{item}}
                                </td>
                            </tr>

                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="n_bodyfooter">
            <div id="isjianjieY"></div>
            <table width="640" class="n_sm_table" border="0" cellspacing="0" cellpadding="0">
                <tbody>
                    <tr>
                        <td width="43" class="n_sm">说明： </td>
                        <td class="n_sms" colspan="5">1.仅可用于检测期刊编辑部来稿，不得用于其他用途。
                        </td>
                    </tr>
                    <tr>
                        <td width="43" class="n_sm"></td>
                        <td class="n_sms" colspan="5">2.总文字复制比：被检测文章总重合字数在总字数中所占的比例。
                        </td>
                    </tr>
                    <tr>
                        <td width="43" class="n_sm"></td>
                        <td class="n_sms" colspan="5">3.去除引用文献复制比：去除系统识别为引用的文献后，计算出来的重合字数在总字数中所占的比例。
                        </td>
                    </tr>
                    <tr>
                        <td width="43" class="n_sm"></td>
                        <td class="n_sms" colspan="5">4.去除本人已发表文献复制比：去除作者本人已发表文献后，计算出来的重合字数在总字数中所占的比例。
                        </td>
                    </tr>
                    <tr>
                        <td width="43" class="n_sm"></td>
                        <td class="n_sms" colspan="5">5.指标是由系统根据《学术期刊论文不端行为的界定标准》自动生成的。
                        </td>
                    </tr>
                    <tr>
                        <td width="43" class="n_sm"></td>
                        <td class="n_sms" colspan="5">6.<span class="n_red2">红色</span>文字表示文字复制部分<span
                                id="huansequchu">;<span class="n_yes">绿色</span>文字表示引用部分</span>。
                        </td>
                    </tr>
                    <tr>
                        <td width="43" class="n_sm"></td>
                        <td class="n_sms" colspan="5">7.本报告单仅对您所选择比对资源范围内检测结果负责。
                        </td>
                    </tr>
                    <tr>
                        <td width="43" class="n_sm"></td>
                        <td width="160" class="n_sms">8.Email：<a href="mailto:amlc@cnki.net"
                                target="_blank">amlc@cnki.net</a> </td>
                        <td width="25" class="n_sms"><img src="./static/sina.gif">
                        </td>
                        <td width="200" class="n_sms"><a href="http://e.weibo.com/u/3194559873"
                                target="_blank">http://e.weibo.com/u/3194559873</a>
                        </td>
                        <td width="25" class="n_sms"><img src="./static/tx.gif">
                        </td>
                        <td class="n_sms"><a href="http://t.qq.com/CNKI_kycx"
                                target="_blank">http://t.qq.com/CNKI_kycx</a>
                        </td>
                    </tr>
                </tbody>
            </table>
            <table width="640" class="n_sm_tables" border="0" cellspacing="0" cellpadding="0">
                <tbody>
                    <tr>
                        <td width="40"></td>
                        <td width="20"><img title="打印" class="n_print" src="./static/n_btn_print.gif">
                        </td>
                        <td width="40"><a class="n_table_prints n_print" href="javascript:print();">打印</a>
                        </td>
                        <td width="20"><img title="保存" class="n_print" src="./static/n_btn_save.gif">
                        </td>
                        <td width="40"><a class="n_table_prints  n_print" href="javascript:s();">保存</a> </td>
                        <td width="340"></td>
                        <td><a class="n_dz" href="http://check.cnki.net/" target="_blank">http://check.cnki.net/</a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
 {% endraw %}
    <script>
        var mockdata = {
            "success": true,
            "data": {
                 "createtime": "{{extra_info.createtime}}",
            "report_number": "{{extra_info.name}}",
            "report_result": [
               {
                    "key": "总文字复制比",
                    "value": "{{extra_info.similar_rate}}%",
                },
            ],
            "report_diff":  [
                        {% for line in lines %}
                        {
                            "origin_html": `{{line.origin_content}}<br/>`,
                            "origin_tips": `此处有{{line.similar_count}}字相似`,
                            "similar_html": ``,
                            "similar_tips": `来源：{{line.title}}`,
                            "similar": [
                                     {% for similar_data in line.similar_datas %}
                                {
                                    "similar_html": `{{similar_data.similar_content}}`,
                                    "similar_tips": `来源：{{similar_data.title}}`
                                },
                                           {% endfor %}
                            ]
                        },
                 {% endfor %}
               ],
               "report_reference": {
               "reference_title": "全文",
                "reference_wordnumber": "{{extra_info.word_count}}",
                "reference_data": [

                ],
                "reference_list": [
                {% for ref in extra_info.ref_list[:10] %}
                {

                        "title": "{{ref.title}}",
                        "percent": "{{ref.similar_count}}%"
                    },
                {% endfor %}

                ]
            },
                "report_similar": [
                    "",
                ],
                "report_origin_html": `{% for line in lines %}
                {{line.origin_content}}
                {% endfor %}
                `
            }
        }
        var app = new Vue({
            el: '#app',
            data() {
                return {
                    createtime: "",
                    report_number: "",
                    article_name: "",
                    article_author: "",
                    time_range: "",
                    report_result: [],
                    report_diff: [],
                    report_reference: {},
                    report_similar: [],
                    report_origin_html: ''
                }
            },
            methods: {
                init: function () {
                    if (mockdata.success) {
                        this.createtime = mockdata.data.createtime
                        this.report_number = mockdata.data.report_number
                        this.article_name = mockdata.data.article_name
                        this.article_author = mockdata.data.article_author
                        this.time_range = mockdata.data.time_range
                        this.report_result = mockdata.data.report_result
                        this.report_diff = mockdata.data.report_diff
                        this.report_reference = mockdata.data.report_reference
                        this.report_similar = mockdata.data.report_similar
                        this.report_origin_html = mockdata.data.report_origin_html
                    }
                    console.log('init')
                }
            },
            created() {

            },
            mounted() {
                this.init()

            }
        })
    </script>
</body>
<style>
    body {
        text-align: left;
        font-size: 12px;
        color: #292929;
        background: url(images/n_bg.gif) repeat;
        font-family: Arial, Helvetica, sans-serif;
        margin: 0;
        padding: 0;
    }

    #app {
        width: 640px;
        min-height: 600px;
        background-color: #FFF;
        background-repeat: repeat-y;
        height: auto !important;
        margin: 0px auto 0 auto;
    }

    .n_main {
        width: 640px;
        min-height: 600px;
        background-color: #FFF;
        background-repeat: repeat-y;
        height: auto !important;
        margin: 0px auto 0 auto;
    }

    * {
        text-align: left;
    }

    html,

    body {
        text-align: left;
        font-size: 12px;
        color: #292929;
        background: url(images/n_bg.gif) repeat;
        font-family: Arial, Helvetica, sans-serif;
    }

    em {
    color: red;
    font-style:normal
    }
    @media print {
        .n_print {
            display: none;
        }
    }

    .n_table_prints {
        font-weight: bold;
        font-size: 12px;
        color: #2e2f2e;
    }

    .n_table_prints:hover {
        color: #760605;
    }

    .n_title {
        padding-top: 12px;
        padding-bottom: 12px;
        width: 640px;
    }

    .n_logo_left {
        text-align: left;
        padding-left: 20px;
    }

    .n_logo_left img {
        border: none;
    }

    .n_logo_right img {
        border: none;
    }

    .n_bfb {
        font-weight: bold;
    }

    .n_logo_right {
        text-align: right;
        padding-right: 20px;
    }

    .n_title_left {
        float: left;
        width: 190px;
        height: 46px;
        background: url(images/jie_amlc.gif) no-repeat;
        margin-left: 10px;
        display: inline;
    }

    .n_title_right {
        float: right;
        width: 185px;
        height: 62px;
        background: url(images/jie_zw.gif) no-repeat;
        margin-right: 10px;
        display: inline;
    }

    .n_bodytop {
        width: 640px;
        margin: 0px auto;
    }

    .n_clear {
        clear: both;
    }

    .n_bt {
        text-align: center;
        height: 30px;
        line-height: 30px;
        overflow: hidden;
        font-size: 24px;
        font-weight: bold;
        border-bottom: solid 1px #035d03;
        margin-bottom: 1px;
    }

    .n_jie {
        font-size: 12px;
        font-weight: normal;
    }

    .n_no {
        height: 30px;
        background: #f4f9ef;
        width: 640px;
        margin: 0px auto;
        line-height: 30px;
        color: #750606;
        text-align: left;
        font-size: 12px;
    }

    .n_bgd_k1 {
        width: 640px;
        height: auto;
        padding-top: 10px;
        font-size: 12px;
    }

    .n_yes {
        color: #009900;
    }

    .n_table_a {
        color: #000;
        font-size: 12px;
        border: 0;
    }

    .n_table_a_cos {
        background-color: #f4f9ef;
        height: 26px;
    }

    .n_table_a_cosa {
        background-color: #f4f9ef;
        height: 20px;
    }

    .n_text_green {
        color: #1a5f02;
        text-align: right;
        line-height: 26px;
        font-weight: bold;
    }

    .n_text_block_b {
        line-height: 20px;
        padding-left: 8px;
        color: #7a7a7a;
    }

    .n_text_block_bm {
        line-height: 20px;
        font-size: 12px;
        text-align: left;
    }

    .n_text_block_a {
        text-align: left;
        line-height: 26px;
    }

    .n_bgd_k2 {
        font-size: 12px;
    }

    .n_table_b {
        width: 640px;
        border-top: 2px #035d03 solid;
    }

    .n_text_Gm {
        color: #035d03;
    }

    .n_text_Gm a {
        color: #035d03;
    }

    .n_text_Gm a:hover {
        color: #7bab7c;
    }

    .s_new_hui {
        color: #666;
    }

    .n_text_red_a {
        color: #860505;
        line-height: 26px;
        font-size: 12px;
        font-weight: bold;
        text-align: left;
        padding-left: 10px;
    }

    .n_text_red_a_zb {
        color: #860505;
        line-height: 26px;
        font-size: 12px;
        font-weight: bold;
        text-align: left;
        text-align: right;
    }

    .n_text_Gs {
        color: #860505;
        border-top: 1px #035d03 dotted;
    }

    .n_table_b_cos {
        background: #f3f9ef;
    }

    .n_red_bold {
        color: #000;
        font-weight: bold;
    }

    .n_text_block_b6 {
        color: #7e7c7c;
        font-weight: bold;
        text-align: left;
    }

    .n_table_b1 {
        background: #f3f9ef;
    }

    .n_table_a1 {
        background: #f3f9ef;
        line-height: 20px;
        border-bottom: 1px #035d03 dotted;
    }

    .n_table_a2 {
        background: #f3f9ef;
        line-height: 20px;
    }

    .n_table_a3 {
        background: #f3f9ef;
        line-height: 25px;
        border-bottom: 1px #035d03 solid;
        border-top: 1px #035d03 solid;
    }

    .n_table_a3_l {
        text-align: right;
    }

    .n_table_a3_r {
        text-align: left;
        font-weight: bold;
    }

    .n_table_a3_ra {
        color: #292929;
    }

    .n_table_a3_ra:hover {
        color: #750606;
    }

    .n_text_block_bs {
        text-align: left;
        font-weight: bold;
        font-size: 14px;
    }

    .n_text_block_bss {
        text-align: left;
        color: #666;
    }

    .n_text_block_bsm {
        font-weight: bold;
    }

    .n_text_GT {
        border-bottom: 1px #035d03 dotted;
        font-weight: bold;
        padding-left: 6px;
        color: #860505;
    }

    .n_text_GTs {
        font-weight: bold;
        padding-left: 10px;
    }

    .n_qubr_fzb {
        border-bottom: 1px #1a5f02 solid;
    }

    .n_table_a_cosa {
        border-bottom: 1px #1a5f02 solid;
    }

    .n_biao {
        text-align: right;
    }

    .n_bgd_biao {
        width: 640px;
    }

    .n_text_block_a2 a {
        color: #292929;
    }

    .n_text_block_a2 a:hover {
        color: #860505;
    }

    .n_jcjg_a {
        width: 48px;
        height: 17px;
        background-image: url(images/pmlc12_icon1.gif);
        background-repeat: no-repeat;
        text-align: left;
        line-height: 17px;
        padding-left: 10px;
        color: #333;
    }

    .n_jcjg_ap {
        width: 48px;
        height: 17px;
        background-image: url(images/n_re.gif);
        background-repeat: no-repeat;
        text-align: left;
        line-height: 17px;
        padding-left: 10px;
        color: #333;
    }

    .n_jcjg_am {
        width: 48px;
        height: 17px;
        /*background-image: url(images/n_ye.gif);*/
        background-repeat: no-repeat;
        text-align: left;
        line-height: 17px;
        color: #333;
    }

    .n_jcjg_al {
        width: 48px;
        height: 17px;
        background-image: url(images/n_jh.gif);
        background-repeat: no-repeat;
        text-align: left;
        line-height: 17px;
        padding-left: 10px;
        color: #333;
    }

    .n_k3 {
        background: #f7f7f7;
        overflow: hidden;
    }

    .n_pic {
        width: 602px;
        height: 15px;
        margin: 5px auto 10px auto;
    }

    .n_table_zs {
        margin: 0px auto;
    }

    .n_bodymid {
        width: 640px;
        margin: 0px auto;
        font-size: 12px;
        overflow: hidden;
    }

    .n_bodymid_bf {
        margin-top: 5px;
    }

    .n_table_jiebf {
        background: #f3f9ef;
        border-top: 2px #035d03 solid;
    }

    .n_table_jiebfs {
        background: #f3f9ef;
        border-top: 1px #035d03 solid;
        border-bottom: 1px #035d03 solid;
    }

    .n_table_jiebf_zzs {
        padding-left: 40px;
    }

    .n_table_jiebf_fzb {
        font-weight: bold;
        text-align: right;
        color: #760605;
        height: 25px;
        line-height: 25px;
    }

    .n_jcjg_as {
        float: left;
        width: 48px;
        height: 17px;
        background-image: url(images/pmlc12_icon1.gif);
        background-repeat: no-repeat;
        text-align: center;
        line-height: 17px;
        color: #333;
    }

    .n_xu {
        width: 640px;
        border-bottom-width: 1px;
        border-bottom-style: solid;
        border-bottom-color: #CCCCCC;
    }

    .n_xu_a {
        width: 20px;
        height: 20px;
        background-color: #fcfaf1;
        text-align: center;
        border-bottom: 1px #ccc solid;
        border-right: 1px #ccc solid;
    }

    .n_text_back_a {
        font-size: 12px;
        text-align: center;
        color: #333;
        padding-left: 2px;
        line-height: 20px;
    }

    .n_text_G2 {
        color: #333;
        font-size: 12px;
        text-align: left;
        padding-left: 8px;
        line-height: 20px;
    }

    .n_text_G2 a {
        color: #2e2f2e;
    }

    .n_text_G2 a:hover {
        color: #800613;
    }

    .n_xu_a {
        width: 20px;
        height: 20px;
        background-color: #fcfaf1;
        text-align: center;
        border-right-width: 1px;
        border-bottom-width: 1px;
        border-right-style: solid;
        border-bottom-style: solid;
        border-right-color: #CCCCCC;
        border-bottom-color: #CCCCCC;
    }

    .n_text_red_d {
        color: #8b0411;
        font-size: 12px;
        text-align: center;
    }

    .n_xu_d {
        width: 100px;
        height: 20px;
        text-align: center;
        border-left-width: 1px;
        border-left-style: solid;
        border-left-color: #CCCCCC;
        border-bottom: 1px #ccc dotted;
    }

    .n_xu_da {
        width: 100px;
        height: 20px;
        text-align: center;
        border-left-width: 1px;
        border-left-style: solid;
        border-left-color: #CCCCCC;
        color: #7a7a7a;
    }

    .n_bodylast {
        width: 640px;
        margin: 5px auto;
        height: 30px;
        background-color: #f3f9ef;
    }

    .n_bodyfooter {
        color: #666;
        border-top: 2px #1b5e01 solid;
        height: auto;
        width: 640px;
        margin: 5px auto;
        font-size: 12px;
        line-height: 20px;
    }

    .n_footer_sm {
        float: left;
        font-weight: bold;
    }

    .n_footer_sms {
        float: left;
    }

    .n_footer_smr {
        float: right;
    }

    .n_footer_smr:hover {
        color: #800811;
    }

    .n_bodymid_ywnr {
        border-top: 1px #1b5e01 solid;
        height: auto;
        margin-top: 5px;
    }

    .n_table_ywtop {
        background: #ddf0ce;
    }

    .n_ywnr {
        height: 26px;
        line-height: 26px;
        font-weight: bold;
        padding-left: 22px;
    }

    .n_ywnr_content {
        line-height: 180%;
        height: auto;
        padding-left: 20px;
        padding-right: 20px;
        margin-top: 5px;
    }

    .n_ywnr_content p {
        text-indent: 2em;
        margin: 0px auto;
    }

    .n_ywnr_content p.n_new_hui {
        color: #666;
    }

    .n_ywnr_content p img {
        width: 550px;
        height: 250px;
    }

    .n_new_red {
        color: red;
    }

    .n_new_ye {
        color: #e28a05;
    }

    .n_red2 {
        color: Red;
    }

    .red_font {
        color: #d90808;
    }

    .n_ymnr_bz {
        border-top: 1px #1b5e01 solid;
        height: auto;
    }

    .n_ymnr_top {
        height: 26px;
        background: #ddf0ce;
        line-height: 26px;
        font-weight: bold;
        text-indent: 15px;
    }

    .n_ymnr_top_s {
        width: 620px;
        margin: 5px auto;
        background: #f7f7f7;
    }

    .n_table_bz_gd {
        background: #f7f7f7;
        padding: 5px;
        line-height: 150%;
        color: #8b0411;
    }

    .n_table_bz_mark {
        background: #f7f7f7;
        line-height: 25px;
        font-weight: bold;
        text-indent: 18px;
    }

    .n_jz {
        border-top: 1px #1b5e01 solid;
        height: auto;
    }

    .n_jz_nr {
        background: #ddf0ce;
        font-weight: bold;
        padding-left: 10px;
    }

    .n_jz_nrs {
        padding-left: 10px;
        line-height: 180%;
    }

    .n_xzgf_bg {
        margin: 5px auto 5px 0px;
    }

    .n_xzgf_bgs {
        margin: 5px auto;
    }

    .content01 {
        background: #ffffff;
        line-height: 20px;
        font-weight: bold;
    }

    .content02 {
        text-align: center;
        background: #ffffff;
        line-height: 20px;
    }

    .content05 {
        text-align: left;
        background: #ffffff;
        line-height: 20px;
    }

    .content03 {
        background: #ffffff;
        line-height: 20px;
    }

    .n_ywnr_pic {
        width: 482px;
        margin: auto;
    }

    .n_table_bz_gds {
        padding-left: 10px;
        padding-top: 5px;
        padding-bottom: 5px;
    }

    .n_ye {
        color: #aeb81b;
    }

    .n_sm {
        color: #000;
        font-weight: bold;
    }

    .n_sm_tables {
        background: #f7f7f7;
        line-height: 30px;
    }

    .n_dz {
        color: #2e2f2e;
    }

    .n_dz:hover {
        color: #79100d;
        font-size: 12px;
    }

    .n_bgd_biao_b,
    .n_bgd_biao_bs {
        overflow: hidden;
        background: #ddf0ce;
        border-bottom: 1px #999 solid;
        line-height: 26px;
        font-weight: bold;
        text-align: center;
    }

    .n_bgd_biao_bs {
        border-left: 1px #999 solid;
    }

    .n_qwdz_ywnr {
        border-top: 1px #999 solid;
        margin-top: 5px;
    }

    .n_text_red_ax {
        color: #860505;
        line-height: 26px;
        font-size: 12px;
        font-weight: bold;
        text-align: center;
    }

    .n_table_xu_a {
        width: 20px;
        background: #fdfaf3;
        font-weight: bold;
        text-align: center;
        border-bottom: 1px #999 solid;
    }

    .n_qwdz_k {
        background: #f3f9ef;
        border-bottom: 1px #999 solid;
    }

    .n_bgd_biao_KU {
        overflow: hidden;
        border-left: 1px #999 solid;
        border-bottom: 1px #999 solid;
    }

    .n_bgd_biao_c {
        background: #fef4f5;
        line-height: 150%;
        padding: 5px;
        margin: 5px;
    }

    .n_text_Gr {
        border-bottom: 1px #1d5e02 dotted;
    }

    .n_bgd_biao_KUa {
        margin: 6px;
        margin-top: 0px;
        line-height: 18px;
    }

    .n_bgd_biao_KUas {
        line-height: 180%;
        text-align: center;
    }

    .n_bgd_biao_KUas a {
        color: #2e2f2e;
    }

    .n_bgd_biao_KUas a:hover {
        color: #7b100a;
    }

    .n_bgd_biao_KUm {
        font-weight: bold;
        text-align: center;
        background: #ddf0ce;
        line-height: 26px;
    }

    .n_bgd_biao_KUr {
        height: auto;
        min-height: 30px;
        border-bottom: 1px #999 solid;
        border-left: 1px #999 solid;
    }

    .n_bgd_biao_KUu {
        border-bottom: 1px #999 solid;
    }

    .n_qwdz_bz {
        line-height: 180%;
        color: #d90808;
    }

    .n_qwdz_bz a {
        color: #2e2f2e;
    }

    .n_qwdz_bz a:hover {
        color: #7b100a;
    }

    .n_qwdz_xxdz {
        font-size: 12px;
    }

    .n_jcxxjg {
        font-weight: bold;
        line-height: 25px;
    }

    .n_bgxxjc {
        background: #f3f9ef;
        line-height: 30px;
        border-top: 2px #1d5e02 solid;
    }

    .n_bz {
        font-weight: bold;
    }

    .n_bgxxjcs {
        text-align: center;
        padding: 5px;
    }

    .n_bgxxjcm {
        background: #fef4f5;
        line-height: 18px;
    }

    .n_pic_dz {
        text-align: right;
    }

    .n_bf_bt {
        text-align: center;
        font-weight: bold;
    }

    .n_table_bz_gdh {
        color: #2d2d2c;
        height: 20px;
        line-height: 20px;
        text-indent: 18px;
        font-weight: bold;
        border-bottom: 1px #1b5e01 dotted;
    }

    .n_table_pqbt {
        font-weight: bold;
        text-align: center;
    }

    .n_new_czb {
        text-align: center;
    }

    .n_new_czb_red {
        text-align: center;
        color: #ff0000;
    }

    .n_new_bgl {
        font-weight: bold;
        text-align: right;
        line-height: 22px;
    }

    .n_text_block_b6 a {
        color: #666;
    }

    .n_text_block_b6 a:hover {
        color: #860505;
    }

    .n_new_pqgdims {
        background: #f3f9ef;
        font-weight: bold;
        padding-left: 10px;
        border-top: 2px #1a5f02 solid;
        line-height: 25px;
    }

    .n_new_pqgdimx {
        width: 620px;
        margin: 5px auto;
        background: #f7f7f7;
    }

    .n_new_bg_lb table {
        text-align: left;
    }

    .n_new_bgx {
        border-bottom: 1px #1d5e02 dotted;
    }

    .n_new_bgx img {
        float: left;
    }

    .n_new_pqgd_lie {
        text-align: right;
    }

    .n_sms a {
        color: #666;
    }

    .n_sms a:hover {
        color: #90050b;
    }

    /******************全文*******************/
    .n_qwdz_ywnr {
        border-top: 1px #999 solid;
        margin-top: 5px;
    }

    .qw_bgd_biao {
        width: 640px;
        border-collapse: collapse;
        table-layout: fixed;
    }

    .qw_bgd_biao_b {
        height: 25px;
        text-align: center;
        border-top: 1px solid #999;
        border-right: 1px solid #999;
        border-bottom: 1px solid #999;
        line-height: 25px;
        background-color: #DDF0CE;
        color: #000;
    }

    .qw_bgd_biao_bs {
        height: 25px;
        text-align: center;
        border-top: 1px solid #999;
        border-left: 1px solid #999;
        border-bottom: 1px solid #999;
        line-height: 25px;
        background-color: #DDF0CE;
        color: #000;
    }

    .qw_bgd_biao_KU {
        border-right: 1px solid #999;
        border-bottom: 1px solid #999;
        padding-left: 5px;
        padding-right: 5px;
        vertical-align: top;
        text-align: left;
    }

    .qw_bgd_biao_KUa {
        width: 280px;
        padding: 5px;
        vertical-align: top;
        text-align: left;
    }

    .qw_text_red_b {
        color: #d90808;
        line-height: 20px;
        font-size: 12px;
        text-align: left;
    }

    .qw_bgd_biao_c {
        line-height: 18px;
        background-color: #FDF4F2;
        text-align: left;
        margin-top: 5px;
        color: #000;
    }

    .qw_table_xu_a {
        background-color: #fcfaf1;
        text-align: center;
        border-right: 1px dashed #999;
        border-top: 1px solid #999;
        border-left: 1px solid #999;
        border-bottom: 1px solid #999;
    }

    .qw_table_xu_b {
        width: 18px;
        background-color: #DDF0CE;
        text-align: center;
        border-top: 1px solid #999;
        border-left: 1px solid #999;
        border-bottom: 1px solid #999;
    }

    .qw_text_red_ax {
        color: #860505;
        line-height: 26px;
        font-size: 12px;
        font-weight: bold;
        text-align: center;
        padding-left: 10px;
    }

    /******************全文*******************/
    .table_check_rsR table {
        border: solid 1px #cccccc;
        border-collapse: collapse;
        word-break: break-all;
        word-wrap: break-word;
    }

    .table_check_rsR table td,
    th {
        border: solid 1px #cccccc;
        padding: 0px;
        padding-left: 5px;
        padding-right: 5px;
    }

    .t_text_red_a {
        color: #920e0a;
    }

    .Font_Color_Red {
        text-decoration: underline;
    }

    .Font_Color_Green {
        text-decoration: underline;
        font-style: oblique;
    }

    .item_title {
        border-top: 2px #035d03 solid;
        font-size: 14px;
        font-weight: bold;
        padding-left: 10px;
        line-height: 24px;
        background-color: #f4f9ef;
    }

    .n_text_green_normal {
        color: #1a5f02;
        line-height: 26px;
    }

    a.maxlink {
        color: #860505;
    }

    a.maxlink:visited {
        color: #860505;
    }

    .bmH {
        background: #ddf0ce;
        height: 26px;
        line-height: 26px;
        font-weight: bold;
        padding-left: 10px;
        border-top: 1px solid #999;
        margin-top: 5px;
    }

    .Font_Color_Red {
        text-decoration: underline;
    }

    .Font_Color_Red {
        color: Red;
    }
</style>

</html>
'''

def render_html(lines,extra_info={}):
    '''全文数据统计'''
    template = Template(template_str)
    # # 这里相似比计算就取平均算了
    word_count_sum = 0
    similar_count_sum = 0
    for line in lines:
        similar_count_sum += line['similar_count']
        word_count_sum  += line['word_count']
    extra_info['similar_rate'] =  round(100*similar_count_sum/word_count_sum,1) if word_count_sum else 0
    rsp = (template.render(lines=lines,extra_info=extra_info ))
    return rsp,extra_info['similar_rate']

def render_html2(lines,extra_info={}):
    '''全文数据统计'''
    template = Template(template_str2)
    # # 这里相似比计算就取平均算了
    word_count_sum = 0
    similar_count_sum = 0
    for line in lines:
        similar_count_sum += line['similar_count']
        word_count_sum  += line['word_count']
    extra_info['similar_rate'] =  round(100*similar_count_sum/word_count_sum,1) if word_count_sum else 0
    rsp = (template.render(lines=lines,extra_info=extra_info ))
    return rsp,extra_info['similar_rate']

if __name__ == '__main__':
    import sys

    reload(sys)
    sys.setdefaultencoding('utf8')
    lines = []
    line0 = {}
    line0['origin_content'] = u'无人敢出面指责,但是司马昭却不敢称帝,还自己找了个曹家子孙当了魏元帝'
    line0["similar_count"] = 15
    line0['word_count'] = 20
    sentences = []
    sentence = {}
    sentence['origin_content'] = u'无人敢出面指责,但是司马昭却不敢称帝,还自己找了个曹家子孙当了魏元帝'
    sentence['similar_content'] = u'无人敢出面指责,但是司马昭却不敢称帝,还放了魏元帝'
    sentence['title'] = u'大军师司马懿之军师联盟 (豆瓣)'
    sentence[
        'similar_url'] = 'http://www.baidu.com/link?url=FBneBZXWW6kInMuLKdrQv6pbxCTCuTFA0xTE1e-fCSLOhFUOd8QGyUlKZ7uBgO_srQZFJFKf7mKWUP_fAPuXev29hVoGS0VkwDfoMSMMfPO'
    sentence['similar_rate'] = 0.658
    sentences.append(sentence)
    sentences.append(sentence)
    line0['similar_datas'] = sentences
    lines.append(line0)
    print(render_html(lines)[0])
    with open('1.html','w') as f:
        f.write(render_html(lines)[0])
