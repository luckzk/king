# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2018/11/29
#File        : 笔趣阁全站小说.py
#Software    : PyCharm
#finish date :
'''

import requests
from pyquery import PyQuery



def get_text(url,name):
    # url = 'https://www.biqukan.com/0_973/276440.html'
    response = requests.get(url).text


    doc = PyQuery(response)
    content = doc('#content').text()       #content是id   .content 是calss
    title = doc('h1').text()
    # name = doc('#wrapper > div.book.reader > div.path > div > a:nth-child(2)').text()

    with open(name, 'a+',encoding='utf-8') as f:
        f.write(title +'\n' + content)

def get_onebook_url(url_onebook):
    base_url = 'https://www.biqukan.com'
    response = requests.get(url_onebook)
    doc = PyQuery(response.text)
    name = doc('h2').text()
    links = doc('div.listmain a')

    # print(type(links))
    for link in links.items():
        try:
            print(base_url + link.attr.href,name)
            get_text(base_url + link.attr.href,name)
        except Exception as e:
            print(e)


def get_all_url():
    base_url = 'https://www.biqukan.com'
    response = requests.get('https://www.biqukan.com/xuanhuanxiaoshuo')
    doc = PyQuery(response.text)
    links = doc('span.s2 > a')
    # print(links)
    for link in links.items():
        # print(base_url + link.attr.href)
        try:
            print(base_url + link.attr.href)
            get_onebook_url(base_url + link.attr.href)

        except Exception as e:
            print(e)

# get_onebook_url('https://www.biqukan.com/57_57069/')
get_all_url()