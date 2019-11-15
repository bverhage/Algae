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
tE=365*4

#step time
dt=0.1


# inital conditions

#creating the initial w matrix

w0=np.block([
                [0.12],
                [0.1],
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
        
plots.default_plot(w,Time)
plt.show()

print('------ end of code ------')
