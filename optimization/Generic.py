# -*- coding: utf-8 -*-
from scipy import *
import time
import abc
import sys                                           #hur äe denna generisk? 
class QuasiNewton():
    def __init__(self,problem,a):
        self.problem = problem
        self.a = a
        
    def solve(self,x,tolerance):
#        print(len(squeeze(asarray(x))))
        re = []
        h = matrix(eye(len(squeeze(asarray(x)))))
#        print("h:",h)
        sys.stdout.flush()
        for i in range(50):
            re.append(x)
#            print("x:",x)
            g=self.problem.grad(x)
#            print("g:",g)
            s=-h*self.problem.grad(x)
            s=s/sum(abs(s))
#            print("s:",s)
            sys.stdout.flush()
            if(sum(abs(g)) < tolerance):
#                print("return1")
                return re
            a = self.a(self.problem(),x,s)
#            print("a:",a)
            sys.stdout.flush()
            xn = x+(a*s)     #xn = x + a*s ? 
            
            p = self.problem()
            delta = xn-x
            gamma = self.problem.grad(xn)-self.problem.grad(x)

            x = xn           
#            print(" h:")
#            print(h)
            sys.stdout.flush()
            
            h=self.nextH(h,delta,gamma)
#            print("next h:",h)
#            print()
#            print()
#            time.sleep(0.1)
        return re
    
    @abc.abstractmethod
    def nextH(self,H,delta,gamma):
        return