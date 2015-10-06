# -*- coding: utf-8 -*-
from scipy import *
from H import *
#from Generic import QuasiNewton
from Line import *
from Problem import Problem

def f(x):
    x = squeeze(asarray(x))
    return sum([(i) ** 2 for i in x])
    
def r(x):
    x = squeeze(asarray(x))
    return 100*(x[1]-x[0]**2)**2+(1-x[0])**2
    

#print(Problem(f).grad(array([1.,1])))

#qn = QuasiNewton(Problem(f),BadBroyden(),ExactLine())
#print(qn.slove(array([1.,1]),0.01))

x0 = matrix([-1.,-1]).transpose()
s0 = matrix([804.,400.])
#print(5*x0)
p=Problem(r)
a=InExactLine()
#print(a(p,x0,s0))
qn = GoodBroyden(p,a)
print("res ",qn.solve(x0,2**(-1)))


#g = matrix([1,2])
#gt = g.transpose()
#print(g)
#print((gt*g)/(g*gt))