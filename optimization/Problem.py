# -*- coding: utf-8 -*-
from scipy import *
class Problem():
    
    def __init__(self,f,g=None):
        self.f=f
        self.g=g
    
    def __call__(self):
        return self.f
        
    def grad(self,x):
        if(self.g is not None):
            return self.g(x)
        else:
            #Numerisk gradient
            return 0