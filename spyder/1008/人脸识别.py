# -*- coding: utf-8 -*-
'''
#intent      :人脸识别
#Author      :Michael Jack hu
#start date  : 2018/10/8
#File        : 人脸识别.py
#Software    : PyCharm
#finish date :
'''
#
#1. 导入库
import cv2


font = cv2.FONT_HERSHEY_SIMPLEX
#2. 加载图片
img = cv2.imread('C\huzhi\Desktop\04.jpg')
#3. 创建窗口
cv2.nameWindow('james')
#4. 显示图片
cv2.imshow('jiaqi',img)
#5. 暂停窗口
cv2.waitKey(0)
#6. 关闭窗口
cv2.destroyAllWindows()
