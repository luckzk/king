# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2018/11/8
#File        : 豆瓣TOP250.py
#Software    : PyCharm
#finish date :
'''


import re
import requests
import pandas as pd
import csv

# list = [[1,2,3],[4,4,5],[5,6,7],[5,6,7],[5,6,7]]
name = ['电影名','英文名','别名','背景','影评']
# test = pd.DataFrame(columns=name,data=list)
# test.to_csv('D:/TOP250.csv')

i=0

while(i<250):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
        print(url)
        i=i+25

        res = requests.get(url)
        res.encoding='utf-8'
        res = res.text

        dl_1 = re.findall(r'<ol class="grid_view">(.*?)</ol>',res,re.S)[0]
        movie_name_1 = re.findall(r'<span class="title">(.*?)</span>',dl_1,re.S)
        movie_name_2 = re.findall(r'<span class="other">(.*?)</span>',dl_1,re.S)
        yingping = re.findall(r'<span class="inq">(.*?)</span>',dl_1,re.S)

        # for movie_name in movie_name_1:
        #     movie_name = movie_name.replace('&nbsp;/&nbsp;','')




        # # name = ['电影名','英文名','别名','背景','影评']
        test = pd.DataFrame({'movies_name':yingping,'别名':movie_name_2})
        test.to_csv('D:/TOP250.csv',index=False,encoding='utf-8-sig')


        # with open("D:/test.csv","w",encoding="utf-8-sig") as csvfile:
        #     writer = csv.writer(csvfile)
        #
        #     writer.writerow(["aasdad","bdasdsad"])
        #     writer.writerows([[movie_name_1],[movie_name_2]])
        #     print("ok")

