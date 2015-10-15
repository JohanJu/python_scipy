# -*- coding: utf-8 -*-
from Problem import Problem
from Line import *
from scipy import *

#from Main import plot
def r(x):
    return 100*(x[1]-x[0]**2)**2+(1-x[0])**2
    
def f(x):
    return sum([(i) ** 2 for i in x])


x0 = matrix([1.,1.]).transpose()
p=Problem(f)
#a=ExactLine()
print("test.py")
qn = Newton(p)
result = qn.solve(x0,2**(-4))
print(result[-1])
#plot(f,result)