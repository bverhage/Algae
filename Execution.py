# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:37:58 2019

@author: billy, joost
"""
import numpy as np
import plots
from classes.classDifferentialEquation import differentialEquation

''' --------------- Execution --------------- '''
M0, N0, P0, H0 = 60, 9.64202509, 0.1545726, 0.166578
W, Time = differentialEquation.execute(M0,N0,P0,H0) #simulation with progress bar
      
''' --------------- The plots --------------- '''
plots.test_plots(W,Time) #very insightful

''' -------------- The Errors ------------ '''
if np.min(W)<0:
    print("ERROR, negative values!")
    
if np.max(W)>10**10:
    print("ERROR, Unstable solution!")
