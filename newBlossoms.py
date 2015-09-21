# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from scipy import *
from pylab import *

class Spline():
    
    def __init__(self, ui, d):
        self.ui = ui
        self.d = d
        
    def __call__(self, u):
        I = self.hotInterval(u)
        return self.Blossom(u,I-1,self.d)
        
    def hotInterval(self, u):
        return (self.ui > u).argmax()
    
    def plot(self, controlPolygon, deBoorPoints):
        ls = linspace(2, 12, 100)
        x = []
        y = []
        for l in ls:
            x.append(l)
            y.append(self.__call__(l))
        plot(x,y,'black')
        
        if(controlPolygon):
            plot(self.ui+1,self.d,'--')
        if(deBoorPoints):
            plot(self.ui+1,self.d,'o')
    
        ylim(0,11)
    
    def Blossom(self, u, I, d):
        d11 = self.Alpha(u,ui[I+1],ui[I-2])*d[I-2]+(1-self.Alpha(u,ui[I+1], ui[I-2]))*d[I-1]
        d12 = self.Alpha(u, ui[I+2], ui[I-1])*d[I-1]+(1-self.Alpha(u,ui[I+2], ui[I-1]))*d[I]
        d13 = self.Alpha(u, ui[I+3], ui[I])*d[I]+(1-self.Alpha(u,ui[I+3], ui[I]))*d[I+1]
    
        d21 = self.Alpha(u, ui[I+1], ui[I-1])*d11+(1-self.Alpha(u,ui[I+1], ui[I-1]))*d12
        d22 = self.Alpha(u, ui[I+2], ui[I])*d12+(1-self.Alpha(u,ui[I+2], ui[I]))*d13
    
        return self.Alpha(u, ui[I+1], ui[I])*d21+(1-self.Alpha(u,ui[I+1], ui[I]))*d22 
    
    def Alpha(self, u, rightmostknot, leftmostknot):
        return (rightmostknot-u)/(rightmostknot-leftmostknot)
    
    def plotSplineWithBossom(self,fromX, toX, index):
        d = zeros(16)
        d[index] = 1
        ls = linspace(2, 12, 1000)
        x = []
        y = []
        for l in ls:
            x.append(l)
            I = self.hotInterval(l)
            y.append(self.Blossom(l,I-1,d))
        plot(x,y)

    # return s(u)
    def evaluateFromBasisFunction(self, u):
        sum = 0
        # -3 otherwise 'basisFunction' will go out of bound since it gets a value at i+K        
        for i in range(self.ui.size-3):
            basisF = self.basisFunction3(i,self.ui)
            sum += self.d[i]*basisF(u)
        return sum
        
    def plotFromBasisFunction(self):
        ls = linspace(self.ui[0], self.ui[-1], 100)
        x = []
        y = []
        for l in ls:
            x.append(l)
            y.append(self.evaluateFromBasisFunction(l))
        plot(x,y,'+')

    def plotSplineFromBasisFunction(self,f, fromX, toX):
        x = []
        y = []
        ls = linspace(fromX, toX,1000)
        for k in ls:
            x.append(k)
            y.append(f(k)) 
        plot(x,y)
        
    def basisFunction3 (self,j,u):
        return self.basisFunction(j,u,3)

    def basisFunction (self,i, u, K):
        def function(x):
            if(K == 0):
                if(u[i-1] == u[i]):
                    return 0
                if( ( (x > u[i-1]) or (x == u[i-1]) ) and ( x < u[i] ) ):
                    return 1
                else:
                    return 0
            fac1 = (x-u[i-1])/(u[i+K-1]-u[i-1])
            func1 = self.basisFunction(i,u,K-1)
            fac2 = (u[i+K]-x)/(u[i+K]-u[i])
            func2 = self.basisFunction(i+1,u,K-1)
            return fac1*func1(x) + fac2*func2(x)
        return function




ui= array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
d = array([0,0,0,1,2,3,5,8,10,10,8,6,3,0,0,0])
s = Spline(ui, d)

figure(1)
for i in range(1,13):
    f3 = s.basisFunction3(i,ui)
    s.plotSplineFromBasisFunction(f3,0,16)
    s.plotSplineWithBossom(1,13,i)

figure(2)
s.plot(1, 1)
s.plotFromBasisFunction()
print(s.__call__(5.))
