# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:49:33 2020

@author: Bipin Kumar
"""

import webbrowser, pyperclip
address = pyperclip.paste()
#print(address)
s = address.split('\n')
home = '26.8015285 84.5584678'
address1 = s[0]
address2 = s[1]

print(address1)
print(address2)
webbrowser.open('https://www.google.com/maps/dir/' + home + '/' + address1 + '/' + address2 + '/' + home)
