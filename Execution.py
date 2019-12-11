# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:37:58 2019

@author: billy, joost
"""

import numpy as np
import plots
from classes.classDifferentialEquation import differentialEquation as de

import InitialConditions as IC

''' --------------- Execution --------------- '''
'''initialisation'''
W0=IC.IC1(de.dx,de.N)

'''execution on initial W0'''
W, Time = de.execute(W0) #simulation with progress bar
      
''' --------------- The plots --------------- '''
plots.test_plots(W,Time) #very insightful

plots.Xslider(W,Time) # does currently not work if you run the exact code that is within the function it does work
plots.Tslider(W,Time) # does currently not work if you run the exact code that is within the function it does work

''' -------------- The Errors ------------ '''
if np.min(W)<0:
    print("ERROR, negative values!")
    
if np.max(W)>10**10:
    print("ERROR, Unstable solution!")
