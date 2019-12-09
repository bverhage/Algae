# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:37:58 2019

@author: billy, joost
"""
import numpy as np
import plots
from classes.classDifferentialEquation import differentialEquation as de

''' --------------- Execution --------------- '''
'''initialisation'''
w0=np.block([
                        [de.M0],       # M0 Inital mixed layer dept     
                        [de.N0],         # N0 Inital nutrients concentration
                        [de.P0],    # P0 Initial pythoplankton conenctration
                        [de.H0],    # H0 Initial herbivore concentration
                        ])
W0=np.tile(w0,(de.N,1,1)) #creating the inital condition over the whole of the W

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
