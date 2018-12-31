# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2018/11/17
#File        : csdn.py
#Software    : PyCharm
#finish date :
'''

# -*- coding: utf-8 -*-

import urllib
import random
import time
import requests

proxy_list = []


def get_proxy_list():
    global proxy_list
    print("导入proxy_list...".encode('utf-8'))
    # ip文件可以浏览我上文链接文章“多线程爬虫——抓取代理ip”
    f = open("ip.txt")
    # 从文件中读取的line会有回车，要把\n去掉
    line = f.readline().strip('\n')
    while line:
        proxy_list.append(line)
        line = f.readline().strip('\n')
    f.close()


def start():
    # 总次数和有效次数
    times = 0
    finished_times = 0
    # 无限刷
    while 1:
        user_agent_list = [
            {'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)'},
            {'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)'},
            {'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)'},
            {'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11'},
            {'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'},
            {
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER'},
            {'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)'},
            {
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0'},
            {
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36'},
            {
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'}
        ]

        referer_list = [
            {'https://blog.csdn.net/qq_43580281/article/details/84074443'},
            {'http://blog.csdn.net/'},
            {
            'https://www.sogou.com/tx?query=%E4%BD%BF%E7%94%A8%E7%88%AC%E8%99%AB%E5%88%B7csdn%E8%AE%BF%E9%97%AE%E9%87%8F&hdq=sogou-site-706608cfdbcc1886-0001&ekv=2&ie=utf8&cid=qb7.zhuye&'},
            {
            'https://www.baidu.com/s?tn=98074231_1_hao_pg&word=%E4%BD%BF%E7%94%A8%E7%88%AC%E8%99%AB%E5%88%B7csdn%E8%AE%BF%E9%97%AE%E9%87%8F'}
        ]
        # 想要刷的blog的url
        url = 'https://blog.csdn.net/qq_43580281/article/details/84074443'
        # 随机user_agent和Referer
        header = {'User-Agent': random.choice(user_agent_list),
                  'Referer': random.choice(referer_list)
                  }
        # 依次从proxy_list中取
        ip = proxy_list[times % len(proxy_list)]
        # 设置代理,格式如下
        proxy_ip = 'http://' + ip
        proxy_ips = 'https://' + ip
        proxy = {'https': proxy_ips, 'http': proxy_ip}

        try:
            response = requests.get(url, headers=header, proxies=proxy)
        except:
            # 无响应则print出该代理ip
            print('代理出问题啦:')
            time.sleep(0.1)
        else:
            print('已刷%d次,%s') % (finished_times + 1, proxy["https"])
            time.sleep(random.random())
            finished_times += 1

        times += 1
        # 每当所有的代理ip刷过一轮，延时15秒
        if not times % len(proxy_list):
            time.sleep(15)


if __name__ == "__main__":
    get_proxy_list()
    start()
