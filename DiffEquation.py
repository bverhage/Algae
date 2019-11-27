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
##Deep nutreints
const_N0=10 #mM m^-3

global const_j
##Uptake half saturation
const_j=0.5 #mM m^-3

global const_r
##Plant metabolic loss
const_r=0.07 #d^-1

#const_r=0.07*dt #d^-1

global const_P0
##Grazing threshold
const_P0=0.1 #mM m^-3

global const_g
##Loss to carnivores
const_g=0.07 #d^-1

#const_g=0.07*dt

global const_c
##maximum grazing rate
const_c=1 #d^-1

#const_c=1*dt

global const_K
##Grazing half saturation
const_K=1.0 #mM m^-3

global const_f
##Grazing efficiency
const_f=0.5 #-

global const_m
##Diffusion rate
const_m=3 #md^-1

#const_m=3*dt

## ----------- the total differential eq --------------
def F(t,W):
    ''' The Total differential equation for each x_n 
        imputs: t time as array
                W total matrix for every slice
                W=[w(x1),w(x2),w(x3),...,w(xN)]
                Where w(x1)=[w0(x1),w1(x1),...,wn(w1)]
    '''
    nX, nD, _ = W.shape #size of grid and number of dimensions
    
    ## notice that W has the form
    
    ## |w1| the w matrix for x=0 
    ## |w2| the w matrix for x=deltax
    ## |w3| the w matrix for x=2deltax
    ##  .
    ##  .
    ##  .
    ## |wN| the w matrix for x=Ndeltax
    
    ## to call the w of ith position xi The code
    ## W[i]
    
    #internal f over whole the F.
    ans=f(t,W[0])
    for i in range(1,len(W)):
        #ans[i]=f(t,W[i])
        ans=np.append(ans,f(t,W[i]),axis=1)
    return(ans.transpose().reshape(((nX,nD,1))))
## ------------ the internal differential eq --------------    
def f(t,w):
    ''' The differential equation that has to be solved.
        imputs: t is time array
                w matrix consisting of w=[w0,w1,w2,...,wn]
                with wi=[u1(i),u2(i),u3(i),...,um(i)]^T
                
        Returns:The next numerical approximation of the solution.
                wn+1=[u1(n+1),u2(n+1),...,un(n+1)]^T'''
    
    
    ## notice that w has the form
    
    ##       | M | mixed layer dept             w[0,-1]
    ##       | N | nutrient concentration       w[1,-1]
    ##       | P | pythoplankton concentration  w[2,-1]
    ##       | H | herbivore concentration      w[3,-1]
    

    
    ##The total differential equation.
    
    #change of layer depth
    ans=changelayerdepht(t)
    
    #transfere from N to P
    ans=ans+NPtransfere(t,w)
    
    #transfere due to diffusion
    ans=ans+diffusion(t,w)
    
    #concequences of the chaning layer depht
    ans=ans+swollowingmixedlayer(t,w)
        
    #transfere from P to H
    ans=ans+PHtransfere(t,w)
    
    #loss due to carnivores
    ans=ans+losstoCarnifores(t,w)
    

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
    ans=(0.4-0.3*np.cos(2*np.pi/365.25*t))

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
    
def diffusion(t,w):
    ans=const_m/w[0,-1]
    ans=np.array([
                 [0],
                 [ans*(const_N0-w[1,-1])],
                 [-ans*w[2,-1]],
                 [0]
                 ])
    
    return(ans)

def swollowingmixedlayer(t,w):
    #due to a swollowing mixed layer depth
    ans=np.max(xi(t),0)/w[0,-1]
    ans=np.array([
                 [0],
                 [ans*(const_N0-w[1,-1])],
                 [-ans*w[2,-1]],
                 [-xi(t)/w[0,-1]*w[3,-1]]
                 ])
    return(ans)

def PHtransfere(t,w):
    #due to the herbevores eating the pytho plankton
    grazhingtheresehold=np.max(w[2,-1]-const_P0,0)
    ans=const_c*(grazhingtheresehold)/(const_K+grazhingtheresehold)*w[3,-1]
    ans=np.array([
                 [0],
                 [0],#(1-const_f)*ans],
                 [-1*ans],
                 [const_f*ans]
                 ])
    return(ans)
    
def losstoCarnifores(t,w):
    # the loss of herbivores due to carnivores
    ans=np.array([
                 [0],
                 [0],
                 [0],
                 [-const_g*w[3,-1]]
                 ])
    return(ans)
    
    