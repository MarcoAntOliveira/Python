#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 08:41:35 2022

@author: diogo.siebert
"""

from scipy.interpolate import interp1d
from scipy.optimize import bisect 
import numpy as np
from imageio import imread
import matplotlib.pylab as plt 

I = imread("Peao.png")

R = I[:,:,0]
Nrow, Ncol = R.shape 

rowList = []
colList = []

col = 0
y = R[:,col]
x = np.arange(0,Nrow)
f = interp1d(x,y.astype(np.float64)-127, kind = "slinear" )   
yb = bisect(f,0,(Nrow-1)/2,xtol=1E-2)

rowList.append(yb)
colList.append(col)

for row in range(40,500,15):
    y = R[row,:]
    x = np.arange(0,Ncol)
    f = interp1d(x,y.astype(np.float64)-127, kind = "slinear" )   
    rb = bisect(f,0,Ncol-1,xtol=1E-2)
    rowList.append( row )
    colList.append( rb )

col = 0
y = R[:,col]
x = np.arange(0,Nrow)
f = interp1d(x,y.astype(np.float64)-127, kind = "slinear" )   
yb = bisect(f,(Nrow-1)/2,(Nrow-1),xtol=1E-2)

rowList.append(yb)
colList.append(col)

#X = np.linspace(x[0],x[-1], 1000)
#plt.plot(X,f(X) )
#plt.plot(x,y,"o")

r = interp1d(rowList,colList, kind = 'cubic' )
y = np.linspace( rowList[0], rowList[-1], 200 )

plt.imshow(R)
plt.plot(r(y), y , "r")
#plt.plot(colList,rowList,"ro")
plt.show()    


