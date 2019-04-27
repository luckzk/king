# !/user/bin/env python
# -*- coding: utf-8 -*-
__author__='laohu'
import urllib.request,urllib
import ssl
import http.cookiejar


c = http.cookiejar.LWPCookieJar
cookie = urllib.request.HTTPCookieProcessor(c)
opener = urllib.request.build_opener(cookie)
urllib.request.install_opener(opener)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

ssl._create_default_https_context = ssl._create_unverified_context

def login():
    req = urllib.request.Request('https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.8761820145030748')
    req.headers = headers
    imgCode = opener.open(req).read()
    with open('code.png','wb') as fn:
        fn.write(imgCode)
    req = urllib.request.Request('https://kyfw.12306.cn/passport/captcha/captcha-check')
    req.headers = headers
    code = raw_input('请输入验证码：')
    data = {
        'answer':'code',
        'login_site':'E',
        'rand':'sjrand'
    }
    data = urllib.urlencode(data)

    html = opener.open(req,data).read()
    print(html)


login()