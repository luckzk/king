#/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2019/1/22
#File        : csdn_test1.py
#Software    : PyCharm
#finish date :
'''

from urllib import request
import random
import time
import _thread

dlurl = [
        'https://www.xicidaili.com/wt/', # 国内http
        'https://www.xicidaili.com/wn/', # 国内https
        'https://www.xicidaili.com/nt/', # 国内普通
        'https://www.xicidaili.com/nn/'  # 国内高匿
    ]

def get_blog_url():
    blog_url_list =[
        'https://blog.csdn.net/Gents_hu/article/details/86585317',
        'https://blog.csdn.net/Gents_hu/article/details/86584845',
        'https://blog.csdn.net/Gents_hu/article/details/86566072',
        'https://blog.csdn.net/Gents_hu/article/details/86560851',
        'https://blog.csdn.net/Gents_hu/article/details/81746900'
            ]
    blog_url = random.choice(blog_url_list)
    return "'"+blog_url+"'"

def user_agent():
    user_agent_list = [
        "'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)'",
        "'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)'",
        "'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)'",
        "'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11'",
        "'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'",
        "'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER'",
        "'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)'",
        "'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0'",
        "'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36'",
        "'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'"
            ]
    agent = random.choice(user_agent_list)
    return agent

def get_ip():
    f = open('ip.txt', 'r')                   #以读方式打开文件
    result = list()
    for line in f.readlines():                          #依次读取每行
        line = line.strip()                             #去掉每行头尾空白
        if not len(line) or line.startswith('#'):       #判断是否是空行或注释行
            continue                                    #是的话，跳过不处理
        result.append(line)                             #保存
    result.sort()                                       #排序结果
    ip = random.choice(result)
    return ip


def start():
    blog_url_list = [
        'https://blog.csdn.net/Gents_hu/article/details/86585317',
        'https://blog.csdn.net/Gents_hu/article/details/86584845',
        'https://blog.csdn.net/Gents_hu/article/details/86566072',
        'https://blog.csdn.net/Gents_hu/article/details/86560851',
        'https://blog.csdn.net/Gents_hu/article/details/86434542',
        'https://blog.csdn.net/Gents_hu/article/details/86494912',
        'https://blog.csdn.net/Gents_hu/article/details/81746900',
        'https://blog.csdn.net/Gents_hu/article/details/86606244',
        'https://blog.csdn.net/Gents_hu/article/details/86626067'
    ]
    blog_url = random.choice(blog_url_list)
    # Burl = 'https://blog.csdn.net/Gents_hu/article/details/86585317'
    # 这是代理IP
    proxy = get_ip()
    # 创建ProxyHandler
    proxy_support = request.ProxyHandler({'http':proxy})
    # 创建Opener
    opener = request.build_opener(proxy_support)
    # 添加User Angent
    opener.addheaders = [('User-Agent', user_agent())]
    # 安装OPener
    request.install_opener(opener)
    # 使用自己安装好的Opener
    response = request.urlopen(blog_url,timeout=500)
    # 读取相应信息并解码
    html = response.read().decode("utf-8")
    # 打印信息
    # print(ip)
    # print(agent)
    print(blog_url)
    print(proxy)






def times(times):
    tim = 0

    while tim < times:
        start()
        tim = tim + 1
        # time.sleep(10)
        cishu = "第%d次刷新完毕" %tim
        print(cishu)
        time.sleep(2)
    else:
        print('complete!')


try:
    while True:
        start()
except:
    print("出问题了！请重新尝试或优化代码。")
