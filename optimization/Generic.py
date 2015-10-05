# -*- coding: utf-8 -*-
from scipy import *
                                                #hur äe denna generisk? 
class QuasiNewton(object):
    def __init__(self,problem,a):
        self.problem = problem
        self.a = a
        
    def slove(self,x,tolerance):
        error = 1000;
        h = eye(len(x))
        while(error>tolerance):
            s=-dot(h,self.problem.grad(x))
            xn = x+self.a(self.problem(),x,s)*s     #xn = x + a*s ? 
            p = self.problem()
            error = abs(p(xn)-p(x))
            delta = xn-x
            gamma = self.problem.grad(xn)-self.problem.grad(x)
            x = xn
            h=self.H(h,delta,gamma)
        return x
        
        @abstractmethod
        def nextH(self,h,delta,gamma):
            pass