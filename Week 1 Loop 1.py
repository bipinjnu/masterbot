# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:43:05 2020

@author: Bipin Kumar
"""

for i in range(50):
    print("Outer Loop: ", i)
    for j in range (40):
        print("Inner loop: ", j)
    print("Outside of inner loop, back to outer loop")
    