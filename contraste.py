#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 11:26:06 2019

@author: jared
"""

import numpy as np
import cv2
from importar_img import rutaimagen


img = cv2.imread(rutaimagen()+"/zyttM.jpg")
#cv2.imshow('test', img)
#cv2.waitKey(0)
#cv2.destroyWindow("test")
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


imghsv[:,:,2] = [[max(pixel - 25, 0) if pixel < 190 else min(pixel + 25, 255) for pixel in row] for row in imghsv[:,:,2]]
cv2.imshow('contrast', cv2.cvtColor(imghsv, cv2.COLOR_HSV2BGR))

cv2.waitKey(0)
cv2.destroyWindow("contrast")
