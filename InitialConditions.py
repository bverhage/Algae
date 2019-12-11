# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:52:10 2019

@author: billy
"""

import numpy as np



if __name__ == "__main__":
    print("\n\nThis is the InitalCondition program.")
    print("To run the programm run Execution.py, but I will do that for you this time:")
    exec(open("Execution.py").read());

''' initial coefficients '''
M0 = 60           #m        #inital mixed layer dept
N0 = 9.64202509   #mM m^-3  # inital Nutrients concentration
P0 = 0.1545726    #mM m^-3  # inital pythoplankton concentration
H0 = 0.166578     #mM m^-3  # inital herbevores concentration

    
'''functions'''
def UniformIC(dx,N):
    W0=np.block([
                [M0*np.ones([N,1,1])],       # M0 Inital mixed layer dept     
                [N0*np.ones([N,1,1])],         # N0 Inital nutrients concentration
                [P0*np.ones([N,1,1])],    # P0 Initial pythoplankton conenctration
                [H0*np.ones([N,1,1])],    # H0 Initial herbivore concentration
                ])
    return(W0)
    
def IC1(dx,N):
    W0=np.block([
                [M0*np.ones([N,1,1])],       # M0 Inital mixed layer dept     
                [N0*np.ones([N,1,1])],         # N0 Inital nutrients concentration
                [P0*np.ones([N,1,1])],    # P0 Initial pythoplankton conenctration
                [H0*np.ones([N,1,1])],    # H0 Initial herbivore concentration
                ])
    
    X=np.linspace(0,N*dx,N) #X coridinates
    
    W0[:,1,:]=1*W0[:,1,:]-5*np.exp(-0.1*(X-0.5*N*dx)**(2)).reshape(N,1)
    #W0[:,2,:]=0.0*W0[:,2,:]+1*P0/N*X.reshape(N,1)

    return(W0)
        

        
        
