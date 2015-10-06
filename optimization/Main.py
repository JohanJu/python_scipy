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

x0 = matrix([0.5,0.5]).transpose()
s0 = matrix([804.,400.])
#print(5*x0)
p=Problem(r)
a=ExactLine()
#print(a(p,x0,s0))
qn = GoodBroyden(p,a)
#qn = DFPRank2Update(p,a)
#qn = BFGSRank2Update(p,a)

print("\n\n-xxx-\n",qn.solve(x0,2**(-10)),"\n-xxx-")

#g = matrix([1,2])
#gt = g.transpose()
#print(g)
#print((gt*g)/(g*gt))