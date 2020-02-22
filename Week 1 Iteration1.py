# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:25:29 2020

@author: Bipin Kumar
"""

x = 4
ans = 0
itersLeft = x
while (itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft - 1
print (str(x) + "*" + str(x) + "=" + str(ans))
    