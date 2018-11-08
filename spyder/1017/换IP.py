# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2018/10/17
#File        : 换IP.py
#Software    : PyCharm
#finish date :
'''

import bs4
import urllib

def getProxyIp():
    proxy = []
    for i in range(1, 3):
        print(i)
        header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                                           'AppleWebKit/537.36 (KHTML, like Gecko) '
                                               'Ubuntu Chromium/44.0.2403.89 '
                                               'Chrome/44.0.2403.89 '
                                               'Safari/537.36'}
        req = urllib.request.Request(url='http://www.xicidaili.com/nt/{0}'.format(i), headers=header)
        r = urllib.request.urlopen(req)
        soup = BeautifulSoup(r,'html.parser',from_encoding='utf-8')
        table = soup.find('table', attrs={'id': 'ip_list'})
        tr = table.find_all('tr')[1:]
        #解析得到代理ip的地址，端口，和类型
        for item in tr:
            tds =  item.find_all('td')
            temp_dict = {}
            kind = "{0}:{1}".format(tds[1].get_text().lower(), tds[2].get_text())
            proxy.append(kind)
    return proxy


    proxy_handler = urllib.request.ProxyHandler({'http': proxy_dict})
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)
    req = urllib.request.Request(url="http://www.zy52113.com/", headers=header)
    urllib.request.urlopen(req)
    print(req)

while 1:
    {
        getProxyIp()
    }