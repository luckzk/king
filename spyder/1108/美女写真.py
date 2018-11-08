# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2018/11/8
#File        : 美女写真.py
#Software    : PyCharm
#finish date :
'''

import requests
import re
import os
import urllib

url = 'http://rosi44.com/model.html'

res = requests.get(url)
res.encoding = 'gb2312'
res = res.text

dl = re.findall(r'<ul class="mod_ul black">(.*?)</ul>',res,re.S)[0]
url_info_list = re.findall(r'<div><img src="(.*?) /></div><div><p>昵称：(.*?)<br />',dl)

for url_list in url_info_list:
    pe,pe_title = url_list
    dowurl = 'http://rosi44.com%S %url_list'
    # im = requests.get(dowurl)
    #
    # if im.status_code ==200:
    #     open(str(dowurl)+'.jpg','wb').write(im.content)
    # print(url_list)
    urllib.urlretrieve(dowurl, 'D:/pe/@S.jpg %pe_title',)
