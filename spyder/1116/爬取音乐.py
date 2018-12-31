# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2018/11/16
#File        : 爬取音乐.py
#Software    : PyCharm
#finish date :
'''


import re
import requests
import json
import jsonpath

musicer = ''
url = 'http://music.taihe.com/search'
data = {
    'key':musicer
}


html = requests.get(url,params=data).text
sids = re.findall(r'data-playdata="(.+?)"',html)
da1 = re.findall(r'\d+',sids[0])   #\d  表示匹配数字，+  表示多个

for i in da1:
    api = 'http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&callback=jQuery172032643105088821245_1542373438384&songid=%s&from=web&_=1542373442779'%i
    js = requests.get(api).text

    data = re.findall(r'\((.*)\)',js)[0]
    data2 = json.loads(data)
 # 第一种方式
    mp3_name = data2['songinfo']['title']
    mp3_url = data2['bitrate']['file_link']

    mp3 = requests.get(mp3_url)
    with open(r'E:\onedrive\OneDrive - qlb\music\千千音乐\%s\%s.mp3'%musicer%mp3_name,'wb') as f:
        f.write(mp3.content)

    print(mp3_name,'ok')


   # # 第二种方式
   #  name = jsonpath.jsonpath(data2,"$..title")    # $ 表示根目录 ..表示不管任何位置
   #  mp3_link = jsonpath.jsonpath(data2,"$..file_link")
   #  mp3 = requests.get(mp3_link[0])    #  注意，多了[0]
   #  with open(r'E:\onedrive\OneDrive - qlb\music\千千音乐\%s.mp3'%name,'wb') as f:
   #      f.write(mp3.content)
   #
   #  print(name,'ok')
