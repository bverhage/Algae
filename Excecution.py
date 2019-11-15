

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:37:58 2019

@author: billy
"""

import numpy as np
import matplotlib.pyplot as plt
import plots
from NumericalSolvers import RK,EF,TZ


print('------ begin of code ------')


## boundry conditions

# time starting point  
t0=0

#time ending point
tE=365

#step time
dt=0.1


# inital conditions

#creating the initial w matrix

w0=np.block([
                [60],       # M0 Inital mixed layer dept     
                [0.2],         # N0 Inital nutrients concentration
                [0.115],    # P0 Initial pythoplankton conenctration
                [0.01],    # H0 Initial herbivore concentration
                ])


## the first step 
## the starting point for the total data matrix w
w=w0

## the starting point for the time vector Time
Time=[t0]


##----------- The excecution --------------
while(Time[-1]<tE):
    
    #appling the numerical method over the differnential eqation f.
    
    wn=RK(Time,w,dt)
    
    #adding the next point to the numerical matrix w
    
    w=np.append(w,wn,axis=1)

    #going to the next time step.
    
    Time.append(Time[-1]+dt)
    
    #reitterating everything until tE
    
  
## --------------- The plots --------------- 
    
plots.cycleplot_plot(w,Time)

plots.MN_plot(w,Time)

plots.test_plot(w,Time)
plt.show()

print('------ end of code ------')
