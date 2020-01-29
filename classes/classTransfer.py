# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 23:47:15 2019

@author: joost
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
    
        
    def alpha(t,M,P,H):
        '''
        the photosynthetic rate of phytoplankton
        extra uitleg / documentatie zou handig zijn @billy / @rona
        '''  
        def g(y,t):
            '''help function for alpha'''
            ans=(((y**2)+(t**2))**(1/2))-t*np.log((t+((y**2)+(t**2))**(1/2))/y)
            return(ans)
            
        '''constants'''
        Q = 2 # Maximum photosyntetic rate
        k = 0.10 # light attenuation by water
        alfa=4  #low light photosyntetic slope
        alfat=(0.6-0.4*np.cos(2*np.pi/365.25*t)) #seasonal effects       
        tau=0.5 # day length
        J=2 #light level at the surface at noon
        beta=Q*tau/(alfa*J)
       
        
        ans=((2*Q)/(M*k))*(g(beta*np.e**(k*M),tau)-g(beta,tau)-g(beta*np.e**(k*M),0)+g(beta,0))*np.min([((H+P)**(-1/3)),1])*alfat
        
        
        return ans    
    
    def NPtransfer(t,w):
        '''due to pythoplankton eating the nutrients'''
        
  
        ans=(transfer.alpha(t,w[0],w[2],w[3])*w[1]/(transfer.j+w[1])-transfer.r)*w[2] #Note to self (J): w[...,-1] means last value
        ans=np.array([
                     [0],
                     [-ans],
                     [ans],
                     [0]
                     ])
        return(ans)
        
    def DeepDiffusion(t,w):
        '''Transmission of Nutrients due to deep diffusion'''
        frac=(transfer.m + transfer.zetaPlus(t))/w[0]
        ans=np.array([
                     [0],
                     [frac*(transfer.N0-w[1])],
                     [-frac*w[2]],
                     [0]
                     ])
        return(ans)
    
    def ShallowingHerbivoreDeath(t,w):
        '''due to a swollowing mixed layer depth'''
        ans=np.array([
                     [0],
                     [0],
                     [0],
                     [-transfer.zeta(t)/w[0]*w[3]]
                     ])
        return(ans)
    
    def PHtransfer(t,w):
        '''due to the herbevores eating the pytho plankton'''
        grazingthreshold=np.max([w[2]-transfer.P0,0])
        ans=transfer.c*(grazingthreshold)/(transfer.K+grazingthreshold)*w[3]
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
                     [-transfer.g*w[3]]
                     ])
        return(ans)
        
    def internalExchange(t,w):
        ''' Describes the internal change (source) part of the transfer
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

