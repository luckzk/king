#/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2019/1/26
#File        : CSDN批量点赞.py
#Software    : PyCharm
#finish date :
'''

import requests
from lxml import etree
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

main_url = 'https://blog.csdn.net/qq_43580281?t=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
           "cookie": "uuid_tt_dd=10_36845198140-1523070045124-989704; __yadk_uid=G61LkbpKh15bigSg8a2hhaYUnlefmAD6; kd_user_id=b008b655-c076-4ec5-bfc5-d48d29a707d5; UN=Gents_hu; ADHOC_MEMBERSHIP_CLIENT_ID1.0=4098b447-0fd8-3fad-ef42-9d7dc6b021cc; smidV2=20180613223214713a03509da026706c0455f292030dbe00c2cd16f56525af0; __utma=17226283.842948702.1529235409.1529235409.1529235409.1; dc_session_id=10_1536545132631.331403; TY_SESSION_ID=3f359650-4f0e-49a9-b8a9-0b93b017bb3b; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=1788*1*PC_VC!5744*1*Gents_hu; ARK_ID=JS2f01815f2afa9de83aebc0c8005c50df2f01; cache_cart_num=0; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; SESSION=32954978-956d-4ff0-9019-fbb6d4f739d3; UserName=Gents_hu; UserInfo=6639ce4e00e84d73a506aecdcbb2975e; UserToken=6639ce4e00e84d73a506aecdcbb2975e; UserNick=%E6%9C%89%E6%83%B3%E6%B3%95%E7%9A%84py%E5%B7%A5%E7%A8%8B%E5%B8%88; AU=E22; BT=1548250492955; tipShow=true; TINGYUN_DATA=%7B%22id%22%3A%22-sf2Cni530g%23HL5wvli0FZI%22%2C%22n%22%3A%22WebAction%2FCI%2FarticleList%252Flist%22%2C%22tid%22%3A%223bfaa29e693b70%22%2C%22q%22%3A0%2C%22a%22%3A93%7D; firstDie=1; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1548502156,1548502262,1548557816,1548558075; dc_tos=plz1oz; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1548561492",
           "x-requested-with": "XMLHttpRequest",
           # ":authority": "blog.csdn.net",
           # "accept-encoding": "gzip, deflate, br",
           # "accept-language": "zh-CN,zh;q=0.9"
           }
blog_name = 'qq_43580281'
def get_page():
    for p in range(1,100):
        main_blog_url = 'https://blog.csdn.net/' + blog_name + '/article/list/' + p(str) +'?t=1&'
        res = requests.get(main_blog_url)
        if res.status_code == 200:
            get_url(main_blog_url)
        else:
            break


def get_url(url):
    html = requests.get(url,headers = headers).text

    dl = re.findall(r'<main>(.*?)</main>', html, re.S)[0]
    url_list = re.findall(r'<a href="https://blog.csdn.net/(.*)/article/details/(.*?)"',dl)
    for user_id_one in url_list:
        user_name,art_id = user_id_one
        if user_name == blog_name:
            fin = requests.get('https://blog.csdn.net/' + blog_name + '/phoenix/article/digg?ArticleId=' + art_id +'',headers=headers)
            print(fin.text)
    print(url_list)


me_url = requests.get('https://i.csdn.net/#/uc/profile',headers=headers).text
print(me_url)

# get_url('https://blog.csdn.net/qq_43580281/article/list/1?t=1&')
# get_page('qq_43580281')
# for url in get_url():
#     if re.findall(r'https://blog.csdn.net(.*?)',url):
#         url_list.append(url)
#     else:
#         pass
# print(url_list)