# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2018/10/27
#File        : 91.py
#Software    : PyCharm
#finish date :
'''

import requests
import re


#下载网页
url = 'https://91mjw.com/category/all_mj'
#模拟浏览器发送请求
response = requests.get(url)
#编码方式
response.encoding='UTF-8'

html = response.text




dd = re.findall(r'<h1 class="title"><strong>(.*?)<div class="ads ads-content">',html,re.S)[0]
# title = re.findall(r'class="channel-detail movie-item-title"(.*?)>',dd)
movies_list = re.findall(r'<a href="(.*?)">',dd)
# f = open('meiju.txt','w',encoding='UTF-8')
# f.write(movies_list)
print(movies_list)

# f.write(html)
# f.close()
# print(html)