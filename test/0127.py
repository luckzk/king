#/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2019/1/27
#File        : 0127.py
#Software    : PyCharm
#finish date :
'''

import requests

# url = 'http://baidu.com'
# params = {'param1':'hhe'}
# response1 = requests.get(url=url)
# response2 = requests.head(url)
# inp = 'baidu'
# new_url = '/s?wd='.join([url,inp])
# response3 = requests.get(new_url)
# # print(response1.status_code)
# # print(response1.json())
# # print(response1.headers)
# print(response3.text)
# print(new_url)

fruits = ['banana', 'apple',  'mango']
print(range(len(fruits)))
for index in range(len(fruits)):
   print('当前水果 :', fruits[index])
print(len(fruits))