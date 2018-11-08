'''
目的：一键完成常用网站的签到
目标网站：https://www.52pojie.cn
        https://www.bilibili.com
        https://steamcn.com/forum.php
作者：胡
开始日期：20190908
完成日期：
'''
import selenium.webdriver
import time
from selenium.webdriver.common.alert import Alert



#吾爱破解网站完成签到
driver = selenium.webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")

# wuaipojie_url = "https://www.52pojie.cn"
# driver.get(wuaipojie_url)
# time.sleep(1)
#
# driver.find_element_by_id("ls_username").send_keys("风之翼hzk")
# driver.find_element_by_id("ls_password").send_keys("hzk19970217")
# driver.find_element_by_class_name("fastlg_l").click()



#B站登陆
#steamCN登陆
#教务管理
jiaowu_url = "http://jiaowu.pdsu.edu.cn/"
driver.get(jiaowu_url)
time.sleep(1)
current_window = driver.current_window_handle  # 获取当前窗口handle name
print(current_window)
all_windows = driver.window_handles  # 获取所有窗口handle name
print(all_windows)
for window in all_windows:
    if window == current_window:
        driver.switch_to.window(window)



print (driver.title)  # 打印该页面title



#driver.close()
#driver.switch_to.window(window)  # 关闭新窗口后切回原窗口，在这里不切回原窗口，是无法操作原窗口元素的，即使你关闭了新窗口
print (driver.title)  # 打印原页面title

time.sleep(3)
driver.find_element_by_id("txt_asmcdefsddsd").send_keys("151360202")
driver.find_element_by_id("txt_pewerwedsdfsdff").send_keys("hzk1997")
driver.find_element_by_class_name("btnlogin").click()
