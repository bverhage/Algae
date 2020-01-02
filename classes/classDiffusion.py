# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:59:32 2019

@author: joost
"""
import numpy as np
from classes.classDerivatives import derivatives
secondDerivative = derivatives.secondDerivative

class diffusion:
    '''diffusion factors'''
    Dn = 10**-2 #Diffusion coefficient of nutrients #This is an absolute guess !!!
    Dp = 10**-2 #Diffusion coefficient of phytoplankton #This is an absolute guess !!!
    
    '''functions'''
    def totalDiffusion(t,Wstep,dx, boundary):
        '''total diffusion'''
        nX, nD = Wstep.shape
        #n = len(Wstep)
        M0, N0, P0, H0 = boundary
        tot = np.block([
                     [np.zeros(nX)], #M
                     [diffusion.Dn*secondDerivative(Wstep[:,1],dx,(N0,N0))], #N
                     [diffusion.Dp*secondDerivative(Wstep[:,2],dx,(P0,P0))], #P
                     [np.zeros(nX)]  #H
                     ])
    
        tot=np.transpose(tot)
        
        return tot
        
    
    
    
