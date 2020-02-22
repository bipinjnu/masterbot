# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 21:23:22 2020

@author: Bipin Kumar
"""

count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))