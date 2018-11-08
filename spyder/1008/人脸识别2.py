# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2018/10/8
#File        : 人脸识别2.py
#Software    : PyCharm
#finish date :
'''

# 在识别的图片上面添加人脸识别：重点注意  需要添加模型
# 1.导入库
import cv2
# 2.加载图片
img = cv2.imread('D:\04.jpg')
# 3.加载人脸模型
face = cv2.Case("D:\timg.jpg")
# 4.调整图片灰度
gray = cv2.cvColor(img,cv2.COLOR_RGB2GRAY)
# 5.检查人脸
faces = face.detectMultiScale(gray)
# 6.标记人脸
for (x,y,w,h) in faces:
    #里面有四个参数  1，写图片 2，坐标原点 3，识别大小 4，颜色RGB5，线宽
    cv2.rectang(img,(x,y),(x+w,y+h),(0,255,0),10)
# 7.创建窗口
cv2.nameWindow('james 窗口')
# 8.显示图片
cv2.imshow('jiaqi',img)
# 9.暂停窗口
cv2.waitKey(0)
# 10.关闭窗口
cv2.destroyAllWindows()