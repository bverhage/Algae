# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:37:14 2019

@author: billy
"""
import numpy as np
from transferFunctions import internalExchange
from diffusionFunctions import totalDiffusion
from currentFunctions import totalCurrent

if __name__ == "__main__":    
    print("This is the Differential equation.")
    print("To run the programm run Excecution.py")


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
    ans=f(t,W[0])
    for i in range(1,len(W)):
        ans=np.append(ans,f(t,W[i]),axis=1)
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
    
