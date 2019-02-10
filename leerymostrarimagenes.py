#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 12:03:24 2019

@author: jared
"""

#reading and displaying Images, you can use de video, photo and others

import cv2
import os
import numpy as np
from importar_img import rutaimagen
from matplotlib import pyplot as plt

def main():
    
    ## read an image
    imgpath=rutaimagen()+"/zyttM.jpg"
    img=cv2.imread(imgpath,1)
    
    img = cv2.resize(img, dsize=(720, 480), interpolation=cv2.INTER_CUBIC)
    brightness = 10
    contrast = 90
    img = np.int16(img)
    img = img * (contrast/127+1) - contrast + brightness
    img = np.clip(img, 0, 255)
    img = np.uint8(img)
    
    
    lmin=img.argmax()
    hnin=img.argmin()
    lout=0;
    hout=255;
    m=(hout-lout)/(hnin-lmin)
    b=lout-m*lmin
    print(hnin)
    print(lmin)
    x=np.arange(lmin,hnin,100)
    plt.title('Line')
    plt.plot(x,x*m+b)
    plt.show()
    

    """
    modos de imagen
    1: rbg escala
    0: escala de grises
    -1: alpha de imagenes
    """
    
    ## escribir la imagen
    outpath=os.getcwd()+"/output/lenakawaii.tiff"
    cv2.imwrite(outpath,img)
    
    ## show an image
    cv2.namedWindow("lena",cv2.WINDOW_AUTOSIZE)
    cv2.imshow("lena",img)
    cv2.waitKey(0)
    #cv2.destroyAllWindows()
    cv2.destroyWindow("lena")
    
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    plt.hist(img.ravel(),256,[0,256])
    plt.title('Histogram for gray scale picture')
    plt.show()

    while True:
        k = cv2.waitKey(0) & 0xFF     
        if k == 27: break             # ESC key to exit 
        cv2.destroyAllWindows()
    
    

    
    

    
    
if __name__=="__main__":
    main()