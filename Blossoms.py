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
            if( ( (x > u[i-1]) or (x == u[i-1]) ) and ( (x < u[i]) ) ):
                return 1
            else:
                return 0
        fac1 = (x-u[i-1])/(u[i+K-1]-u[i-1])
        func1 = basisFunction(i,u,K-1)
        fac2 = (u[i+K]-x)/(u[i+K]-u[i])
        func2 = basisFunction(i+1,u,K-1)
        return fac1*func1(x) + fac2*func2(x)
    return function

def plotFunction(f, fromX, toX):
    x = []
    y = []
    ls = linspace(fromX, toX)
    for k in ls:
        x.append(k)
        y.append(f(k)) 
    plot(x,y)
    
    
basisF = basisFunction(2, array([0.,1,2,3,4,5,6,7,8,9,10]),3)
#print(basisF(4))
basisF3 = basisFunction3(3, array([0.,1,2,3,4,5,6,7,8,9,10]))
#print(basisF3(2))
 
plotFunction(basisF,0,9)
plotFunction(basisF3,0,9)

"""
annan version
"""

K = 10;
ui = list(range(K))
ui.append(-2)
ui.append(-1)
u = array(linspace(0,K-2,1000))
print(ui)

def N0(i,j):
    re = []
    for j in u:
        if(ui[i-1]<=j and j<ui[i]):
            re.append(1)
        else:
            re.append(0)
    return re

def Nk(k,i,u):
    if(k>1):
        ret=(u-ui[i-1])*Nk(k-1,i,u)/(ui[i+k-1]-ui[i-1])
        ret+=(ui[i+k]-u)*Nk(k-1,i+1,u)/(ui[i+k]-ui[i])
    else:
        ret=(u-ui[i-1])*N0(i,u)/(ui[i+k-1]-ui[i-1])
        ret+=(ui[i+k]-u)*N0(i+1,u)/(ui[i+k]-ui[i])
    return ret
    

plot(u,Nk(3,2,u))

y = array(zeros(1000))
for i in range(-2,K-1):
    y+=Nk(3,i,u)
    
plot(u,y)
