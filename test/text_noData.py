# !/user/bin/env python
# -*- coding: utf-8 -*-
import requests
import re

# 下载一个网页
url = 'https://www.52pojie.cn/'
#模拟浏览器发送请求
respononse = requests.get(url)
#编码方式
respononse.encoding = 'utf-8'
html = respononse.text
# zhuangtai = re.findall(r'<div id="messagetext" class="alert_info">(.*?)<p class="alert_btnleft">',html)[0]
# print(zhuangtai)