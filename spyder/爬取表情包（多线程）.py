# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2019/1/18
#File        : 爬取表情包（多线程）.py
#Software    : PyCharm
#finish date :
'''

import requests
from lxml import etree
import os
import re
from urllib import request
from queue import Queue
import threading

class Procuder(threading.Thread):
    headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Procuder,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self,url):
        resopnse = requests.get(url,headers=self.headers)
        text = resopnse.text
        html = etree.HTML(text)
        imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        for img in imgs:
            img_url = img.get('data-original')
            alt = img.get('alt')
            alt = re.sub(r'[\?？\.，。!！*]',' ',alt)

            suffix = os.path.splitext(img_url)[1]
            suffix = re.sub(r'!dta', '', suffix)
            filename = alt + suffix
            self.img_queue.put((img_url,filename))

class Consumer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url,filename = self.img_queue.get()
            request.urlretrieve(img_url,'doutu/'+filename)
            print(filename + '下载完成')

def main():
    page_queue = Queue(100)
    img_queue = Queue(500)
    for x in range(1,101):
        url = 'http://www.doutula.com/photo/list/?page=%d' %x
        page_queue.put(url)
        print('The %d page is finshed!' %x)

    for x in range(5):
        t = Procuder(page_queue,img_queue)
        t.start()

    for x in range(5):
        t = Consumer(page_queue,img_queue)
        t.start()


if __name__ == '__main__':
    main()