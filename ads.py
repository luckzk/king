# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2018/12/22
#File        : ads.py
#Software    : PyCharm
#finish date :
'''
'''
from bs4 import BeautifulSoup
text = "<a href='提示我这个链接地址'>sflkj</a>"
the_html = BeautifulSoup(text,features='lxml')
print(the_html.find('a').attrs['href'])
'''

def factorial(n):
    x = 1
    for i in range(1, n+1):
        x = x * i
    # return x
    print(x)
factorial(20)