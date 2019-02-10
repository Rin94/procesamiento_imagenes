#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 20:46:07 2019

@author: jared
"""

import negativo_met
import cv2
import numpy as np
from matplotlib import pyplot as plt


def convolution2D(img,size):
    kernel=np.ones((size,size),np.float32)/(size*size)
    dst=cv2.filter2D(img,-1,kernel)
    return dst


"""
computes the median of all the pixels under the kernel window,
and the central pixel is replaced with this median value.
Is higly effective in removing salt-and-paper noise
The fucking kernel must be a positive and big bonner odd integer
"""
def medianFiltering(img,kernel):
    median=cv2.medianBlur(img,kernel)
    return median



"""
image smooting, is blurring the image, by passing a low-pass filter kernel.
Use handy for removing noise, this is done by taking the average of all pixels
under kernel area and replace the central element with this average
"""
def blurringImage(img,size):
    blur=cv2.blur(img,(size,size))
    return blur

"""
this method consist  of equal filter coefficientes, we specficy the
width and height of the kernel, which should be positive and odd
specify the width and heigth of the kernel
"""
def gaussianFiltering(img,size,param):
    gblur=cv2.GaussianBlur(img,(size,size),param)
    return gblur



def plotTheFilteringShit(img1,img2):
    plt.subplot(121),plt.imshow(img1),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img2),plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()
    
"""
is highly effective at noise removal while preserving edges, but it takes more
computation cost, uses a gaussian filter, and neighboors
"""
def bilateralFiltering(img,kernel,size):
    blur=cv2.bilateralFilter(img,kernel,size,size)
    #blur=cv2.bilateralFilter(img,9,25,25)
    return blur
    

    
    


def main():
    img=negativo_met.load_image("/OpenCV.jpg",1)
    #dst=convolution2D(img,3)
    #blur=blurringImage(img,10)
    #gblur=gaussianFiltering(img,5,0)
    #med=medianFiltering(img,7)
    blur=bilateralFiltering(img,9,75)
    plotTheFilteringShit(img,blur)
    

if __name__=="__main__":
    main()
    