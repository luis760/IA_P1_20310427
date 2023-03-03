# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 23:23:10 2023

@author: 52331
"""

import cv2

videoo = cv2.VideoCapture(0)
salida_video = cv2.VideoWriter('videochido.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (640,480))

while (True):
    ret, frame = videoo.read()
    cv2.imshow('frame',frame)
    salida_video.write(frame)
    if (cv2.waitKey(1) == ord('p')):
        break

salida_video.release()
videoo.release()
cv2.destroyAllWindows()