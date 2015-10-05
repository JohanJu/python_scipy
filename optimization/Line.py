# -*- coding: utf-8 -*-
from scipy import *
from scipy import optimize as op

class InExactLine():
    def __init__(self,p,s,t,x):
        self.p=p
        self.s=s
        self.t=t
        self.x=x
    
    #använder ej s
    def __call__(self,f,x,s):
        '''
        fOfaL = f(a_L)
        fOfa0 = f(a_0)
        gradOfaL = f'(a_L)
        gradOfa0 = f'(a_0)
        
        '''
        aL = 0
        aU = 10**99
        a0 = 0
        
        fOfaL = f(x+aL*s)
        fOfa0 = f(x+a0*s)
        gradOfaL = f.grad(x+aL*s)
        gradOfa0 = f.grad(x+a0*s)
        
        
        while not (LC(a0,aL,fOfa0,fOfaL,gradOfaL) and RC(a0,aL,fOfa0,fOfaL,gradOfaL)):
            if not LC(a0,aL,fOfa0,fOfaL,gradOfaL):
                a0,aL = block1(a0,aL,gradOfa0,gradOfaL)
            else:
                a0,aU = block2(a0,aU,aL,gradOfaL,fOfaL,fOfa0)
            
            fOfaL = f(x+aL*s)
            fOfa0 = f(x+a0*s)
            gradOfaL = f.grad(x+aL*s)
            gradOfa0 = f.grad(x+a0*s)
            
        return a0, fOfa0
        
    def block1(a0,aL,gradOfa0,gradOfaL):
        deltaA0 = extrapolation(f,a0,aL,gradOfa0,gradOfaL)
        deltaA0 = max(deltaA0,self.t*(a0-aL))
        deltaA0 = min(deltaA0,self.x*(a0-aL))
        aL = a0
        a0 = a0 + deltaA0
        return a0,aL
        
    def extrapolation(f,a0,aL,gradOfa0,gradOfaL):
        return (a0-aL)*gradOfa0/(gradOfaL-gradOfa0)
    
    def block2(a0,aU,aL,gradOfaL,fOfaL,fOfa0):
        aU = min(a0,aU)
        a0 = interpolation(a0,aL,gradOfaL,fOfaL,fOfa0)
        a0 = max(a0,aL+self.t*(aU-aL))
        a0 = min(a0, aU-self.t*(aU-aL))
        a0 = a0                               #ta bort, har här ingen betydelse om det är ã eller a
        return a0,aU
    
    def interpolation(a0,aL,gradOfaL,fOfaL,fOfa0):
        return ((a0-aL)**2*gradOfaL)/(2*(fOfaL-fOfa0+(a0-aL)*gradOfaL))
    
    '''
    Gör någon lösning på vilka conditions som ska användas
    '''

    #Goldstein conditions
    def LC(a0,aL,fOfa0,fOfaL,gradOfaL):
        return fOfa0 >= fOfaL + (1-self.p)*(a0-aL)*gradOfaL
    def RC(a0,aL,fOfa0,fOfaL,gradOfaL):
        return fOfa0 <= fOfaL + self.p*(a0-aL)*gradOfaL
    
    #Wolfe-Powell conditions
    def LCWP(gradOfa0, gradOfaL):
        return gradOfa0 >= self.s*gradofaL
    def RCWP(a0, aL, fOfaL, gradOfa0, gradOfaL):
        return gradOfa0 <= (fOfaL + self.p*(a0-aL)*gradOfaL)
    

class ExactLine():
    def __call__(self,p,x,s):
        def mf(a):
            return(p.func(x+a*s))       
        return op.minimize(mf,0).x