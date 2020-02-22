# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 21:30:23 2020

@author: Bipin Kumar
"""

s = 'azcbobobegghakl'
count = 0
for a in s:
    if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
       count += 1
print("Number of vowels: ", count)
        