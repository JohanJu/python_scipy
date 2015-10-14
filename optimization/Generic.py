# -*- coding: utf-8 -*-
from scipy import *
from scipy import linalg
import time
import abc
import sys                                          
class QuasiNewton():
    def __init__(self,problem,a):
        self.problem = problem
        self.a = a
        
    def solve(self,x,tolerance):
        re = []
        h = matrix(eye(len(squeeze(asarray(x)))))
        for i in range(50):
            re.append(x)
            g=self.problem.grad(x)
#            print("h",h)
#            print("g",g)
            s=-h*self.problem.grad(x)
            s=s/sum(abs(s))
            if(sum(abs(g)) < tolerance):
                return re
            a = self.a(self.problem(),x,s)
            if(a < 0.000001):
               a = 0.01
            xn = x+(a*s)       
            p = self.problem()
            delta = xn-x
            gamma = self.problem.grad(xn)-self.problem.grad(x)
            x = xn           
            h=self.nextH(h,delta,gamma)
            #for comparision only
            h2 = linalg.inv(self.calcG(self.problem,x))
            print("h",h)
            print("h2",h2)
    
        return re
    
    @abc.abstractmethod
    def nextH(self,H,delta,gamma):
        return
        
    #for comparision only
    def calcG(self,p,x):
        x = squeeze(asarray(x));
        n = len(x)
        h = matrix(zeros([n,n]))
        g1  = p.grad(x).transpose();
        for i in range(n):   
#            print("g1",g1)
            eps = max(1,abs(x[i]))*(2**(-20))
            x[i] += eps
            g2 = p.grad(x).transpose();
#            print("g2",g2)
            x[i] -= eps
            h[i] = (g2-g1)/eps
        return 0.5*(h+h.transpose())