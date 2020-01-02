# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:49:03 2019

@author: joost
"""
import numpy as np

def unit(value,size,index):
        '''returns basis vector e_index with dimension size times value'''
        if index < 0:
            index = size + index # so if index = -1, the function will put value at the last index
        return value*np.eye(1,size,index).reshape(size)
    
def diagMatrix(n,L,M,R):
        '''makes square (nxn) matrix with
            L on the left off diagonal
            M on the diagonal
            R on the right off diagonal
    
            useful for discretization of first and second spatial derivative
        '''
        mat = M*np.identity(n) #diagonal
    
        leftOff = L*np.ones(n-1) #left off-diagonal
        np.fill_diagonal(mat[1:], leftOff)
    
        rightOff = R*np.ones(n-1) #right off-diagonal
        np.fill_diagonal(mat[:,1:],rightOff)
        return mat
    
class derivatives:
    BC_type = "P"
    
    def secondDerivative(y,dx,boundary = (0,0)):
        '''computes second derivative numerically
        y(x): vector
        dx: spatial step size
        boundary [tuple]: (Lbound,Rbound) if Dirichelet boundaries, default is (0,0)
        '''
        n = len(y)
        mat = diagMatrix(n,1,-2,1)
            
        BC = derivatives.BC_type
        if BC == "D":
            Lb,Rb = boundary #boundary is forced to be a certain (inputted) value
            return 1/dx**2*(mat.dot(y) + unit(Lb,n,0) + unit(Rb,n,-1)) #second derivative with Dirichelet BC
        
        elif BC == "N":
            raise NotImplementedError
            return 
        
        elif BC == "P":
            Lb,Rb = y[-1],y[0] #left boundary is the value of the right end, and the right boundary is the value of the left end
            return 1/dx**2*(mat.dot(y) + unit(Lb,n,0) + unit(Rb,n,-1)) #second derivative with periodic BC
    
    def firstDerivative(y,dx, boundary = (0,0)):
        '''computes second derivative numerically
        y(x): vector
        dx: spatial step size
        BC: boundary type Dirichelet (D), Neumann (N) or Periodic (P)
        boundary [tuple]: (Lbound,Rbound) if Dirichelet boundaries, default is (0,0)
        '''
        n = len(y)
        mat = diagMatrix(n,-1,0,1)
            
        BC = derivatives.BC_type
        if BC == "D":
            Lb,Rb = boundary
            return 1/(2*dx)*(mat.dot(y) - unit(Lb,n,0) + unit(Rb,n,-1)) #first derivative with Dirichelet BC
            
        elif BC == "N":
            raise NotImplementedError
            return None
            
        elif BC == "P":
            Lb,Rb = y[-1],y[0] #left boundary is the value of the right end, and the right boundary is the value of the left end
            return 1/(2*dx)*(mat.dot(y) - unit(Lb,n,0) + unit(Rb,n,-1)) #first derivative with periodic BC