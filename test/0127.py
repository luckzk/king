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

# fruits = ['banana', 'apple',  'mango']
# print(range(len(fruits)))
# for index in range(len(fruits)):
#    print('当前水果 :', fruits[index])
# print(len(fruits))

# a = {1,2,3,4,5,6}
# print(sorted(a))


# def printme(str):
#    "打印传入的字符串到标准显示设备上"
#    print (str)
#    return
#
# printme(str="abc")

# def ChangeInt(a):
#    a = 10
#    return a
#
# b = 2
# ChangeInt(b)
# print(ChangeInt(b))   #  10
# print(b)  # 结果是 2

# # 可写函数说明
# def changeme(mylist):
#    "修改传入的列表"
#    mylist.append([1, 2, 3, 4]);
#    print("函数内取值: ", mylist)
#    return
#
#
# # 调用changeme函数
# mylist = [10, 20, 30];
# changeme(mylist);
# print("函数外取值: ", mylist)

# # 可写函数说明
# def printinfo(name, age=35):
#    "打印任何传入的字符串"
#    print("Name: ", name);
#    print("Age ", age);
#    return;
#
#
# # 调用printinfo函数
# printinfo(age=50, name="miki");
# printinfo(name="miki");

# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))