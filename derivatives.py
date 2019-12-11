# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:49:03 2019

@author: joost
"""
import numpy as np

def unit(value,size,index):
    '''returns basis vector e_index with dimension size times value'''
    return value*np.eye(1,size,index).reshape(size)
    
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

def secondDerivative(y,dx,boundary = (0,0)):
    '''computes second derivative numerically
    y(x): vector
    dx: spatial step size
    boundary tuple: (Lbound,Rbound) dirichelet, default is (0,0)
    '''
    Lb,Rb = boundary
    
    n = len(y)
    mat = diagMatrix(n,1,-2,1)
    sd = 1/dx**2*(mat.dot(y) + unit(Lb,n,0) + unit(Rb,n,-1)) #np.eye(1,size,index)
    

    return sd

def firstDerivative(y,dx, boundary = (0,0)):
    '''computes second derivative numerically
    y(x): vector
    dx: spatial step size
    boundary tuple: (Lbound,Rbound) dirichelet, default is (0,0)
    '''
    Lb,Rb = boundary
    
    n = len(y)
    mat = diagMatrix(n,-1,0,1)
    fd = 1/(2*dx)*(mat.dot(y)+ unit(Lb,n,0) + unit(Rb,n,0)) #np.eye(1,size,index)
    return fd