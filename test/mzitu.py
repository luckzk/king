#/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2019/3/12
#File        : mzitu.py
#Software    : PyCharm
#finish date :
'''


import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'referer': 'https://www.mzitu.com/tag/ugirls/'
}

response = requests.get("https://www.mzitu.com/tag/ugirls/")
html = etree.HTML(response.text)

alt_list = html.xpath('//img[@class="lazy"]/@alt')
src_list = html.xpath('//img[@class="lazy"]/@data-original')
for alt,src in zip(alt_list,src_list):
    response = requests.get(src,headers=headers)

    fileName = alt + ".jpg"
    with open(fileName,"wb")as f:
        f.write(response.content)