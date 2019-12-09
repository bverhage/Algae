# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:59:50 2019

@author: joost
"""
import numpy as np
from derivatives import firstDerivative

class current:
    '''velocity factors'''
    kN = 1 #Dimensionless factor describing the velocity of the nutrients w.r.t. water velocity
    kP = 1 #Dimensionless factor describing the velocity of the phytoplankton w.r.t. water velocity
    kH = 1 #Dimensionless factor describing the velocity of the herbivores w.r.t. water velocity
    
    def V(n,t):
        c = 0
        return c*np.ones(n)
        
    '''functions'''
    def totalCurrent(t,Wstep,dx, boundary):
        '''boundary are the initial values of M0, N0, P0, H0 respectively
        We assume that there is no divergence in the currentfield (so no accumulation)
        '''
        n = len(Wstep)
        #assumption divergence is zero!
        M0, N0, P0, H0 = boundary
        
        tot = np.array([
                     [np.zeros(n)], #M
                     [-np.multiply(current.V(n,t), current.kN*firstDerivative(Wstep[:,1,0],dx,(N0,N0)))], #N
                     [-np.multiply(current.V(n,t), current.kP*firstDerivative(Wstep[:,2,0],dx,(P0,P0)))], #P
                     [np.zeros(n)]  #H
                     ])
        return tot
        #return np.zeros([4,1]) #yet to be implemented