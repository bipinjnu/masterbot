# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 12:04:59 2020

@author: Bipin Kumar
"""

x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
    print("x and y are equal")
    if y != 0:
        print("therefore, x/y is ", x/y)
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")
print("thanks")
