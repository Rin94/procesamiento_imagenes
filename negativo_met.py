#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 14:16:50 2019

@author: jared
"""

import cv2
import numpy as np
from importar_img import rutaimagen
from skimage import color
from skimage import io
import os

def transformation_gama(img,m,alpha):
    func_gama=np.power(img/m,alpha)
    return func_gama
    #255*
    
def transformation_estiramiento(img,m,e):
    funcion_stiramiento=1/(1+(np.power((m/img),e)))
    return funcion_stiramiento
                             
    
def to_uint8( data ) :
    # maximum pixel
    latch = np.zeros_like( data )
    latch[:] = 255
    # minimum pixel
    zeros = np.zeros_like( data )

    # unrolled to illustrate steps
    d = np.maximum( zeros, data )
    d = np.minimum( latch, d )

    # cast to uint8
    return np.asarray( d, dtype="uint8" )


def funcion_logaritmica(c,img):
    func_log=c*np.log(1+img)
    to_uint8(func_log)
    return func_log
    
def func_inversa(img,m):
    func_inv=(m-img)
    return func_inv

def write_img(img,ruta):
    outpath=os.getcwd()+"/output/"+ruta
    cv2.imwrite(outpath,img)

def show_image(img, name):
    cv2.namedWindow(name,cv2.WINDOW_AUTOSIZE)
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyWindow(name)

def increase_brightness(img, value=0):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

def diff_img(img1,img3):
    img_diff = np.ndarray(shape=img1.shape, dtype='float32')
    img_diff.fill(128)
    img_diff += (img1 - img3)
    img_diff -= img_diff.min()
    img_diff *= (255/img_diff.max())
    return img_diff

"""
g(x)=alphaf(x)+ beta
"""
def increase_contrast(img,alpha, beta):
    img=cv2.addWeighted(img,alpha,np.zeros(img.shape,img.dtype),0, beta)
    return img
    

def invert_image (imagem, name):
    imagem=(-imagem)
    #cv2.imwrite(name, imagem)
    return imagem


def convert_grayscale(img):
    img = color.rgb2gray(img)

    return img

def load_image(path,canal):
    imgpath=rutaimagen()+path
    img=cv2.imread(imgpath,)
    return img



def main():
    img=load_image("/test.jpg",1)
    #print(img)
    #img=transformation_gama(img,255,0.5)
    #img=func_inversa(img,100)
    #img=funcion_logaritmica(1,img)
    img=transformation_estiramiento(img,100,2)
    #img=invert_image(img,"lena_inv")
    #img=increase_brightness(img)
    #img3=increase_contrast(img,alpha=0.5,beta=50)
    #img3=convert_grayscale(img)
    #img=diff_img(img,img3)
    show_image(img,"lena_inv")
    

if __name__=="__main__":
    main()
    