# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 21:44:39 2020

@author: Bipin Kumar
"""

s = 'azcbobobegghakl'
count = 0
bobcount = 0
while count < len(s):
    a=s[count:count+3]
    if a == "bob":
        bobcount += 1
    count += 1
print("Number of times bob occurs is:", bobcount)