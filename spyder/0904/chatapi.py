# -*- coding:utf-8 -*-
'''
编程目的：编写微信机器人

作者：胡
时间：20180904
'''


import urllib.request
import urllib.parse
import json
import itchat

# ssl._create_default_https_context = ssl._create_unverified_context


#自动聊天
def autoChat(input_data,userid):
    api_url = "https://tuling123.com/openapi/api"
    post_data = {
        "key":"06bb07f109fb4b64b0ab93d7d08e2d68",
        "info":input_data,
        "loc":"郑州市",#loc是local，本地城市
        "userid":userid
    }

    re_content = json.loads(urllib.request.urlopen(urllib.request.Request(url=api_url,data=urllib.parse.urlencode(post_data).encode("utf-8"))).read().decode("utf-8"))["text"]
    return re_content

#自动回复
@itchat.msg_register('Text',isGroupChat=False)
def text_reply(msg):
    content = msg["Content"]
    fromuser = msg["FromUserName"]
    message = autoChat(content,fromuser)
    itchat.send(message,fromuser)


itchat.login()
itchat.run()
