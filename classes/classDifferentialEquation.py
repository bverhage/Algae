# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:37:14 2019

@author: billy, joost
"""
import numpy as np
from NumericalSolvers import RK,EF,TZ
from tqdm import tqdm 

# importing change functions
from classes.classTransfer import transfer
internalExchange = transfer.internalExchange
from classes.classDiffusion import diffusion
totalDiffusion = diffusion.totalDiffusion
from classes.classCurrent import current
totalCurrent = current.totalCurrent



if __name__ == "__main__":    
    print("This is the Differential equation.")
    print("To run the programm run Excecution.py")

class differentialEquation:
    '''Class for the total handling of the differential equation'''
    
    ''' ----------- hyperparameters ----------- '''
    '''space'''
    dx=0.1          # space jump delta x
    N = 100         # number of delta x'es
    
    '''time'''
    t0 = 0          # time starting point
    tE = 365.25     #time ending point
    dt = 0.1        #step time

    '''boundary values'''
    initial = 60, 9.64202509, 0.1545726, 0.166578
    M0, N0, P0, H0 = initial
    
    ''' ----------- the total differential eq -------------- '''
    def F(t,Wstep):
        ''' The Total differential equation for each x_n 
            imputs: t time as array
                    W total matrix for every slice
                    W=[w(x1),w(x2),w(x3),...,w(xN)]
                    Where w(x1)=[w0(x1),w1(x1),...,wn(w1)]
        
        notice that Wstep has the form
        
        |w1| the w matrix for x=0 
        |w2| the w matrix for x=deltax
        |w3| the w matrix for x=2deltax
         .
         . 
         .
        |wN| the w matrix for x=Ndeltax
        
        to call the w of ith position zeta The code: W[i]
        '''
        boundary = differentialEquation.initial #initial values at the boundary, used for first and second derivative in current and diffusion respectively
        
        nX, nD, _ = Wstep.shape #size of grid and number of dimensions
        Wstep=Wstep.reshape(nX,nD)
        
        #internal exchange over whole the F
        tot = np.array([internalExchange(t,Wstep[i]) for i in range(0,len(Wstep))]).reshape(nX,nD)
        
        #diffusion
        tot += totalDiffusion(t,Wstep,differentialEquation.dx,boundary)

        #current
        tot += totalCurrent(t,Wstep,differentialEquation.dx,boundary)
        
        return tot.reshape((nX,nD,1))
        
        
    def execute(W0):
        '''Executing the method with initial condition M0,N0,P0,H0'''
        NumMet = RK#Numerical Method
        
        ''' ----------- Initialisation -------------- '''
        
    
        #creating the initial w matrix
        W=W0 # the first step, the starting point for the total data matrix w
        Time=[differentialEquation.t0] # the starting point for the time vector Time
        
        
        ''' ----------- The execution -------------- '''
        
        ## It uses tqdm to create a proces bar.
        with tqdm(total=int(np.ceil(differentialEquation.tE/differentialEquation.dt))) as pbar:
            while(Time[-1]<differentialEquation.tE):
                
                #appling the numerical method over the differnential eqation f.
                Wn=NumMet(Time,W,differentialEquation.dt, differentialEquation.F)
                
                #adding the next point to the numerical matrix w
                W=np.append(W,Wn,axis=2)
                
                #going to the next time step.
                Time.append(Time[-1]+differentialEquation.dt)
                
                #reitterating everything until tE
                
                ## updating the proces bar
                pbar.update(1)
        
        return W, Time