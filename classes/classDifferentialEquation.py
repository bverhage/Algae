# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:37:14 2019

@author: billy
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
    # hyperparameters
    #   space
    dx=1 # space jump delta x
    N = 100 # number of delta x'es
    
    #   time
    t0 = 0 # time starting point
    tE = 365.25 #time ending point
    dt = 0.5 #step time

    ## ----------- the total differential eq --------------
    def F(t,W):
        ''' The Total differential equation for each x_n 
            imputs: t time as array
                    W total matrix for every slice
                    W=[w(x1),w(x2),w(x3),...,w(xN)]
                    Where w(x1)=[w0(x1),w1(x1),...,wn(w1)]
        
        notice that W has the form
        
        |w1| the w matrix for x=0 
        |w2| the w matrix for x=deltax
        |w3| the w matrix for x=2deltax
         .
         . 
         .
        |wN| the w matrix for x=Ndeltax
        
        to call the w of ith position zeta The code: W[i]
        '''
        nX, nD, _ = W.shape #size of grid and number of dimensions
        
        #internal f over whole the F.
        ans=differentialEquation.f(t,W[0])
        for i in range(1,len(W)):
            ans=np.append(ans,differentialEquation.f(t,W[i]),axis=1)
        return(ans.transpose().reshape(((nX,nD,1))))
        
        
    ## ------------ step differential eq --------------    
    def f(t,w):
        ''' The differential equation that has to be solved.
            inputs: t is time array
                    w matrix consisting of w=[w0,w1,w2,...,wn]
                    with wi=[u1(i),u2(i),u3(i),...,um(i)]^T
                    
            Returns:The next numerical approximation of the solution.
                    wn+1=[u1(n+1),u2(n+1),...,un(n+1)]^T
        
        
        notice that w has the form
        
               | M | mixed layer dept             w[0,-1]
               | N | nutrient concentration       w[1,-1]
               | P | pythoplankton concentration  w[2,-1]
               | H | herbivore concentration      w[3,-1]
        '''
    
        # ---The total differential equation---
        
        ans = internalExchange(t,w)
        ans += totalDiffusion(t,w) #yet to be implemented
        ans += totalCurrent(t,w) #yet to be implemented
        return(ans)    
    
    def execute(M0,N0,P0,H0):
        '''Executing the method with initial condition M0,N0,P0,H0'''
        NumMet = RK #Numerical Method
        
        ''' ----------- Initialisation -------------- '''
        #creating the initial w matrix
        w0=np.block([
                        [M0],       # M0 Inital mixed layer dept     
                        [N0],         # N0 Inital nutrients concentration
                        [P0],    # P0 Initial pythoplankton conenctration
                        [H0],    # H0 Initial herbivore concentration
                        ])
        W0=np.tile(w0,(differentialEquation.N,1,1)) #creating the inital condition over the whole of the W
        
        X=np.linspace(0,differentialEquation.N*differentialEquation.dx,differentialEquation.N)
        #W0[:,1,:]=0.0*W0[:,1,:]+5*np.exp(-0.1*(X-50)**(2)).reshape(differentialEquation.N,1)
        W0[:,2,:]=0.0*W0[:,2,:]+1*P0/differentialEquation.N*X.reshape(differentialEquation.N,1)
        
        
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