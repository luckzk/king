#/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2019/1/25
#File        : roob_8.py
#Software    : PyCharm
#finish date :
'''
for i in range(1,10):
     for j in range(1,i+1):
         print("%d*%d=%2d" % (i,j,i*j),end=" ")
     print (" ")