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



while True:
    a=a+1
    cam, frame=video.read()
    print(frame)
    print(cam)
    cv2.imshow("gray", frame)
    key=cv2.waitKey(1)
    if key==ord("q"):
        break
print(a)

cv2.destroyAllWindows()
cam.release()