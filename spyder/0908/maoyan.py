# -*- coding:utf-8 -*-


import requests
from lxml import etree


def getOnePage(n):
    header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"}

    url = f'http://maoyan.com/board/4?offset{n*10}'


    r = requests.get(url)



def parse(text):

    #初始化，标准化
    html = etree.HTML(text)


    names = html.xpath('//div[@class="movie-item-info"]/p[@class="name]/a/@title')

    print(names)


text = getOnePage(4)
parse(text)