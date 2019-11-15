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
    plt.title('Total Nitrogien in the system')
    ax.legend(('Nutrients','phytoplankton','herbivore','Total Nitrogietn in the system'))

    

    return;


  