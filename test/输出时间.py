#/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2019/1/25
#File        : 输出时间.py
#Software    : PyCharm
#finish date :
'''
import time

# while True:
#     print(time.localtime(time.time()))
#     time.sleep(1)
#     print(time.strftime('%Y-%m-%d %w %H:%M:%S', time.localtime(time.time())))


L = [1, 23, "runoob", 1]
# print(L)
# =>
a = [1,2,3,None,(),[],]

# print(len(a))
def Foo(x):
    if (x==1):
        return 1
    else:
        return x+Foo(x-1)

print(Foo(4))