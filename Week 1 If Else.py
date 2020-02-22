# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 11:45:11 2020

@author: Bipin Kumar
"""
x = int(input("Enter an integer: "))
if x%2 == 0:
    if x%3 == 0:
        print("This number is divisible by 2 and 3")
    else:
        print("This number is divisible by 2 but not 3")
elif x%3 == 0:
    print("This number is divisible by 3 but not by 2")
    12