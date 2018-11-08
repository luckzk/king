# -*- coding: utf-8 -*-
'''
#intent      :调用摄像头
#Author      :Michael Jack hu
#start date  : 2018/10/8
#File        : 人脸识别3.py
#Software    : PyCharm
#finish date :
'''
# 1.导入库
import cv2
# 2.打开摄像头
capture = cv2.VideoCapture(0)
# 3.获取摄像头实时画面
cv2.nameWindow('she xiang tou')
while True:
    #获取摄像头的帧画面
    ret,frame = capture.read()
    # 显示图片（渲染画面）
    cv2.imshow('james',frame)
    # 暂停窗口
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
# 4.释放资源
capture.release()
# 5.关闭窗口
cv2.destroyAllWindows()