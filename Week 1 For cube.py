# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:57:38 2020

@author: Bipin Kumar
"""

cube = 11
for guess in range(cube+1):
    if guess**3 == cube:
        print ("Cube root of ", cube, " is ",guess)
        