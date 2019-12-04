# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:49:03 2019

@author: joost
"""
import numpy as np

def diagMatrix(n,L,M,R):
    '''makes square (nxn) matrix with
        L on the left off diagonal
        M on the diagonal
        R on the right off diagonal

        useful for discretization of first and second spatial derivative
    '''
    mat = M*np.identity(n) #diagonal

    rightOff = R*np.ones(n-1) #right off-diagonal
    np.fill_diagonal(mat[1:], rightOff)

    leftOff = L*np.ones(n-1) #left off-diagonal
    np.fill_diagonal(mat[:,1:],leftOff)
    return mat

def secondDerivative(t,y,dx):
    '''computes second derivative numerically
    t: time vector
    y(x): vector
    dx: spatial step size
    '''
    n = len(y)
    mat = diagMatrix(n,1,-2,1)
    return 1/dx**2*mat.dot(w)

def firstDerivative(t,w,n,dx):
    mat = diagMatrix(n,-1,0,1)
    return 1/(2*dx)*mat.dot(w)