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

plt.close("all")


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
    
def Layerdept_plot(w,Time):
    
    fig2 = plt.figure()
    
    ax = fig2.add_subplot(111)
    
    plt.plot(Time,w[0,0,:],'--')
    plt.xlabel('Time (d)')
    plt.ylabel('dept (m)')
    plt.title('mixed layer dept')
    ax.legend('Mixed layer dept')
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
    
    from classes.classTransfer import transfer as t
    
    x=50
    
    a=np.array([t.alpha(Time[0],w[x,0,[0]],w[x,2,[0]])])
    
    for i in range(1, len(Time)):
        
        
        na=t.alpha(Time[i],w[x,0,[i]],w[x,2,[i]])
        
    
        a=np.append(a,na)
        
    fig3 = plt.figure()
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
    #plt.plot(range(nX),sum([W[:,i,tn] for i in [1,2,3]]),'--')
    plt.xlabel('x (m)')
    plt.ylabel('Concentration (mmol m$^{-2}$s$^{-1}$)')
    plt.title('x-dependency ')#at time $t_{'+str(tn)+'}$')
    ax.legend(('Nutrients(x)','Phytoplankton(x)','Herbivore(x)'))#,'Total Nitrogen in the system(x)'))

def XslicePlot(W,Time, xn):
    '''slice plot at xn over all t'''
    nX, nDim, nT = W.shape
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    # Temporal plot at x = xn
    plt.plot(Time,W[xn,1,:],'-') #Nutrients
    plt.plot(Time,W[xn,2,:],'-') #Phytoplankton
    plt.plot(Time,W[xn,3,:],'-') #Herbivore
    #plt.plot(Time,sum([W[xn,i,:] for i in [1,2,3]]),'--')
    plt.xlabel('Time (d)')
    plt.ylabel('Concentration (mmol m$^{-2}$s$^{-1}$)')
    plt.title('t-dependency')# at position $x_{'+str(xn)+'}$')
    ax.legend(('Nutrients(x)','Phytoplankton(x)','Herbivore(x)'))#,'Total Nitrogen in the system(x)'))
    
def colorplot(W,Time):
    '''Plots all quantities for on whole (X x T) domain using a colorplot'''
    nX, nDim, nT = W.shape
    
    #Depth
    fig = plt.figure()
    #fig.add_subplot(221)
    #plt.imshow(W[:,0,:].reshape((nX,len(W[:,1,:][1])),order='F'),aspect='auto' )
    #plt.xlabel('Time (d)')
    #plt.ylabel('x (m)')
    #plt.title('Depth')
    #plt.colorbar()

    #Nutrietns
    fig.add_subplot(311)
    plt.imshow(W[:,1,:].reshape((nX,len(W[:,1,:][1])),order='F'),aspect='auto')    
    plt.xlabel('Time (steps)')
    plt.ylabel('x (m)')
    plt.title('Nutrients')
    plt.colorbar()

    #Phytoplankton
    fig.add_subplot(312)
    plt.imshow(W[:,2,:].reshape((nX,len(W[:,1,:][1])),order='F'),aspect='auto')
    plt.xlabel('Time (d)')
    plt.ylabel('x (m)')
    plt.title('Phytoplankton')
    plt.colorbar()
    
    #Herbivores
    fig.add_subplot(313)
    plt.imshow(W[:,3,:].reshape((nX,len(W[:,1,:][1])),order='F'),aspect='auto')
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
    return slider
    

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
    lN, = ax.plot(Time,N)
    lP, = ax.plot(Time,P)
    lH, = ax.plot(Time,H)
    lT, = ax.plot(Time,N+P+H,'--')
    
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
    
        xdata=Time
        lN.set_data(xdata,N)
        lP.set_data(xdata,P)
        lH.set_data(xdata,H)
        lT.set_data(xdata,N+P+H)
        fig.canvas.draw()
    
    slider.on_changed(update)
    return slider
      


def Tanimation(W,Time):
    '''An animation that slices T'''
    import matplotlib.animation as animation
    fig, ax = plt.subplots()
    fig.set_tight_layout(True)
    
    nX, nDim, nT = W.shape
    
    # select first image
    N = W[:,1,0].squeeze()
    P = W[:,2,0].squeeze()
    H = W[:,3,0].squeeze()
    
    # display image
    xdata=range(nX)
    lN, = ax.plot(xdata,N)
    lP, = ax.plot(xdata,P)
    lH, = ax.plot(xdata,H)
    lT, = ax.plot(xdata,N+P+H,'--')
    
    plt.xlabel('x (m)')
    plt.ylabel('Concentration (mmol m$^{-2}$s$^{-1}$)')
    plt.title('x-dependency at varing time ')
    plt.legend(('Nutrients(x)','Phytoplankton(x)','Herbivore(x)','Total Nitrogen in the system(x)'))
    
    def update(i):
        
        # Update the line and the axes (with a new xlabel). Return a tuple of
        # "artists" that have to be redrawn for this frame.
        #ydata
        N = W[:,1,i].squeeze()
        P = W[:,2,i].squeeze()
        H = W[:,3,i].squeeze()
    
        xdata=range(nX)
        lN.set_data(xdata,N)
        lP.set_data(xdata,P)
        lH.set_data(xdata,H)
        lT.set_data(xdata,N+P+H)
        
        label = 'Time {0}'.format(i)
        ax.set_xlabel(label)
        
        return lN,lP,lH,lT

    anim = animation.FuncAnimation(fig, update, frames=np.arange(0, nT), interval=4)

    FFwriter=animation.FFMpegWriter(fps=30, extra_args=['-vcodec', 'libx264'])
    anim.save('Tanimation.mp4', writer=FFwriter)
    plt.show()
    
def Xanimation(W,Time):
    '''An animation that slices X'''
    import matplotlib.animation as animation
    fig, ax = plt.subplots()
    fig.set_tight_layout(True)
    
    nX, nDim, nT = W.shape
    

    # select first image
    N = W[0,1,:].squeeze()
    P = W[0,2,:].squeeze()
    H = W[0,3,:].squeeze()
    
    # display image
    xdata=Time
    lN, = ax.plot(xdata,N)
    lP, = ax.plot(xdata,P)
    lH, = ax.plot(xdata,H)
    #lT, = ax.plot(N+P+H,'--')
    
    
    plt.xlabel('Time (d)')
    plt.ylabel('Concentration (mmol m$^{-2}$s$^{-1}$)')
    plt.title('t-dependency at varing position ')
    ax.legend(('Nutrients(x)','Phytoplankton(x)','Herbivore(x)','Total Nitrogen in the system(x)'))
    
    def update(i):
        
        # Update the line and the axes (with a new xlabel). Return a tuple of
        # "artists" that have to be redrawn for this frame.
        #ydata
        N = W[i,1,:].squeeze()
        P = W[i,2,:].squeeze()
        H = W[i,3,:].squeeze()
    
        xdata=Time
        lN.set_data(xdata,N)
        lP.set_data(xdata,P)
        lH.set_data(xdata,H)
        #lT.set_data(xdata,N+P+H)
        
        label = 'X {0}'.format(i)
        ax.set_xlabel(label)
        return lN,lP,lH#,lT
    
    # Set up formatting for the movie files
    FFwriter=animation.FFMpegWriter(fps=30, extra_args=['-vcodec', 'libx264'])
    anim = animation.FuncAnimation(fig, update, frames=np.arange(0, nX), interval=150)
    anim.save('Xanimation.mp4', writer=FFwriter)


    