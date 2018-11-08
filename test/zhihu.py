# -*- coding:utf-8 -*-
import http.cookiejar
import urllib
import bs4
import re
from bs4 import BeautifulSoup

cookie = http.cookiejar.MozillaCookieJar()  # 声明一个CookieJar对象实例来保存cookie
cookie.load('cookies_csddn.txt',ignore_discard=False,ignore_expires=False)  # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  # 用header保存模拟的请求身份
headers = {'User-Agent': user_agent, 'Referer': 'http://my.csdn.net/'}
url = "http://my.csdn.net/"
rq_body = ''
req = urllib.Request(url, rq_body, headers)
opener = urllib.build_opener(urllib.HTTPCookieProcessor(cookie))
response = opener.open(req)
print
response.read()
