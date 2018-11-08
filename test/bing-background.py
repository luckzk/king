# !/user/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
import urllib
from PIL import Image
from io import BytesIO
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

url = 'https://cn.bing.com/'
response = requests.get(url)
response.encoding='utf-8'
html = response.text
back = re.findall(r'g_img={url: ".*?jpg"',html,re.S)[0]    #获取到的网址为  ['g_img={url: "/az/hprichbg/rb/SkylineparkRoller_ZH-CN8492771279_1920x1080.jpg"']
#对网址进性修改，增加前缀，删除多余
back = back.replace('g_img={url: "','https://cn.bing.com')
#保存title
title = re.findall(r'class="sc_light" title=(.*?)Karl-Josef Hildenbrand/Getty Images',html)[0]
title = title.replace('(© ','')
print(title)
#保存图片
background = requests.get(back)
image = Image.open(BytesIO(background.content))
image.save('title.jpg')