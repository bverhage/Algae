# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:52:10 2019

@author: billy
"""

import numpy as np


    
''' initial coefficients '''
M0 = 60           #m        #inital mixed layer dept
N0 = 9.64202509   #mM m^-3  # inital Nutrients concentration
P0 = 0.1545726    #mM m^-3  # inital pythoplankton concentration
H0 = 0.166578     #mM m^-3  # inital herbevores concentration

    
'''functions'''
def UniformIC(dx,N):
    w0=np.block([
                [M0],       # M0 Inital mixed layer dept     
                [N0],         # N0 Inital nutrients concentration
                [P0],    # P0 Initial pythoplankton conenctration
                [H0],    # H0 Initial herbivore concentration
                ])
    W0=np.tile(w0,(N,1,1)) #creating the inital condition over the whole of the W

    return(W0)
    
def IC1(dx,N):
    w0=np.block([
                [M0],       # M0 Inital mixed layer dept     
                [N0],         # N0 Inital nutrients concentration
                [P0],    # P0 Initial pythoplankton conenctration
                [H0],    # H0 Initial herbivore concentration
                ])
    W0=np.tile(w0,(N,1,1)) #creating the inital condition over the whole of the W
    X=np.linspace(0,N*dx,N)
    #W0[:,1,:]=0.0*W0[:,1,:]+5*np.exp(-0.1*(X-50)**(2)).reshape(differentialEquation.N,1)
    W0[:,2,:]=0.0*W0[:,2,:]+1*P0/N*X.reshape(N,1)

    return(W0)
        

        
        
