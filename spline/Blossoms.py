# -*- coding: utf-8 -*-
from scipy import *
from pylab import *
rcParams['figure.figsize'] = 8, 6
"""
Task 3 
"""
class Spline():
#    ui = []
    def __call__(self,u):
        I = (self.ui>=u).argmax()-1
        return self.d[I-2]*self.baseList[I-2](u)+self.d[I-1]*self.baseList[I-1](u)+self.d[I]*self.baseList[I](u)+self.d[I+1]*self.baseList[I+1](u)
   
    def __init__(self,ui,d):
        self.ui=array(ui)
        self.d=d
        self.initArr()
        
    def initArr(self):
        # y is a vector which contais s(x)
        self.y = array(zeros(100))
        self.x = linspace(self.ui[0], self.ui[-1],100)
        self.baseList = []
        for i in range(self.ui.size-3):
            yp = []
            self.baseList.append(self.basisFunction3(i, self.ui))
            for k in self.x:
               yp.append(self.d[i]*self.baseList[-1](k)) 
            self.y+=array(yp)
             
                
    def plot(self,deBoorPoints,controlPolygon):   
        plot(self.x,self.y)
        if(deBoorPoints):
            plot(self.ui+1,self.d,'o')
        if(controlPolygon):
            plot(self.ui+1,self.d,'--')

    
    def basisFunction3 (self,j,u):
        return self.basisFunction(j,u,3)

    def basisFunction (self,i, u, K):
        def function(x):
            if(K == 0):
                if(u[i-1] == u[i]):
                    return 0
                if( ( (x > u[i-1]) or (x == u[i-1]) ) and ( (x < u[i]) ) ):
                    return 1
                else:
                    return 0
            fac1 = (x-u[i-1])/(u[i+K-1]-u[i-1])
            func1 = self.basisFunction(i,u,K-1)
            fac2 = (u[i+K]-x)/(u[i+K]-u[i])
            func2 = self.basisFunction(i+1,u,K-1)
            return fac1*func1(x) + fac2*func2(x)
        return function

    def plotFunction(self,f, fromX, toX):
        x = []
        y = []
        ls = linspace(fromX, toX)
        for k in ls:
            x.append(k)
            y.append(f(k)) 
        plot(x,y)
        
ui= array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
d = array([0,0,0,1,4,6,8,0,10,8,4,2,2,0,0,0])
s=Spline(ui,d)
s.plot(0,1)


class BlossomSpline():
    
    def __call__(self,u):
        I = (self.ui>=u).argmax()-1
        
        d11 = self.alpha(u,self.ui[I+1],self.ui[I-2])*self.d[I-2]+(1-self.alpha(u,self.ui[I+1], self.ui[I-2]))*self.d[I-1]
        d12 = self.alpha(u, self.ui[I+2], self.ui[I-1])*self.d[I-1]+(1-self.alpha(u,self.ui[I+2], self.ui[I-1]))*self.d[I]
        d13 = self.alpha(u, self.ui[I+3], self.ui[I])*self.d[I]+(1-self.alpha(u,self.ui[I+3], self.ui[I]))*self.d[I+1]

        d21 = self.alpha(u, self.ui[I+1], self.ui[I-1])*d11+(1-self.alpha(u,self.ui[I+1], self.ui[I-1]))*d12
        d22 = self.alpha(u, self.ui[I+2], self.ui[I])*d12+(1-self.alpha(u,self.ui[I+2], self.ui[I]))*d13

        return self.alpha(u, self.ui[I+1], self.ui[I])*d21+(1-self.alpha(u,self.ui[I+1], self.ui[I]))*d22 
    def __init__(self,ui,d):
        self.ui=ui
        self.d=d
    def alpha(self,u, rm, lm):
        return (rm-u)/(rm-lm)
#        return (self.ui[rm)]-u)/(self.ui[rm)]-self.ui[lm)])
    def plot(self,start,end,nbr):
        lx = linspace(start,end,nbr)
        ly = []
        for i in lx:
            ly.append(self(i))
        plot(lx,ly,'o')
        
bs=BlossomSpline(ui,d)
bs.plot(2,13,30)

import unittest

