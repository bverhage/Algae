# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:37:58 2019

@author: billy, joost
"""
import numpy as np
import plots

### if the porces bar does not work as expected in spyder
### than use the following code in the console
### conda install -c conda-forge tqdm
print('------ begin of code ------')

W, Time = differentialEquation.execute()
      
''' --------------- The plots --------------- '''

## old plots not updated yett        
#plots.cycleplot_plot(w,Time)

#plots.MN_plot(w,Time)

#plots.test_plot(w,Time)

#plots.change_plot(w,Time)

## new test plot
plots.test_plots(W,Time)

''' -------------- The Errors ------------ '''

if np.min(W)<0:
    print("ERROR, negative values!")
    
if np.max(W)>10**10:
    print("ERROR, Unstable solution!")

print('------ end of code ------')


