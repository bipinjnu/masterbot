# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 21:05:48 2020

@author: Bipin Kumar
"""

cube = -27
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, " is not a perfect cube")
else:
    if cube < 0:
        guess = -guess
    print ("Cube root of ", cube, " is ",guess)
        