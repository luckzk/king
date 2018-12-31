# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2018/11/17
#File        : ip.py
#Software    : PyCharm
#finish date :
'''

import re
import requests
import random

url = 'http://www.xicidaili.com/nt/'

user_agent_list = [
    {'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)'},
    {'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)'},
    {'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)'},
    {'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11'},
    {'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'},
    {
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER'},
    {'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)'},
    {
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0'},
    {
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36'},
    {
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'}
        ]
data = {
    'Accept-Ranges':'bytes',
    'Age':'1157',
    'Ali-Swift-Global-Savetime':'1539942384',
    'EagleId':'70366c1815424502083211646e',
    'ETag':'"5b253e6b-1acd"',
    'Content-Length':'6861',
    'Content-Type':'text/css',
    'Server':'Tengine',
    'Timing-Allow-Origin':'*',
    'X-Cache':'HIT TCP_MEM_HIT dirn:6:295703745',
    'X-Swift-CacheTime':'600',
}
header = {'User-Agent':'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)'}

res = requests.get(url,headers=header,data=data).text
print(res)