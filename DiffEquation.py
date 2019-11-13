# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:37:14 2019

@author: billy
"""
import numpy as np

if __name__ == "__main__":    
    print("This is the Differential equation.")
    print("To run the programm run Excecution.py")


## constants
# the g
global const_g
const_g=0.07

global const_c
const_c=1

global const_P0
const_P0=0.1

global const_k
const_k=0.1

global const_f
const_f=0.5


  
## ------------ the differential eq --------------    
def f(t,w):
    ''' The differential equation that has to be solved.
        imputs: t is time array
                w matrix consisting of w=[w0,w1,w2,...,wn]
                with wi=[u1(i),u2(i),u3(i),...,um(i)]^T
                
        Returns:The next numerical approximation of the solution.
                wn+1=[u1(n+1),u2(n+1),...,un(n+1)]^T'''
    
    ## this is the linear part of the differential equation
    ## Little is linair so this matrix A is moslty filled with 0
    ## the dimentions of A are 2x2
    ## The first value is P and the second H
    ##
    ##       | P |
    ##       | H |
    
    A=np.array([
                [0,0],
                [0,-const_g]
                ])
    





    
    ##The total differential equation.
    
    #Linear part
    ans=A.dot(w)
    
    #alpha
    ans=ans+alpha(t,w)
    #non linear part of P
    ans=ans+non_linear_transfere(t,w)
    
    return(ans)    




## ----------------Non linear funcitons-------------------
def alpha(t,w):
    ans=(0.4+0.3*np.cos(2*np.pi/365.25*t))*w[0,-1]
    ans=np.array([
                 [ans],
                 [0]
                 ])
    return(ans)

    
def non_linear_transfere(t,w):
    grazhingtheresehold=np.max([w[0,-1]-const_P0,0])
    ans=const_c*(grazhingtheresehold)/(const_k+grazhingtheresehold)*w[1,-1]
    ans=np.array([
                 [-ans],
                 [const_f*ans]
                 ])
    return(ans)
    
    