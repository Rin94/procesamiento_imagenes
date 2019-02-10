#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 12:26:29 2019

@author: jared
"""
import os
import sys
def rutaimagen():
    ruta=os.getcwd()+"/dataset_route.txt"
    file=open(ruta,"r")
    
    return file.readline()
    
    

if __name__=="__main__":
    rutaimagen()
    