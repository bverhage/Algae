# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:38:51 2019

@author: billy
"""
if __name__ == "__main__":
    print("This is the Plots program.")
    print("To run the programm run Excecution.py")
    
import numpy as np

import matplotlib.pyplot as plt




##------------- The plots -----------------
def cycleplot_plot(w,Time):
    
    fig3 = plt.figure()
    
    ax = fig3.add_subplot(111)
    
    
    plt.plot(Time,w[2,:],'-')
    plt.plot(Time,w[3,:],'--')
    plt.xlabel('Time(d)')
    plt.ylabel('c')
    plt.title('Algae')
    ax.legend(('phytoplankton','herbivore'))
    
    return;
    
def MN_plot(w,Time):
    
    fig2 = plt.figure()
    
    ax = fig2.add_subplot(121)
    
    plt.plot(Time,w[0,:],'--')
    plt.xlabel('Time (d)')
    plt.ylabel('dept (m)')
    plt.title('mixed layer dept')
    ax.legend('Mixed layer dept')
    
    ax2 = fig2.add_subplot(122)
    
    plt.plot(Time,w[1,:],'--')
    plt.xlabel('Time (d)')
    plt.ylabel('concentration Nutrients (mmol/m^2)')
    plt.title('nutrients')
    ax2.legend('nutrients')
    return;
    
def test_plot(w,Time):
    
    fig2 = plt.figure()
    
    ax = fig2.add_subplot(111)
    plt.plot(Time,w[1,:],'--')
    plt.plot(Time,w[2,:],'--')
    plt.plot(Time,w[3,:],'--')
    plt.plot(Time,w[1,:]+w[2,:]+w[3,:],'-')
    plt.xlabel('Time (d)')
    plt.ylabel('concentration (mmol/m^2)')
    plt.title('Total system')
    ax.legend(('Nutrients','phytoplankton','herbivore','Total Nitrogietn in the system'))
    return;
    
def change_plot(w,Time):
    from DiffEquation import f,alpha
    
    dw=f(Time[0],w[:,[0]])
    
    a=np.array([alpha(Time[0],w[:,[0]])])
    
    for i in range(1, len(Time)):
        
        ndw=f(Time[i],w[:,[i]])
        
        na=alpha(Time[i],w[:,[i]])
        
        dw=np.append(dw,ndw,axis=1)
        a=np.append(a,na)
        
    fig2 = plt.figure()
    ax = fig2.add_subplot(111)
    plt.plot(Time,dw[1,:],'--')
    plt.plot(Time,dw[2,:],'--')
    plt.plot(Time,dw[3,:],'--')
    plt.plot(Time,dw[1,:]+dw[2,:]+dw[3,:],'-')
    plt.xlabel('Time (d)')
    plt.ylabel('concentration (mmol m^-2s^-1)')
    plt.title('d/dt Total system')
    ax.legend(('d/dt Nutrients','d/dt phytoplankton','d/dt herbivore','d/dt Total Nitrogietn in the system'))
    
    fig3 = plt.figure()
    ax = fig3.add_subplot(111)
    plt.xlabel('Time (d)')
    plt.plot(Time,a,'-')
    plt.ylabel('growfactor alpha ')
    plt.title('alpha')
    
        
    
    


  