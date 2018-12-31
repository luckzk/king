# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2018/12/26
#File        : 斗鱼直播.py
#Software    : PyCharm
#finish date :
'''
import json
import time

from selenium import webdriver

url = 'https://www.douyu.com/directory/all'
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
driver.get(url)



def douyu():
    li_list = driver.find_elements_by_xpath('//ul[@id="live-list-contentbox"]/li')
    content_dict = {}
    for li in li_list:
        content_dict["title"] = li.find_element_by_xpath('./a').get_attribute("title")
        content_dict["author"] = li.find_element_by_xpath('//span[@class="dy-name ellipsis fl"]').text
        content_dict["watch"] = li.find_element_by_xpath('//span[@class="dy-num fr"]').text
        print(content_dict)
        ret = json.dumps(content_dict,ensure_ascii=False)   #json.dumps把字典类型数据变成字符串类型数据
    #     with open('douyu.txt','a',encoding='utf-8') as f:
    #         f.write(ret + '\n')
    # next_url = driver.find_elements_by_xpath('.//a[@class="shark-pager-next"]')
    # print('本页完')
    # next_url = next_url[0] if len(next_url) > 0 else None
    # while next_url is not None:
    #     next_url.click()   #点击事件
    #     time.sleep(3)
    #     douyu()  #递归调用


if __name__ == '__main__':
    douyu()