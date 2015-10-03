# -*- coding: utf-8 -*-
from scipy import *
class QuasiNewton:
    def __init__(self,problem,H,a):
        self.problem = problem
        self.H = H
        self.a = a
        
    def slove(self,x,tolerance):
        error = 1000;
        h = eye(len(x))
        while(error>tolerance):
            s=-dot(h,self.problem.grad(x))
            xn = x+self.a(self.problem(),x,s)*x
            p = self.problem()
            error = abs(p(xn)-p(x))
            delta = xn-x
            gamma = self.problem.grad(xn)-self.problem.grad(x)
            x = xn
            h=self.H(h,delta,gamma)
        return x