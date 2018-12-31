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
from PIL import Image
from io import BytesIO
import random

url = 'http://rosi44.com/model.html'

res = requests.get(url)
res.encoding = 'gb2312'
res = res.text

dl = re.findall(r'<ul class="mod_ul black">(.*?)</ul>',res,re.S)[0]
url_info_list = re.findall(r'<div><img src="(.*?)" /></div>',dl)
pe_title = re.findall(r'<div><p>昵称：(.*?)<br />',dl)
name = random.randint(0,100)
i=0
for url_list in url_info_list:
    pe = "http://rosi44.com/{}".format(url_list)
    # im = requests.get(dowurl)
    #
    # if im.status_code ==200:
    #     open(str(dowurl)+'.jpg','wb').write(im.content)

    # response = requests.get(pe)
    # image = Image.open(BytesIO(response.content))
    # image.save('D:/pe/{}.jpg'.format(i))
    urllib.request.urlretrieve(pe,"D:/pe/{}.jpg".format(i))
    i=i+1
    print(pe)