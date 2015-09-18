# -*- coding: utf-8 -*-
from scipy import *
from pylab import *

"""
Task 3 
"""

def basisFunction3 (j,u):
    return basisFunction(j,u,3)

def basisFunction (i, u, K):
    def function(x):
        if(K == 0):
            if(u[i-1] == u[i]):
                return 0
            if( ( (x > u[i-1]) or (x == u[i-1]) ) and (x < u[i]) ):
                return 1
            else:
                return 0
        fac1 = (x-u[i-1])/(u[i+K-1]-u[i-1])
        func1 = basisFunction(i,u,K-1)
        fac2 = (u[i+K]-x)/(u[i+K]-u[i])
        func2 = basisFunction(i+1,u,K-1)
        return fac1*func1(x) + fac2*func2(x)
    return function


basisF = basisFunction(3, array([2,3,4,5,6,7,8,9,10]),3)
print(basisF(4))
basisF3 = basisFunction3(3, array([2,3,4,5,6,7,8,9,10]))
print(basisF3(2))

