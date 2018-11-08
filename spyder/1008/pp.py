# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2018/10/9
#File        : pp.py
#Software    : PyCharm
#finish date :
'''

import cv2
import os
import numpy as np
from PIL import Image

# Path for face image database
path = 'dataset'
recognizer = cv2.face_LBPHFaceRecognizer.create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")