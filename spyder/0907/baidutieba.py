'''

目标网址：https://tieba.baidu.com/
目的：登陆百度贴吧
作者:胡
日期：20180907
'''

from selenium import webdriver
import time


driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")

url = "https://tieba.baidu.com/"
driver.get(url)

#点击登陆
driver.find_element_by_xpath('//div[@class="u_menu_item"]/a').click()
time.sleep(1)
#点击用户名登陆
driver.find_element_by_class_name("tang-pass-footerBarULogin").click()
time.sleep(1)
#输入用户名密码
driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("3454582692@qq.com")
driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("hzk19970217")
driver.find_element_by_id("TANGRAM__PSP_10__submit").click()

time.sleep(30)

driver.quit()