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

global const_N0
const_N0=10

global const_j
const_j=0.5

global const_r
const_r=0.07

global const_P0
const_P0=0.1

global const_g
const_g=0.07

global const_c
const_c=1

global const_k
const_k=0.1

global const_f
const_f=0.5

global const_m
const_m=3

  
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
    ## the dimentions of A are 4x4
    ## The first value is M and the second N the third is P and the forth is H
    ##  
    ##       | M | mixed layer dept             w[0,-1]
    ##       | N | nutrient concentration       w[1,-1]
    ##       | P | pythoplankton concentration  w[2,-1]
    ##       | H | herbivore concentration      w[3,-1]
    
    A=np.array([
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,-const_g]
                ])
    





    
    ##The total differential equation.
    
    #Linear part
    ans=A.dot(w)
    
    #change of layer depth
    ans=ans+changelayerdepht(t)
    
    #transfere from N to P
    ans=ans+NPtransfere(t,w)
    
    #concequences of the chaning layer depht
    ans=ans+swollowingmixedlayer(t,w)
        
    #transfere from P to H
    ans=ans+PHtransfere(t,w)

    return(ans)    




## ----------------Non linear funcitons-------------------
    
def xi(t):
    ## rate of change of the mixed layer dept
    t=np.mod(t,365)
    m=np.floor(t/(365.25/12))+1
    
    if m==1:
        ans=(80-60)/(2*365.25/12)
    elif m==2:
        ans=(80-60)/(2*365.25/12)
    elif m==3:
        ans=0
    elif m==4:
        ans=(20-80)/(365.25/12)
    elif m==5:
        ans=0
    elif m==6:
        ans=0
    elif m==7:
        ans=0
    elif m==8:
        ans=0
    elif m==9:
        ans=(60-20)/(4*365.25/12)
    elif m==10:
        ans=(60-20)/(4*365.25/12)
    elif m==11:
        ans=(60-20)/(4*365.25/12)
    elif m==12:
        ans=(60-20)/(4*365.25/12)
    return(ans)
        
    
def changelayerdepht(t):
    ans=np.array([
                 [xi(t)],
                 [0],
                 [0],
                 [0]
                 ])
    return(ans)
    
def alpha(t,w):
    #the photosynthetic rate of phytoplankton
    ans=(0.4+0.3*np.cos(2*np.pi/365.25*t))

    return(ans)
    
def NPtransfere(t,w):
    #due to pythoplankton eating the nutrients
    ans=(alpha(t,w)*w[1,-1]/(const_j+w[1,-1])-const_r)*w[2,-1]
    ans=np.array([
                 [0],
                 [-ans],
                 [ans],
                 [0]
                 ])
    return(ans)
    
def swollowingmixedlayer(t,w):
    #due to a swollowing mixed layer depth
    ans=(const_m+np.max(xi(t),0))/w[0,-1]
    ans=np.array([
                 [0],
                 [ans*(const_N0-w[1,-1])],
                 [-ans*w[2,-1]],
                 [-xi(t)/w[0,-1]*w[3,-1]]
                 ])
    return(ans)

def PHtransfere(t,w):
    #due to the herbevores eating the pytho plankton
    grazhingtheresehold=np.max([w[2,-1]-const_P0])
    ans=const_c*(grazhingtheresehold)/(const_k+grazhingtheresehold)*w[3,-1]
    ans=np.array([
                 [0],
                 [0],
                 [-1*ans],
                 [const_f*ans]
                 ])
    return(ans)
    
    