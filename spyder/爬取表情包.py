# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2019/1/18
#File        : 爬取表情包.py
#Software    : PyCharm
#finish date :
'''

import requests
from lxml import etree
import os
import re
from urllib import request

def parse_page(url):
    headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    resopnse = requests.get(url,headers=headers)
    text = resopnse.text
    html = etree.HTML(text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    for img in imgs:
        img_url = img.get('data-original')
        alt = img.get('alt')
        alt = re.sub(r'[\?？\.，。!！]',' ',alt)

        suffix = os.path.splitext(img_url)[1]
        suffix = re.sub(r'!dta', '', suffix)
        filename = alt + suffix
        request.urlretrieve(img_url,'doutu/'+filename)

def main():
    for x in range(1,101):
        url = 'http://www.doutula.com/photo/list/?page=%d' %x
        parse_page(url)
        print('The %d page is finshed!' %x)


if __name__ == '__main__':
    main()