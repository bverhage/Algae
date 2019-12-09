# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:38:51 2019

@author: billy
"""
if __name__ == "__main__":
    print("\n\nThis is the Plots program.")
    print("To run the programm run Execution.py, but I will do that for you this time:")
    exec(open("Execution.py").read());
    
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


##------------- The plots -----------------
def test_plots(W,Time):
    '''plots all plots - Joost'''
    
    #plots of slices at specific t and x respectively
    tn,xn = 200, 1 #position of slices
    TslicePlot(W,Time, tn) #slice plot at tn over all x
    XslicePlot(W,Time, xn) #slice plot at xn over all t
    
    #2D (x,t) with color
    colorplot(W,Time)
    
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
    plt.title('Total system')
    ax.legend(('d/dt Nutrients','d/dt phytoplankton','d/dt herbivore','d/dt Total Nitrogietn in the system'))
    
    fig3 = plt.figure()
    ax = fig3.add_subplot(111)
    plt.xlabel('Time (d)')
    plt.plot(Time,a,'-')
    plt.ylabel('growfactor alpha ')
    plt.title('alpha')
    return;
    
def TslicePlot(W,Time, tn):
    '''slice plot at tn over all x'''
    nX, nDim, nT = W.shape
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    # Spatial plot at t = tn
    plt.plot(range(nX),W[:,1,tn],'-') #Nutrients #ERROR HERE
    plt.plot(range(nX),W[:,2,tn],'-') #Phytoplankton
    plt.plot(range(nX),W[:,3,tn],'-') #Herbivore
    plt.plot(range(nX),sum([W[:,i,tn] for i in [1,2,3]]),'--')
    plt.xlabel('x (m)')
    plt.ylabel('Concentration (mmol m$^{-2}$s$^{-1}$)')
    plt.title('x-dependency at time $t_{'+str(tn)+'}$')
    ax.legend(('Nutrients(x)','Phytoplankton(x)','Herbivore(x)','Total Nitrogen in the system(x)'))

def XslicePlot(W,Time, xn):
    '''slice plot at xn over all t'''
    nX, nDim, nT = W.shape
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    # Temporal plot at x = xn
    plt.plot(range(nT),W[xn,1,:],'-') #Nutrients
    plt.plot(range(nT),W[xn,2,:],'-') #Phytoplankton
    plt.plot(range(nT),W[xn,3,:],'-') #Herbivore
    plt.plot(range(nT),sum([W[xn,i,:] for i in [1,2,3]]),'--')
    plt.xlabel('Time (d)')
    plt.ylabel('Concentration (mmol m$^{-2}$s$^{-1}$)')
    plt.title('t-dependency at position $x_{'+str(xn)+'}$')
    ax.legend(('Nutrients(x)','Phytoplankton(x)','Herbivore(x)','Total Nitrogen in the system(x)'))
    
def colorplot(W,Time):
    '''Plots all quantities for on whole (X x T) domain using a colorplot'''
    nX, nDim, nT = W.shape
    
    #Depth
    fig = plt.figure()
    ax = fig.add_subplot(221)
    plt.imshow(W[:,0,:].reshape((nX,len(W[:,1,:][1])),order='F'))
    plt.xlabel('Time (d)')
    plt.ylabel('x (m)')
    plt.title('Depth')
    plt.colorbar()

    #Nutrietns
    ax = fig.add_subplot(222)
    plt.imshow(W[:,1,:].reshape((nX,len(W[:,1,:][1])),order='F'))    
    plt.xlabel('Time (d)')
    plt.ylabel('x (m)')
    plt.title('Nutrients')
    plt.colorbar()

    #Phytoplankton
    ax = fig.add_subplot(223)
    plt.imshow(W[:,2,:].reshape((nX,len(W[:,1,:][1])),order='F'))
    plt.xlabel('Time (d)')
    plt.ylabel('x (m)')
    plt.title('Phytoplankton')
    plt.colorbar()
    
    #Herbivores
    ax = fig.add_subplot(224)
    plt.imshow(W[:,3,:].reshape((nX,len(W[:,1,:][1])),order='F'))
    plt.xlabel('Time (d)')
    plt.ylabel('x (m)')
    plt.title('Herbivores')
    plt.colorbar()
    
def Tslider(W,Time):
    '''slice plot at varing t over all x using a slider '''
    nX, nDim, nT = W.shape
    # generate figure
    fig = plt.figure()
    ax = plt.subplot(111)
    fig.subplots_adjust(left=0.25, bottom=0.25)
    
    # select first image

    N = W[:,1,0].squeeze()
    P = W[:,2,0].squeeze()
    H = W[:,3,0].squeeze()
    
    
    # display image
    lN, = ax.plot(range(nX),N)
    lP, = ax.plot(range(nX),P)
    lH, = ax.plot(range(nX),H)
    
    plt.xlabel('x (m)')
    plt.ylabel('Concentration (mmol m$^{-2}$s$^{-1}$)')
    plt.title('x-dependency at varing time ')
    plt.legend(('Nutrients(x)','Phytoplankton(x)','Herbivore(x)','Total Nitrogen in the system(x)'))
    
    # define slider
    
    ax = fig.add_axes([0.25, 0.1, 0.65, 0.03])
    
    slider = Slider(ax, 'Time in steps', 0, nT - 1,valinit=0, valfmt='%i')
    
    def update(val):
        ind = int(slider.val)
        
        #ydata
        N = W[:,1,ind].squeeze()
        P = W[:,2,ind].squeeze()
        H = W[:,3,ind].squeeze()
    
        xdata=range(nX)
        lN.set_data(xdata,N)
        lP.set_data(xdata,P)
        lH.set_data(xdata,H)
        
        
        fig.canvas.draw()
    
    slider.on_changed(update)
    

def Xslider(W,Time):
    '''slice plot at varing x over all t using a slider '''
    nX, nDim, nT = W.shape

    # generate figure
    fig = plt.figure()
    ax = plt.subplot(111)
    fig.subplots_adjust(left=0.25, bottom=0.25)
    
    # select first image
    N = W[0,1,:].squeeze()
    P = W[0,2,:].squeeze()
    H = W[0,3,:].squeeze()
    
    
    # display image
    lN, = ax.plot(N)
    lP, = ax.plot(P)
    lH, = ax.plot(H)
    lT, = ax.plot(range(nT),N+P+H,'--')
    
    plt.xlabel('Time (d)')
    plt.ylabel('Concentration (mmol m$^{-2}$s$^{-1}$)')
    plt.title('t-dependency at varing position ')
    ax.legend(('Nutrients(x)','Phytoplankton(x)','Herbivore(x)','Total Nitrogen in the system(x)'))
    
    # define slider
    ax = fig.add_axes([0.25, 0.1, 0.65, 0.03])
    
    slider = Slider(ax, 'X position', 0, nX - 1,valinit=0, valfmt='%i')
    
    def update(val):
        ind = int(slider.val)
        
        #ydata
        N = W[ind,1,:].squeeze()
        P = W[ind,2,:].squeeze()
        H = W[ind,3,:].squeeze()
    
        xdata=range(nT)
        lN.set_data(xdata,N)
        lP.set_data(xdata,P)
        lH.set_data(xdata,H)
        lT.set_data(xdata,N+P+H)
        fig.canvas.draw()
    
    slider.on_changed(update)
      