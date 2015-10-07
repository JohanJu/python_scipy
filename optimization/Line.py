# -*- coding: utf-8 -*-
from scipy import *
from scipy import optimize as op


class InExactLine():
   
    def __init__(self):
        self.p=0.4
        self.s=0.7
        self.t=0.1
        self.x=9.
    
    #använder ej s
    def __call__(self,p,x,s):
        '''
        fOfaL = f(a_L)
        fOfa0 = f(a_0)
        gradOfaL = f'(a_L)
        gradOfa0 = f'(a_0)
        
        '''
        aL = 0.
        aU = 10.**99
        a0 = 0.1
        
        fOfaL = p.func(x+aL*s)
        fOfa0 = p.func(x+a0*s)
        gradOfaL = self.der(p,aL,x,s)
        gradOfa0 = self.der(p,a0,x,s)
        
        
        while not (self.LC(a0,aL,fOfa0,fOfaL,gradOfaL,gradOfa0) and self.RC(a0,aL,fOfa0,fOfaL,gradOfaL,gradOfa0)):
            if not self.LC(a0,aL,fOfa0,fOfaL,gradOfaL,gradOfa0):
                a0,aL = self.block1(a0,aL,gradOfa0,gradOfaL)
            else:
                a0,aU = self.block2(a0,aU,aL,gradOfaL,fOfaL,fOfa0)
            
            fOfaL = p.func(x+aL*s)
            fOfa0 = p.func(x+a0*s)
            gradOfaL = self.der(p,aL,x,s)
            gradOfa0 = self.der(p,a0,x,s)
            
        return a0
        
    def der(self,p,a0,x,s):
        eps = 2**(-30)
        return (p.func(x+(a0+eps)*s)-p.func(x+a0*s))/eps
        
    def block1(self,a0,aL,gradOfa0,gradOfaL):
        deltaA0 = self.extrapolation(a0,aL,gradOfa0,gradOfaL)
        deltaA0 = max(deltaA0,self.t*(a0-aL))
        deltaA0 = min(deltaA0,self.x*(a0-aL))
        aL = a0
        a0 = a0 + deltaA0
        return a0,aL
        
    def extrapolation(self,a0,aL,gradOfa0,gradOfaL):
        return (a0-aL)*gradOfa0/(gradOfaL-gradOfa0)
    
    def block2(self,a0,aU,aL,gradOfaL,fOfaL,fOfa0):
        aU = min(a0,aU)
        a0 = self.interpolation(a0,aL,gradOfaL,fOfaL,fOfa0)
        a0 = max(a0,aL+self.t*(aU-aL))
        a0 = min(a0, aU-self.t*(aU-aL))
        a0 = a0                               #ta bort, har här ingen betydelse om det är ã eller a
        return a0,aU
    
    def interpolation(self,a0,aL,gradOfaL,fOfaL,fOfa0):
        return ((a0-aL)**2*gradOfaL)/(2*(fOfaL-fOfa0+(a0-aL)*gradOfaL))
    
    '''
    Gör någon lösning på vilka conditions som ska användas
    '''

    #Goldstein conditions
    def LC(self,a0,aL,fOfa0,fOfaL,gradOfaL,gradOfa0):
        return fOfa0 >= (fOfaL + (1-self.p)*(a0-aL)*gradOfaL)
    def RC(self,a0,aL,fOfa0,fOfaL,gradOfaL,gradOfa0):
        return fOfa0 <= (fOfaL + self.p*(a0-aL)*gradOfaL)
    
    #Wolfe-Powell conditions
    def LC1(self,a0,aL,fOfa0,fOfaL,gradOfaL,gradOfa0):
        return gradOfa0 >= self.s*gradOfaL
    def RC1(self,a0,aL,fOfa0,fOfaL,gradOfaL,gradOfa0):
        return gradOfa0 <= (fOfaL + self.p*(a0-aL)*gradOfaL)
    

class ExactLine():
    def __call__(self,p,x,s):
        x = squeeze(asarray(x))
        s = squeeze(asarray(s))
        def mf(a):
            return(p.func(x+a*s))       
        return op.minimize(mf,0).x[0]