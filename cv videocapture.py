# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:49:00 2020

@author: Asus
"""

import cv2
import numpy as np
a=1
videoname="livecaoture"
video=cv2.VideoCapture(0)
filename="E:\opencvnew2.avi"
codec=cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
framerate=30
resolution=(640,480)
videofileoutput=cv2.VideoWriter(filename, codec, framerate, resolution)

while True:
    a=a+1
    cam, frame=video.read()
    videofileoutput.write(frame)
    print(frame)
    print(cam)
    cv2.imshow("gray", frame)
    key=cv2.waitKey(1)
    if key==ord("q"):
        break
print(a)

cv2.destroyAllWindows()
videofileoutput.release()
cam.release()