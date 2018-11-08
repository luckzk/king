# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2018/9/15
#File        : 王者荣耀.py
#Software    : PyCharm
#finish date :
'''

import os
import requests


url = "http://pvp.qq.com/web201605/js/herolist.json"

html = requests.get(url)

html_json = html.json()  #转化为json格式


hero_name = list(map(lambda x:x['cname'],html.json()))
hero_number = list(map(lambda x:x['ename'],html.json()))
skin_name = list(map(lambda x:x['skin_name'],html.json()))


def main():      #用于下载图片
    ii = 0
    for v in hero_number:
        os.mkdir('D:\\王者荣耀图片\\'+hero_name[ii])#创建文件夹
        os.chdir('D:\\王者荣耀图片\\'+hero_name[ii])#进入刚刚创建的文件夹
        ii = ii + 1
        for u in range(12):
            onehero_links = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+str(v)+'/'+str(v)+'-bigskin-'+str(u)+'.jpg'
            im = requests.get(onehero_links)

            if im.status_code == 200:
                open(str(u)+'.jpg','wb').write(im.content)



main()