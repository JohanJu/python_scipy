# -*- coding: utf-8 -*-
# @author: Caroline Brandberg, Johan Ju
from scipy import *
class Problem():
    
    def __init__(self,f,g=None):
        self.f=f
        self.g=g
    
    def __call__(self):
        return self
        
    def func(self,x):
        x = squeeze(asarray(x))
        return self.f(x)
        
    def grad(self,x):
        if(self.g is not None):
            x = squeeze(asarray(x))
            return matrix(self.g(x)).transpose()
        else:
            x = squeeze(asarray(x))
            eps = 2**(-30)
            g = zeros(len(x))
            for i in range(len(x)):
                eps = max(1,abs(x[i]))*(2**(-20))
                x[i] += eps
                t = self.f(x)
                x[i] -= eps
                g[i] = (t-self.f(x))/eps;
            return matrix(g).transpose()
