# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:59:50 2019

@author: joost
"""
import numpy as np
from derivatives import firstDerivative

class current:
    '''velocity factors'''
    k_N = 1 #Dimensionless factor describing the velocity of the nutrients w.r.t. water velocity
    k_P = 1 #Dimensionless factor describing the velocity of the phytoplankton w.r.t. water velocity
    k_H = 1 #Dimensionless factor describing the velocity of the herbivores w.r.t. water velocity
    
    def V(x):
        return 1 #THIS SHOULD BE CHANGED
        
    '''functions'''
    def totalCurrent(t,w):
        n = len(w)
        
        return np.zeros([4,1]) #yet to be implemented