# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:37:58 2019

@author: billy, joost
"""

import numpy as np
from plots import TslicePlot, XslicePlot, Xslider, Tslider, colorplot, change_plot, Tanimation, Xanimation
from classes.classDifferentialEquation import differentialEquation as de
import InitialConditions as IC

''' --------------- Execution --------------- '''
'''initialisation'''
W0= IC.IC_Gauss(de.dx,de.N)

'''execution on initial W0'''
W, Time = de.execute(W0) #simulation with progress bar
      
''' --------------- The plots --------------- '''
#plots of slices at specific t and x respectively
tn = 200 #position of t-slice
TslicePlot(W,Time, tn) #slice plot at tn over all x
xn = 10 #position of t-slice
XslicePlot(W,Time, xn) #slice plot at xn over all t

#2D (x,t) with color
colorplot(W,Time)

#Change plot ???
change_plot(W,Time)

#Slider plots
xslide = Xslider(W,Time)
tslide = Tslider(W,Time)

''' -------------- The Errors ------------ '''
if np.min(W)<0:
    print("ERROR, negative values!")
    
if np.max(W)>10**10:
    print("ERROR, Unstable solution!")
