# -*- coding: utf-8 -*-
'''
#intent      :生成验证码
#Author      :Michael Jack hu
#start date  : 2018/9/22
#File        : 验证码.py
#Software    : PyCharm
#finish date :
'''

from  PIL import Image,ImageDraw,ImageFont,ImageFilter
import random


#生成随机字母
def rndchar():

    return chr(random.randint(65,90))
#生成随机数字和字母
def getrand(num,many):        #num是位数   many是个数
    for x in range(many):
        s=""
        for i in range(num):
            n = random.randint(1,2)         #n=1生成数字  #n=2生成字母
            if n==1:
                numb = random.randint(0,9)
                s +=str(numb)
            else:
                nn = random.randint(1,2)
                cc = random.randint(1,26)
                if nn == 1:
                    numb = chr(64+cc)      #大写字母
                    s += numb
                else:
                    numb = chr(96+cc)      #小写字母
                    s += numb
        return s



#生成字体随机颜色
def rndColor():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
#生成背景随机颜色
def rndColor1():
    return (random.randint(90,155), random.randint(90,155), random.randint(90,155))

width = 60*4
height = 60

image = Image.new('RGB',(width,height),(255,255,255))



#创建Font对象：选择文字字体和大小
font = ImageFont.truetype('Arial.ttf',36)


#创建DRAW对象，
draw = ImageDraw.Draw(image)

#填充背景的每个像素
for x in range(width):
    for y in  range(height):
        draw.point((x,y),fill=rndColor1())


#输出文字
for t in range(4):
    draw.text((60*t+10,10),getrand(1,4),font=font,fill=rndColor())    #60*T+10标识的位置
image.show()
image.save('code.jpg','jpeg')