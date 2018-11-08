#coding=utf-8
#!C:\Python27amd64\python2.7
import random
i = 0
b = input('请输入“1”开始抽奖。\n输入“2”退出。\n')
c = input('输入抽奖次数：')
c=int(c)
d = (0,1,2,3,4,5,6,7,8,9)
e=0
for i in range(0,c):
    if b==1:
        def getanswer(a):
            if a==1:
                return '你抽到了三级铭文碎片'
            elif a==2:
                return  '你抽到了紫水晶'
            elif a==3:
                return '你抽到了屠龙宝刀'
            elif a==4:
                return  '你抽到了龙年限定--李青'
            elif a==5:
                return  '你什么也没抽到'
            elif a==6:
                return '你获得一次清空购物车的机会'
            elif a==7:
                return '你抽到了一百元话费'
            elif a==8:
                return '你抽到了50蓝色精粹'
            elif a==9:
                return '你抽到了100橙色精粹'
            elif a==10:
                return '你抽到了半价吧圣物----脏兮兮努努'


        r = random.randint(1,10)
        e=e+1
        print(getanswer(r))

    elif b==2:
        print('游戏结束')
        break
print(e)