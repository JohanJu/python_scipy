# -*- coding: utf-8 -*-
from scipy import *
import abc
import sys                                           #hur äe denna generisk? 
class QuasiNewton():
    def __init__(self,problem,a):
        self.problem = problem
        self.a = a
        
    def solve(self,x,tolerance):
        error = 1000;
        h = eye(len(x))
        print("h",h)
        sys.stdout.flush()
        while(error>tolerance):
            print("start")
            sys.stdout.flush()
            s=-dot(h,self.problem.grad(x))
            print("next")
            sys.stdout.flush()
            print("s:")
            print(s)
            sys.stdout.flush()
            if(sum(abs(s)) < 0.0001):
                print("return1")
                return x
            xn = x+self.a(self.problem(),x,s)*s     #xn = x + a*s ? 
            print("a:")
            print(self.a(self.problem(),x,s))
            sys.stdout.flush()
            print("xn:")
            print(xn)
            sys.stdout.flush()
            p = self.problem()
            error = abs(p.func(xn)-p.func(x))
            delta = xn-x
            if(sum(abs(delta)) < 0.0001):
                print("return2")
                return x
            gamma = self.problem.grad(xn)-self.problem.grad(x)

            x = xn           
#            print(" h:")
#            print(h)
            sys.stdout.flush()
            
            h=self.nextH(h,delta,gamma)
            print("next h:")
            print(h)
            sys.stdout.flush()
        return x
    
    @abc.abstractmethod
    def nextH(self,H,delta,gamma):
        return