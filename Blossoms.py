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
    def __init__(self,ui,dx,dy):
        self.ui=array(ui)
        self.dx=dx
        self.dy=dy
        self.initArr()
#        print(self.x)
        
    def initArr(self):
        self.x = array(zeros(100))
        self.y = array(zeros(100))
        for i in range(self.ui.size-3):
            xp = []
            yp = []
            b = self.basisFunction3(i, self.ui)
            ls = linspace(self.ui[0], self.ui[-1],100)
            for k in ls:
               xp.append(self.dx[i]*b(k))
               yp.append(self.dy[i]*b(k)) 
            self.x+=array(xp)
            self.y+=array(yp)
             
       
                
    def plot(self,db,cp):   
        l = linspace(self.ui[0],self.ui[-1],100)
        plot(l,self.y)
        if(db):
            plot(ui+1,self.dy,'o')
        if(cp):
            plot(ui+1,self.dy,'--')
#        xlim(-.5, 15.5)
#        ylim(-.5, 10.5)          
        
    def change(self,index,x,y):
        self.dx[index]=x
        self.dy[index]=y
    
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
        
mui= array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
dx = array([0,0,0,1,2,3,5,8,10,10,8,6,3,0,0,0])
dy = array([0,0,0,1,4,6,8,10,10,8,4,2,2,0,0,0])
s=Spline(mui,dx,dy)
#basisF = s.basisFunction(0, array([0.,1,2,3,4,5,6,7,8,9,10]),3)
#print(basisF(4))
#basisF3 = s.basisFunction3(3, array([0.,1,2,3,4,5,6,7,8,9,10]))
#print(basisF3(4))
 
#s.plotFunction(basisF,0,9)
#s.plotFunction(basisF3,0,9)
 
s.plot(1,1)
#s.dy[6]=6
#s.plot(1,1)