# -*- coding: utf-8 -*-
'''
#intent      :摄像头识别人脸
#Author      :Michael Jack hu
#start date  : 2018/10/8
#File        : 人脸识别4.py
#Software    : PyCharm
#finish date :
'''

# 1.导入库
import cv2
# 2.加载人脸模型
cv2.CascadeClassifiler()
# 3.打开摄像头
capture = cv2.VideoCapture(0)
# 4.创建窗口
cv2.nameWindow()
# 5.获取摄像头实时画面
cv2.nameWindow('she xiang tou')
while True:
    #获取摄像头的帧画面
    ret,frame = capture.read()
    # 图片灰度调整
    gary = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    #检查人脸
    faces = face.detecMultiScale(gary,1.1,3,0(100,100))
    #标记人脸
    for (x, y, w, h) in faces:
        # 里面有四个参数  1，写图片 2，坐标原点 3，识别大小 4，颜色RGB5，线宽
        cv2.rectang(frame, (x, y), (x + w, y + h), (0, 255, 0), 10)
        #显示图片
        cv2.imshow('shexiangtou',frame)
        #暂停窗口
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
# 6.释放资源
capture.release()
# 7.关闭摄像头
cv2.destroyAllWindows()
