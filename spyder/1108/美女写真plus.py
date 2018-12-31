# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2018/11/8
#File        : 美女写真plus.py
#Software    : PyCharm
#finish date : 1108
'''
import requests
import re
import os
import urllib
from PIL import Image
from io import BytesIO
import random
import time

url = 'http://rosi44.com/x/sj/'
res = requests.get(url)
res.encoding = 'gb2312'
res = res.text
dl = re.findall(r'<ul class="b_ul clearfix">(.*?)</ul>',res,re.S)[0]
href = re.findall(r'<a href="(.*?)" title="(.*?)" alt="">',dl)


def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print ('---  new folder...  ---')
        print ('---  OK  ---')

    else:
        print ("---  There is this folder!  ---")




for file in href:
    son_url,file_name = file
    son_url = 'http://rosi44.com{}'.format(son_url)
    file = "D://pe//{}".format(file_name)
    mkdir(file)  # 调用函数

    url_nei = son_url
    res_1 = requests.get(url_nei)
    res_1.encoding = 'gb2312'
    res_1 = res_1.text
    url_2 = re.findall(r'<li class="c_li c_li_ss">(.*?)</li>',res_1,re.S)[0]
    url_3 = re.findall(r'http:(.*?).jpg',url_2)


    i=0

    for pic in url_3:
        url_4 = 'http:{}.jpg'.format(pic)
        print(url_4)
        os.chdir(file)
        urllib.request.urlretrieve(url_4, "D://pe//{}//{}.jpg".format(file_name,i))
        i = i + 1
