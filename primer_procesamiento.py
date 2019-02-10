#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 17:03:43 2019
Las imágenes en la computación son números

@author: jared
"""

import cv2
from importar_img import rutaimagen

def main():
    imgpath= rutaimagen()+"/4.2.04.tiff"
    #img=cv2.imread(imgpath,1)
    img=cv2.imread(imgpath,0)
    cv2.imshow("lena",img)
    #En python las imagenes se guardan como  un numpy.ndarray
    # N dimensional arrays
    print(type(img))
    print(img)
    #unsignes integer 8-bits todos los datos estan en el rango de 0-255 
    #hay 16777216 de posibles valores
    print(img.dtype)
    
    #imprimir el shape de la imagen (220,220,3) EL ULTIMO ES EL NUMERO DE CANALES DE COLOR
    print(img.shape)
    
    #NUMERO DE DIMENSIONES 3, por el shape 
    print(img.ndim)
    
    #Tamaño de la imagen (sl*sa*nd)
    print(img.size)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    #for i in range (1,5):
     #   cv2.waitKey(1)
    
    
if __name__=="__main__":
    main()      
    
    
    
"""

[127 137 225] RGB cada número es la intensidad del canal de color
BGR openCV lo hace así
Blue=127,
Verde= 137
Roja=225

0 black
255 white

Una imagen conjunto de numeros
[[[127 137 225]
  [127 137 224]
  [119 134 227]
  ...
  [128 141 227]
  [124 150 232]
  [104 120 213]]

 [[127 137 225]
  [127 136 224]
  [119 134 227]
  ...
  [130 144 230]
  [126 155 238]
  [105 124 219]]

 [[122 137 227]
  [118 134 224]
  [117 133 228]
  ...
  [106 113 209]
  [ 96  97 189]
  [ 80  61 149]]

 ...

 [[ 60  28  90]
  [ 61  29  95]
  [ 63  28  97]
  ...
  [ 68  42 126]
  [ 73  58 148]
  [ 73  59 158]]

 [[ 61  24  87]
  [ 62  27  92]
  [ 61  25  95]
  ...
  [ 78  58 143]
  [ 80  67 167]
  [ 78  65 169]]

 [[ 58  22  84]
  [ 62  29  95]
  [ 59  24  93]
  ...
  [ 84  67 159]
  [ 81  70 176]
  [ 80  71 182]]]
"""