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
    def totalDiffusion(t,Wstep,dx, boundary):
        '''total diffusion'''
        n = len(Wstep)
        M0, N0, P0, H0 = boundary
        tot = np.array([
                     [np.zeros(n)], #M
                     [diffusion.Dn*secondDerivative(Wstep[:,1,0],dx,(N0,N0))], #N
                     [diffusion.Dp*secondDerivative(Wstep[:,2,0],dx,(P0,P0))], #P
                     [np.zeros(n)]  #H
                     ])
        return tot
        
    
    
    
