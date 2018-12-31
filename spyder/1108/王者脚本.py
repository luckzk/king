#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 17:53
# @Author  : 马克
#  ADB  安卓平台调试桥 是连接安卓手机和PC端的桥梁
#  运行设备的shell（命令行）
#  adb shell screencap ()    获取设备屏幕截图
#  adb pull （）   传文件
#  adb shell input tap(数值 )     点击手机屏幕  数值是坐标


import os   #导入操作系统的模块
from time import sleep    #  从time模块导入sleep函数

def tap_screen(x,y):
    os.system('adb shell input tap {} {}'.format(x,y))

if __name__ == '__main__':
    for i in range(60):
        print(i)
        tap_screen(1408,880)    # 闯关
        print('开始闯关')
        sleep(22)
        print('进入游戏')
        sleep(2)
        # tap_screen(1795,50)     # 自动
        print('自动按钮点击')
        sleep(32)
        tap_screen(1795,40)     # 跳过
        print('跳过')
        sleep(5)
        tap_screen(1795, 40)  # 跳过
        sleep(1)
        print('跳')
        tap_screen(1795, 40)  # 在跳过
        print('继续跳过')
        sleep(5)
        tap_screen(1500,500)
        print('点击屏幕继续')
        sleep(3)
        tap_screen(1521, 942)  # 再次挑战
        sleep(2)




#
# 暗号：AE86  + 自己昵称
# 马克老师微信号：wqqw0804
