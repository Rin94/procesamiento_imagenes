#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 14:40:01 2019

@author: jared
"""
import numpy as np
import cv2
from importar_img import rutaimagen

def main():
    #imgpath=rutaimagen()+"/4.2.04.tiff"
    #img=cv2.imread(imgpath,1)
    
    #create an image using numpy, this image is black
    img=np.zeros((512,512,3),np.uint8)
    #print(img)
    
    ##crear una linea (imagen,coordenadas,color,tamano)
    cv2.line(img,(0,99),(99,0),(255,0,0),2)
    
    cv2.line(img,(0,413),(413,0),(0,255,0),10)
    
    cv2.line(img,(0,720),(720,0),(0,255,245),3)
    
    ## crear un rectangulo
    cv2.rectangle(img,(140,160),(280,270),(125,255,230),3)
    
    ## crear un circulo
    cv2.circle(img,(230,230),100,(125,105,110),3)
    
    ## crear una elipse -1 hace relleno
    cv2.ellipse(img,(160,260),(50,20),0,0,360,(127,127,110),-1)
    
    ##crear un punto
    points=np.array([[80,2],[125,40],[179,19],[230,5],[30,50]],np.int32)
    points=points.reshape((-1,1,2))
    cv2.polylines(img,[points],True,(0,255,255))
    
    cv2.imshow("lena",img)
    cv2.waitKey(0)
    cv2.destroyWindow("lena")
    
    
    
    
if __name__== "__main__":
    main()