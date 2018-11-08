# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2018/10/27
#File        : 91meiju.py
#Software    : PyCharm
#finish date :
'''


import requests
import re


#下载网页
url = 'http://maoyan.com/films?showType=3'
#模拟浏览器发送请求
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}
response = requests.get(url)
#编码方式
response.encoding='UTF-8'
req = response.headers

html = response.text

# f = open('meiju.txt','w',encoding='UTF-8')


dd = re.findall(r'<title>(.*?)</title>',html,re.S)[0]
# title = re.findall(r'class="channel-detail movie-item-title"(.*?)>',dd)
print(dd)

# f.write(html)
# f.close()
# print(html)