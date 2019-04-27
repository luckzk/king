# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2019/1/13
#File        : msg.py
#Software    : PyCharm
#finish date :
'''

import time
from twilio.rest import Client
import requests
from lxml import etree

def get_text():
    url = "http://www.tianqi.com/zhongmou/life.html"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    response = requests.get(url=url,headers=headers)

    html = response.text
    html_xpath = etree.HTML(html)


    rain = html_xpath.xpath('/html/body/div[4]/div[1]/ul/li[1]/p/text()')[0]
    clothes = html_xpath.xpath('/html/body/div[4]/div[1]/ul/li[6]/p/text()')[0]
    ziwaixian = html_xpath.xpath('/html/body/div[4]/div[1]/ul/li[3]/p/text()')[0]
    travel = html_xpath.xpath('/html/body/div[4]/div[1]/ul/li[7]/p/text()')[0]
    shaiyifu = html_xpath.xpath('/html/body/div[4]/div[1]/ul/li[8]/p/text()')[0]

    url2 = "http://www.tianqi.com/zhongmou/"
    response2 = requests.get(url=url2,headers=headers)
    html2 = response2.text
    html_xpath2 = etree.HTML(html2)
    wendu = html_xpath2.xpath('/html/body/div[5]/div/div[1]/dl/dd[3]/p/b/text()')[0]
    shidu = html_xpath2.xpath('/html/body/div[5]/div/div[1]/dl/dd[4]/b[1]/text()')[0]
    fengxiang = html_xpath2.xpath('/html/body/div[5]/div/div[1]/dl/dd[4]/b[2]/text()')[0]
    tianqi = html_xpath2.xpath('/html/body/div[5]/div/div[1]/dl/dd[3]/span/b/text()')[0]
    wen = html_xpath2.xpath('/html/body/div[5]/div/div[1]/dl/dd[3]/span/text()')[0]
    text = '\n' + "今日天气：" + tianqi +'\n' + '今日温度：' + wen +'\n' + '当前温度：' + wendu +'℃' + '\n' + shidu +'\n' + fengxiang +'\n' + rain +'\n' + clothes + '\n' + ziwaixian + '\n' + travel + '\n' + shaiyifu
    return text

text = get_text()

auth_token = '39da920ec4f23a2a68baa9f547c8753d'   #去twilio.com注册账户获取token
account_sid = 'ACff23cc74bcc50c1552b7f901bc659d50'

client = Client(account_sid,auth_token)


def sent_message(phone_number):
    mes = client.messages.create(
        from_='+18135364517',
        body=text,
        to=phone_number
    )
    print(mes.sid)

print(text)
sent_message("+8615938959075")