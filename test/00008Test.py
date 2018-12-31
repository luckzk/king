# !/user/bin/env python
# -*- coding: utf-8 -*-
import requests
import re

# 下载一个网页
url = 'http://www.jueshitangmen.info/zhetian/'
#模拟浏览器发送请求
respononse = requests.get(url)
#编码方式
respononse.encoding = 'utf-8'
html = respononse.text
title = re.findall(r'<h2>(.*?)</h2>', html)[0]
#   保存小说内容
fb = open('%s.txt' % title, 'w',encoding='utf-8')
#获取每一章的信息
dl = re.findall(r'<ul>(.*?)</ul>',html,re.S)[0]

chapter_info_list = re.findall(r'href="(.*?)">(.*?)<',dl)#反向捕获是什么，怎么用  #反向捕获就是捕捉（返回）括号里面的东西

# 循环每一个章节，分别下载
for chapter_info in chapter_info_list:              #for循环用法
    chapter_url,chapter_title = chapter_info           #涉及到元组
    chapter_url = chapter_url.replace('" rel="bookmark','')
    # chapter_url = "http://www.jingcaiyuedu.com%S" %chapter_url    #由于直接获取到url，就不需要这步了
    #下载章节内容
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = 'utf-8'
    chapter_html = chapter_response.text
    # #提取章节内容
    chapter_content=re.findall(r'<!-- top-right-ad -->(.*?)<!-- o-left-ad -->',chapter_html,re.S)[0]#括号需要转义(此处并不需要转义)
    #清洗数据
    chapter_content = chapter_content.replace(' ','')
    chapter_content = chapter_content.replace('&nbsp;', '')
    chapter_content = chapter_content.replace('</br>', '')
    chapter_content = chapter_content.replace('<divstyle="padding:40px0px0px0px;width:336px;float:right;"></div>','')
    chapter_content = chapter_content.replace('<p>','')
    chapter_content = chapter_content.replace('</p>','')
    chapter_content = chapter_content.replace('<br>', '')
    #持久化
    fb.write(chapter_title)
    fb.write(chapter_content)
    fb.write('\n')
    print(chapter_url)