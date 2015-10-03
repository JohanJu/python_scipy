# -*- coding: utf-8 -*-
from scipy import *
from scipy import optimize as op

class InExactLine():
    def __init__(self,p,s,t,x):
        self.p=p
        self.s=s
        self.t=t
        self.x=x
        
    def __call__(self,f,x,s):
        a = 0
        return a


class ExactLine():
    def __call__(self,f,x,s):
        def mf(a):
            return(f(x+a*s))       
        return op.minimize(mf,0).x