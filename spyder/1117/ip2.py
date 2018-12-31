# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2018/12/29
#File        : ip2.py
#Software    : PyCharm
#finish date :
'''
import requests
from lxml import etree

url =  "http://2018.ip138.com/ic.asp"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
dlurl = [
        'https://www.xicidaili.com/wt/', # 国内http
        'https://www.xicidaili.com/wn/', # 国内https
        'https://www.xicidaili.com/nt/', # 国内普通
        'https://www.xicidaili.com/nn/'     # 国内高匿
    ]

#获取西刺代理IP页面数据
def gethtml(url):
    porxy=[]
    r = requests.get(url,headers=headers)
    r.encoding='utf-8'
    ehtml = etree.HTML(r.text)
    ip   = ehtml.xpath('//*[@class="odd"]/td[2]/text()')
    port = ehtml.xpath('//*[@class="odd"]/td[3]/text()')
    j=0
    for i in ip:
        porxy.append(i+':'+port[j])  #ip+端口
        # porxy.append(i)    #IP
        j+=1
    ip = ehtml.xpath('//*[@class=""]/td[2]/text()')
    port = ehtml.xpath('//*[@class=""]/td[3]/text()')
    j=0
    for i in ip:
        porxy.append(i+':'+port[j])  #IP+端口
        # porxy.append(i) #ip
        j+=1
    return porxy

#检查代理是否可用
def chkproxy(ipport,timeout):
    proxies = {"http": "http://" + ipport}
    try:
        response = requests.get(url, headers=headers, proxies=proxies, timeout=timeout)
        if response.status_code == 200:
            return True
    except OSError:
        pass

def exec(url,pagenum,timeout):
    f = open('C:/Users/huzhi/PycharmProjects/king/spyder/1117/ip.txt', mode='w+')
    for i in range(1,pagenum+1):
        print('开始获取第'+str(i)+'页代理IP数据...')
        porxy=gethtml(url+str(i))
        j=0
        print('开始检查第'+str(i)+'页代理IP...')
        for i in porxy:
            if chkproxy(i,timeout)==True:
                f.write(i+'\n')
            j+=1
    print('任务完成,代理IP已保存')

if __name__ == '__main__':
    #exec(代理IP网页url,获取页数,超时设置)  每页是100条代理IP数据
    exec(dlurl[0],10,0.3)