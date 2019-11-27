# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:59:50 2019

@author: joost


"""
import numpy as np

'''velocity factors'''
global k_N #Dimensionless factor describing the velocity of the nutrients w.r.t. water velocity
k_N = 1 

global k_P #Dimensionless factor describing the velocity of the phytoplankton w.r.t. water velocity
k_P = 1

global k_H #Dimensionless factor describing the velocity of the herbivores w.r.t. water velocity
k_H = 1

'''functions'''
def totalCurrent(t,w):
    return np.zeros([4,1]) #yet to be implemented