# -*- coding: utf-8 -*-
from scipy import *
from pylab import *
rcParams['figure.figsize'] = 8, 6
"""
Task 3 
"""
class Spline():
#    ui = []
    def __call__(self):
        print("call")
    def __init__(self,ui):
        self.ui=array(ui)
        self.dx=array(zeros(ui.size))
        self.dy=array(zeros(ui.size))
        self.dx[3]=2;
        self.dy[3]=3;
        self.dx[4]=4;
        self.dy[4]=3;
        self.dx[5]=4;
        self.dy[5]=1;
#        print(self)
        
    def plot(self,cp,db):
        x = array(zeros(1000))
        y = array(zeros(1000))
        for i in range(self.ui.size-3):
            xp = []
            yp = []
            b = self.basisFunction3(i, array([0.,1,2,3,4,5,6,7,8,9,10]))
            ls = linspace(self.ui[0], self.ui[-1],1000)
            for k in ls:
               xp.append(self.dx[i]*b(k))
               yp.append(self.dy[i]*b(k)) 
            x+=array(xp)
            y+=array(yp)
             
        plot(x,y)
       
                
            
        if(db):
            plot(self.dx,self.dy,'o')
        if(cp):
            plot(self.dx,self.dy,'--')
        xlim(-.5, 5.5)
        ylim(-.5, 5.5)          
        
#    def plotPart(self,f,i):
#        x = []
#        y = []
#        ls = linspace(self.ui[i], self.ui[i+1])
#        print(self.ui[i])
#        print(self.ui[i+1])
#        for k in ls:
#            x.append(self.dx[i]*f(k))
#            y.append(self.dy[i]*f(k)) 
#        plot(x,y)
    
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
        
mui= array([0.,1,2,3,4,5,6,7,8,9,10])
s=Spline(mui)
basisF = s.basisFunction(2, array([0.,1,2,3,4,5,6,7,8,9,10]),3)
print(basisF(4))
basisF3 = s.basisFunction3(3, array([0.,1,2,3,4,5,6,7,8,9,10]))
print(basisF3(4))
 
#s.plotFunction(basisF,0,9)
#s.plotFunction(basisF3,0,9)
 
s.plot(1,1)
