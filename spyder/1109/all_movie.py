# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2018/11/9
#File        : all_movie.py
#Software    : PyCharm
#finish date :
'''


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
from threading import *
from bs4 import BeautifulSoup
from lxml import etree
from contextlib import closing

nMaxThread = 5
connectlock = BoundedSemaphore(nMaxThread)
gHeads = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}

class MovieThread(Thread):
    def __init__(self,url,movieName):
        Thread.__init__(self)
        self.url = url
        self.movieName = movieName

    def run(self):
        try:
            urlList = self.GetMovieUrl(self.url)
            for i in range(len(urlList)):
                type,vkey = self.GetVkeyParam(self.url,urlList[i])
                if type != None and vkey !=None:
                    payload,DownloadUrl = self.GetOtherParam(self.url,urlList[i],type,vkey)
                    if DownloadUrl :
                        videoUrl = self.GetDownloadUrl(payload,DownloadUrl)
                        if videoUrl :
                            self.DownloadVideo(videoUrl,self.movieName,i+1)
        finally:
            connectlock.release()

    def GetMovieUrl(self,url):
        heads = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            "Host":"91mjw.com",
            "Referer":"https://91mjw.com/"
        }
        html = requests.get(url,headers=heads).text
        xmlContent = etree.HTML(html)
        UrlList = xmlContent.xpath("//div[@id='video_list_li']/a/@href")
        if len(UrlList) > 0:
            return UrlList
        else:
            return None

    def GetVkeyParam(self,firstUrl,secUrl):
        heads = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            "Host": "91mjw.com",
            "Referer": firstUrl
        }
        try :
            html = requests.get(firstUrl+secUrl,headers=heads).text
            bs = BeautifulSoup(html,"html.parser")
            content = bs.find("body").find("script")
            reContent = re.findall('"(.*?)"',content.text)
            return reContent[0],reContent[1]
        except:
            return None,None

    def GetOtherParam(self,firstUrl,SecUrl,type,vKey):
        url = "https://api.1suplayer.me/player/?userID=&type=%s&vkey=%s"%(type,vKey)
        heads = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            "Host": "api.1suplayer.me",
            "Referer": firstUrl+SecUrl
        }
        try:
            html = requests.get(url,headers=heads).text
            bs = BeautifulSoup(html,"html.parser")
            content = bs.find("body").find("script").text
            recontent = re.findall(" = '(.+?)'",content)
            payload = {
                    "type":recontent[3],
                    "vkey":recontent[4],
                    "ckey":recontent[2],
                    "userID":"",
                    "userIP":recontent[0],
                    "refres":1,
                    "my_url":recontent[1]
                }
            return payload,url
        except:
            return None,None

    def GetDownloadUrl(self,payload,refereUrl):
        heads = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
                    "Host": "api.1suplayer.me",
                    "Referer": refereUrl,
                    "Origin": "https://api.1suplayer.me",
                    "X-Requested-With": "XMLHttpRequest"
        }
        while True:
            retData = requests.post("https://api.1suplayer.me/player/api.php",data=payload,headers=heads).json()
            if retData["code"] == 200:
                return retData["url"]
            elif retData["code"] == 404:
                payload["refres"] += 1;
                continue
            else:
                return None

    def DownloadVideo(self,url,videoName,videoNum):
        CurrentSize = 0
        heads = {
            "chrome-proxy":"frfr",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            "Host":"sh-yun-ftn.weiyun.com",
            "Range":"bytes=0-"
        }
        with closing(requests.get(url,headers=heads)) as response:
            retSize = int(response.headers['Content-Length'])
            chunkSize = 10240
            if response.status_code == 206:
                print('[File Size]: %0.2f MB\n' % (retSize/1024/1024))
                with open("./video/%s/%02d.mp4"%(videoName,videoNum),"wb") as f:
                    for data in response.iter_content(chunk_size=chunkSize):
                        f.write(data)
                        CurrentSize += len(data)
                        f.flush()
                        print('[Progress]: %0.2f%%' % float(CurrentSize*100/retSize) + '\r')

def main():
    html = requests.get("https://91mjw.com",headers=gHeads).text
    xmlcontent = etree.HTML(html)
    UrlList = xmlcontent.xpath("//div[@class='m-movies clearfix']/article/a/@href")
    NameList = xmlcontent.xpath("//div[@class='m-movies clearfix']/article/h2/a/text()")
    for i in range(len(UrlList)):
        connectlock.acquire()
        url = UrlList[i]
        name = NameList[i].encode("utf-8")
        t = MovieThread(url,name)
        t.start()

if __name__ == '__main__':
        main()