# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:37:58 2019

@author: billy
"""

import numpy as np

import plots

from NumericalSolvers import RK,EF,TZ

from tqdm import tqdm 

### if the porces bar does not work as expected in spyder
### than use the following code in the console
### conda install -c conda-forge tqdm


print('------ begin of code ------')


## boundry conditions

# space jump delta x
Delta_x=1

# number of delta x'es
N=100

## initial condition

# time starting point  
t0=0

#time ending point

tE=365.25

#step time
dt=0.5

#creating the initial w matrix

w0=np.block([
                [60],       # M0 Inital mixed layer dept     
                [9.64202509],         # N0 Inital nutrients concentration
                [0.1545726],    # P0 Initial pythoplankton conenctration
                [0.166578],    # H0 Initial herbivore concentration
                ])

#creating the inital condition over the whole of the W
W0=np.tile(w0,(N,1,1))


## the first step 
## the starting point for the total data matrix w
W=W0

## the starting point for the time vector Time
Time=[t0]





##----------- The excecution --------------
## It uses tqdm to create a proces bar.

with tqdm(total=int(np.ceil(tE/dt))) as pbar:
    while(Time[-1]<tE):
        
        #appling the numerical method over the differnential eqation f.
        
        Wn=RK(Time,W,dt)
        
        #adding the next point to the numerical matrix w
        
        W=np.append(W,Wn,axis=2)
        
    
        #going to the next time step.
        
        Time.append(Time[-1]+dt)
        
        #reitterating everything until tE
        
        ## updating the proces bar
    
        pbar.update(1)
    
      
## --------------- The plots ---------------   

## old plots not updated yett        
#plots.cycleplot_plot(w,Time)

#plots.MN_plot(w,Time)

#plots.test_plot(w,Time)

#plots.change_plot(w,Time)

## new test plot

plots.test_plots(W,Time)

## -------------- The Errors ------------

if np.min(W)<0:
    print("ERROR, negative values!")
    
if np.max(W)>10**10:
    print("ERROR, Unstable solution!")

print('------ end of code ------')


