# -*- coding: utf-8 -*-
from scipy import *
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
    
        return re
    
    @abc.abstractmethod
    def nextH(self,H,delta,gamma):
        return