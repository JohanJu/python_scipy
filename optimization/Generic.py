# -*- coding: utf-8 -*-
from scipy import *
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
            sys.stdout.flush()
            s=-dot(h,self.problem.grad(x))
            print("s:")
            print(s)
            xn = x+self.a(self.problem(),x,s)*s     #xn = x + a*s ? 
            print("a:")
            print(self.a(self.problem(),x,s))
            print("xn:")
            print(xn)
            sys.stdout.flush()
            p = self.problem()
            error = abs(p.func(xn)-p.func(x))
            delta = xn-x
            if(sum(abs(delta)) < 0.0001):
                print("return")
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
        
    def nextH(self,H,delta,gamma):
#        print("delta, gamma:")
#        print(delta)
#        print(gamma)
        sys.stdout.flush()
    
        deltaTranspose = delta.transpose()
        gammaTranspose = gamma.transpose()
        HTimesGamma = H.dot(gamma)
                    
#        print("deltaT, gammaT, h*gamma:")                                
#        print(deltaTranspose)   
#        print(gammaTranspose)
#        print(HTimesGamma)
        sys.stdout.flush()
            
            
        term1 = (delta.dot(deltaTranspose))/(deltaTranspose.dot(gamma))
        term2 = (HTimesGamma.dot(gammaTranspose.dot(H)))/(gammaTranspose.dot(HTimesGamma))
        
#        print("term1, term2:")                                
#        print(term1)   
#        print(term2)
        sys.stdout.flush()
        
        return H + term1 - term2