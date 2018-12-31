# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2018/12/26
#File        : pprint.py
#Software    : PyCharm
#finish date :
'''

import requests
import pprint
url = 'http://www.baidu.com'

headers= {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

ret = requests.get(url,headers=headers)

# print(ret.content.decode())  #显示在一行

pprint.pprint(ret.content.decode())   #一行行显示
