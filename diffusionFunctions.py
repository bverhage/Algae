# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:59:32 2019

@author: joost
"""
import numpy as np

'''velocity factors'''
global const_Dn #Diffusion coefficient of nutrients
const_Dn = 10**-6 #This is an absolute guess !!!

global const_Dp #Diffusion coefficient of phytoplankton
const_Dn = 10**-6 #This is an absolute guess !!!

'''functions'''
def totalDiffusion(t,w):
    return np.zeros([4,1]) #yet to be implemented