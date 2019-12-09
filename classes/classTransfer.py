# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:47:15 2019

@author: joost

Describe the 
"""
import numpy as np

class transfer:
    
    ''' Transfer coefficients '''
    N0=10 #mM m^-3 #Deep nutrients
    j=0.5 #mM m^-3 #Uptake half saturation
    r=0.07 #d^-1 #Plant metabolic loss
    P0=0.1 #mM m^-3 #Grazing threshold
    g=0.07 #d^-1 #Loss to carnivores
    c=1 #d^-1 #maximum grazing rate
    K=1.0 #mM m^-3 #Grazing half saturation
    f=0.5 #- #Grazing efficiency
    m=3 #md^-1 #Diffusion rate
    
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
        return np.max([0,transfer.zeta(t)])
            
    def ChangeLayerDepth(t):
        ans=np.array([
                     [transfer.zeta(t)],
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
        
        ans=(alpha(t)*w[1,-1]/(transfer.j+w[1,-1])-transfer.r)*w[2,-1] #Note to self (J): w[...,-1] means last value
        ans=np.array([
                     [0],
                     [-ans],
                     [ans],
                     [0]
                     ])
        return(ans)
        
    def DeepDiffusion(t,w):
        '''Transmission of Nutrients due to deep diffusion'''
        frac=(transfer.m + transfer.zetaPlus(t))/w[0,-1]
        ans=np.array([
                     [0],
                     [frac*(transfer.N0-w[1,-1])],
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
                     [-transfer.zeta(t)/w[0,-1]*w[3,-1]]
                     ])
        return(ans)
    
    def PHtransfer(t,w):
        '''due to the herbevores eating the pytho plankton'''
        grazingthreshold=np.max([w[2,-1]-transfer.P0,0])
        ans=transfer.c*(grazingthreshold)/(transfer.K+grazingthreshold)*w[3,-1]
        ans=np.array([
                     [0],
                     [0],#(1-const_f)*ans],
                     [-1*ans],
                     [transfer.f*ans]
                     ])
        return(ans)
        
    def LosstoCarnifores(t,w):
        # the loss of herbivores due to carnivores
        ans=np.array([
                     [0],
                     [0],
                     [0],
                     [-transfer.g*w[3,-1]]
                     ])
        return(ans)
        
    def internalExchange(t,w):
        '''Describes the internal change (source) part of the transfer'''
        #change of layer depth
        ans = transfer.ChangeLayerDepth(t)
        
        #transfer from N to P
        ans = ans + transfer.NPtransfer(t,w)
        
        #transfer due to diffusion
        ans += transfer.DeepDiffusion(t,w)
        
        #consequences of the changing layer depth
        ans += transfer.ShallowingHerbivoreDeath(t,w)
            
        #transfer from P to H (grazing)
        ans += transfer.PHtransfer(t,w)
        
        #loss due to carnivores
        ans += transfer.LosstoCarnifores(t,w)
        
        return ans

