# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 21:19:40 2020

@author: Bipin Kumar
"""

iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 