'''
已成功，但是视频网站挂掉了
'''




# -*- coding: utf-8 -*-
import urllib.parse
import urllib.request
import re
import ssl

login_url = "https://login.360.cn/"

ssl._create_default_https_context = ssl._create_unverified_context

def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

account =  input("请输入账号：")
password = input("请输入密码：")

headers  = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

token_url = "https://login.360.cn/?func=jQuery18306920055979980648_1535977210357&src=pcw_svideo&from=pcw_svideo&charset=UTF-8&requestScema=https&quc_sdk_version=6.4.8&quc_sdk_name=jssdk&o=sso&m=getToken&userName="+account+"&_=1535981008428"
token_data = re.findall('"token":"(.*?)"',urllib.request.urlopen(urllib.request.Request(url=token_url,headers=headers)).read().decode("utf-8"))[0]
post_data = {
    "src":"pcw_svideo",
    "from":"pcw_svideo",
    "charset":"UTF-8",
    "requestScema":"https",
    "quc_sdk_version":"6.4.8",
    "quc_sdk_name":"jssdk",
    "o":"sso",
    "m":"login",
    "lm":"0",
    "captFlag":"1",
    "rtype":"data",
    "validatelm":"0",
    "isKeepAlive":"1",
    "captchaApp":"i360",
    "userName":account,
    "smDeviceId":"",
    "type":"normal",
    "account":account,
    "password":md5(password.encode("utf-8")),
    "captcha":"",
    "token":token_data,
    "proxy":"http://k.360kan.com/psp_jump.html",
    "callback":"QiUserJso15np976505659",
    "func":"QiUserJsonp976505659"
}

print(urllib.parse.unquote(urllib.request.urlopen(urllib.request.Request(url=login_url,data = urllib.parse.urlencode(post_data).encode("utf-8"),headers=headers)).read().decode("utf-8")))