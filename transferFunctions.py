# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:47:15 2019

@author: joost

Describe the 
"""
import numpy as np

''' Constants '''
global const_N0 #Deep nutrients
const_N0=10 #mM m^-3

global const_j #Uptake half saturation
const_j=0.5 #mM m^-3

global const_r #Plant metabolic loss
const_r=0.07 #d^-1

global const_P0 #Grazing threshold
const_P0=0.1 #mM m^-3

global const_g #Loss to carnivores
const_g=0.07 #d^-1

global const_c #maximum grazing rate
const_c=1 #d^-1

global const_K #Grazing half saturation
const_K=1.0 #mM m^-3

global const_f #Grazing efficiency
const_f=0.5 #-

global const_m #Diffusion rate
const_m=3 #md^-1


'''functions'''
    
def zeta(t):
    '''rate of change of the mixed layer dept'''
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

def zetaPlus(t):
    return max(0,zeta(t)) #maybe need to numpify t here
        
def ChangeLayerDepth(t):
    ans=np.array([
                 [zeta(t)],
                 [0],
                 [0],
                 [0]
                 ])
    return(ans)
    
    
def NPtransfer(t,w):
    '''due to pythoplankton eating the nutrients'''
    
    def alpha(t):
        '''the photosynthetic rate of phytoplankton'''
        return (0.4-0.3*np.cos(2*np.pi/365.25*t))
    
    ans=(alpha(t)*w[1,-1]/(const_j+w[1,-1])-const_r)*w[2,-1] #Note to self (J): w[...,-1] means last value
    ans=np.array([
                 [0],
                 [-ans],
                 [ans],
                 [0]
                 ])
    return(ans)
    
def DeepDiffusion(t,w):
    '''Transmission of Nutrients due to deep diffusion'''
    frac=(const_m + zetaPlus(t))/w[0,-1]
    ans=np.array([
                 [0],
                 [frac*(const_N0-w[1,-1])],
                 [-frac*w[2,-1]],
                 [0]
                 ])
    return(ans)

def ShallowingHerbivoreDeath(t,w):
    '''due to a swollowing mixed layer depth'''
    ans=np.array([
                 [0],
                 [0],
                 [0],
                 [-zeta(t)/w[0,-1]*w[3,-1]]
                 ])
    return(ans)

def PHtransfer(t,w):
    '''due to the herbevores eating the pytho plankton'''
    grazingthreshold=np.max(w[2,-1]-const_P0,0)
    ans=const_c*(grazingthreshold)/(const_K+grazingthreshold)*w[3,-1]
    ans=np.array([
                 [0],
                 [0],#(1-const_f)*ans],
                 [-1*ans],
                 [const_f*ans]
                 ])
    return(ans)
    
def LosstoCarnifores(t,w):
    # the loss of herbivores due to carnivores
    ans=np.array([
                 [0],
                 [0],
                 [0],
                 [-const_g*w[3,-1]]
                 ])
    return(ans)
    
def internalExchange(t,w):
    '''Describes the internal change (source) part of the transfer'''
    #change of layer depth
    ans=ChangeLayerDepth(t)
    
    #transfer from N to P
    ans = ans + NPtransfer(t,w)
    
    #transfer due to diffusion
    ans += DeepDiffusion(t,w)
    
    #consequences of the changing layer depth
    ans += ShallowingHerbivoreDeath(t,w)
        
    #transfer from P to H (grazing)
    ans += PHtransfer(t,w)
    
    #loss due to carnivores
    ans += LosstoCarnifores(t,w)
    
    return ans