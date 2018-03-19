#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 18:47:26 2018

@author: aadi
"""

import matplotlib.pyplot as plt
import numpy as np
import math

spacing = 0.01
b =10    # 2* math.pi
a = -10
number_of_part =int((b-a)/spacing)
x_axis = np.linspace(a,b,number_of_part)

y_axis = np.array([])
for x in x_axis:
    y = x**2#math.sin(x)
    y_axis = np.append(y_axis,y)
 
plt.plot(x_axis,y_axis) 
        
def integrestion(y_axis,spacing,number_of_part):
    e = 0
    y_temp = np.array([])
    for i in range(0,number_of_part):
        e += y_axis[i] * spacing 
        y_temp = np.append(y_temp,e)
    
    return y_temp

for i in range(0,1):
    t = integrestion(y_axis,spacing,number_of_part)
plt.plot(x_axis,t)
print(sum)
