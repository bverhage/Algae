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
    # Zoals besproken bij Deltares nemen we alle k=1, want de nutrienten en algen gaan bij benadering met gelijke snelheid als het water
    
    def V(n,t):
        # If this is not constant in x, we should include another term in the pde due to the product rule! - Joost
        c = 0.01 #0.1*np.sin(0.5/(2*np.pi)*t) 
        return c*np.ones(n)
        
    '''functions'''
    def totalCurrent(t,Wstep,dx, boundary):
        '''boundary are the initial values of M0, N0, P0, H0 respectively
        We assume that there is no divergence in the currentfield (so no accumulation)
        '''
        n = len(Wstep)
        #assumption divergence is zero!
        M0, N0, P0, H0 = boundary
        
        tot = np.block([
                     [np.zeros(n)], #M
                     [-np.multiply(current.V(n,t), current.kN*firstDerivative(Wstep[:,1],dx,(N0,N0)))], #N
                     [-np.multiply(current.V(n,t), current.kP*firstDerivative(Wstep[:,2],dx,(P0,P0)))], #P
                     [np.zeros(n)]  #H
                     ])
        return np.transpose(tot)