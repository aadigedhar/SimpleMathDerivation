#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 01:16:21 2018

@author: aadi
"""

# Differenciation program for nth order--------


import matplotlib.pyplot as plt
import numpy as np
import math
print('Enter function for Differenction :-')
nth = 0
while (nth == 0):
   nth = int(input('Which number of Differenction you want :'))
 

spacing = .01
b =2* math.pi
a = 0
number_of_part =int((b-a)/spacing)
x_axis = np.linspace(a,b,number_of_part)
y = np.array([])
for x in x_axis:
    q = x**2
    y = np.append(y,q)

#plt.plot(x_axis,y)
def defer(y_axis,spacing,number_of_part):
    y_temp=np.array([])
    for i in range(0,number_of_part-1):
        e = (y_axis[i+1]-y_axis[i])/spacing
        y_temp = np.append(y_temp,e)
    y_temp = np.append(y_temp,y_temp[-1])
    return y_temp


t = y
for i in range(0,n):
    t = defer(t,spacing,number_of_part)
plt.plot(x_axis,t)    