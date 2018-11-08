#!C:\Python27amd64\python2.7
from selenium import webdriver
from ctypes import *
import time
import  random
time.sleep(5)
for i in (1,5):
    r = random.randint(1, 100)
    d = random.randint(1,100)
    windll.user32.SetCursorPos(r,d);
    double_click()
    print(1)
    windll.user32.SetCursorPos(r,d);
    print(2)
    raw_input("press any key to exit")