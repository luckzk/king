# !/user/bin/env pyython
# -*- coding: utf-8 -*-
import requests
import re

#下载一个网页
url='http://www.miui.com/'
#   模拟浏览器发送http请求
kkkk = requests.get(url)
kkkk.encoding="utf-8"

print (kkkk)