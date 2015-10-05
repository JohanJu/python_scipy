# -*- coding: utf-8 -*-
from scipy import *
from H import DFPRank2Update
from Line import ExactLine
from Problem import Problem

def f(x):
    return sum([i ** 2 for i in x])

#print(Problem(f).grad(array([1.,1])))

#qn = QuasiNewton(Problem(f),BadBroyden(),ExactLine())
#print(qn.slove(array([1.,1]),0.01))

p=Problem(f)
#e=InExactLine(0.1,0.7,0.1,9.)
a=ExactLine()
res = a(p,array([1.,1]),array([2.,2]))
print(res)
#qn = DFPRank2Update(p,a)

    




