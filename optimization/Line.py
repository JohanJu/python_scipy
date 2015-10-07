# -*- coding: utf-8 -*-
from scipy import *
from scipy import optimize as op


class InExactLine():
   
    def __init__(self, p = 0.1, s = 0.7, t = 0.1, x = 9.):        
        self.p = p
        self.s=s
        self.t=t
        self.x=x
  
    def __call__(self,p,x,s):
        self.aL = 0.
        self.aU = 10.**99
        self.a0 = 0.1
        
        self.fOfaL = p.func(x+self.aL*s)
        self.fOfa0 = p.func(x+self.a0*s)
        self.derivOfaL = self.der(p,self.aL,x,s)
        self.derivOfa0 = self.der(p,self.a0,x,s)
        

        while not (self.LC() and self.RC()):
            if not self.LC():
                self.a0,self.aL = self.block1()
            else:
                self.a0,self.aU = self.block2()
            
            self.fOfaL = p.func(x+self.aL*s)
            self.fOfa0 = p.func(x+self.a0*s)
            self.derivOfaL = self.der(p,self.aL,x,s)
            self.derivOfa0 = self.der(p,self.a0,x,s)
            
        return self.a0
        
    def der(self,p,a,x,s):
        eps = 2**(-30)
        return (p.func(x+(a+eps)*s)-p.func(x+a*s))/eps
        
    def block1(self):
        deltaA0 = self.extrapolation()
        deltaA0 = max(deltaA0, (self.t*(self.a0-self.aL)) )
        deltaA0 = min(deltaA0, (self.x*(self.a0-self.aL)) )
        aL = self.a0
        a0 = self.a0 + deltaA0
        return a0,aL
        
    def extrapolation(self):
        return (self.a0-self.aL)*self.derivOfa0/(self.derivOfaL-self.derivOfa0)
    
    def block2(self):
        aU = min(self.a0,self.aU)
        tempA0 = self.interpolation()
        tempA0 = max(tempA0, (self.aL+self.t*(aU-self.aL)) )
        tempA0 = min(tempA0, (aU-self.t*(aU-self.aL)) )
        a0 = tempA0
        return a0,aU
    
    def interpolation(self):
        return ((self.a0-self.aL)**2*self.derivOfaL)/(2*(self.fOfaL-self.fOfa0+(self.a0-self.aL)*self.derivOfaL))
    
    '''
    Gör någon lösning på vilka conditions som ska användas
    OBS RC samma för båda conditions
    '''

    #Goldstein conditions
    def LC(self):
        return self.fOfa0 >= (self.fOfaL + (1-self.p)*(self.a0-self.aL)*self.derivOfaL)
    def RC(self):
        return self.fOfa0 <= (self.fOfaL + self.p*(self.a0-self.aL)*self.derivOfaL)
    
    #Wolfe-Powell conditions
    def LC1(self):
        return self.derivOfa0 >= (self.s*self.derivOfaL)
    def RC1(self):
        return self.fOfa0 <= (self.fOfaL + self.p*(self.a0-self.aL)*self.derivOfaL)
    

class ExactLine():
    def __call__(self,p,x,s):
        x = squeeze(asarray(x))
        s = squeeze(asarray(s))
        def mf(a):
            return(p.func(x+a*s))       
        return op.minimize(mf,0).x[0]