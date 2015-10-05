# -*- coding: utf-8 -*-
from scipy import *
class Problem():
    
    def __init__(self,f,g=None):
        self.f=f
        self.g=g
    
    def __call__(self):
        return self
        
    def func(self,x):
        return self.f(x)
        
    def grad(self,x):
        if(self.g is not None):
            return self.g(x)
        else:
            eps = 2**(-30)
            g = zeros(len(x))
            for i in range(len(x)):
                x[i] += eps
                t = self.f(x)
                x[i] -= eps
                g[i] = (t-self.f(x))/eps;
            return g

