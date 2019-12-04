# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:59:32 2019

@author: joost
"""
import numpy as np
from derivatives import secondDerivative

class diffusion:
    '''diffusion factors'''
    Dn = 10**-6 #Diffusion coefficient of nutrients #This is an absolute guess !!!
    Dp = 10**-6 #Diffusion coefficient of phytoplankton #This is an absolute guess !!!
    
    '''functions'''
    def totalDiffusion(t,w):
        #YET TO BE IMPLEMENTED
        return np.array([
                     [0], #M
                     [0], #N
                     [0], #P
                     [0]  #H
                     ])
        
    
    
    
