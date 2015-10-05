# -*- coding: utf-8 -*-
from scipy import *
import sys                                           #hur äe denna generisk? 
class QuasiNewton():
    def __init__(self,problem,a):
        self.problem = problem
        self.a = a
        
    def solve(self,x,tolerance):
        print("3")
        sys.stdout.flush()
        error = 1000;
        h = eye(len(x))
        print(h)
        sys.stdout.flush()
        while(error>tolerance):
            print("1")
            sys.stdout.flush()
            s=-dot(h,self.problem.grad(x))
            xn = x+self.a(self.problem(),x,s)*s     #xn = x + a*s ? 
            p = self.problem()
            error = abs(p.func(xn)-p.func(x))
            delta = xn-x
            gamma = self.problem.grad(xn)-self.problem.grad(x)
            x = xn
            h=self.nextH(h,delta,gamma)
            print(h)
            sys.stdout.flush()
        return x
        
    def nextH(self,H,delta,gamma):
        print("2")
        sys.stdout.flush()
        deltaTranspose = delta.transpose()
        gammaTranspose = gamma.transpose()
        HTimesGamma = H*gamma
        term1 = (delta*deltaTranspose)/(deltaTranspose*gamma)
        term2 = (HTimesGamma*gammaTranspose*H)/(gammaTranspose*HTimesGamma)
        return H + term1 - term2