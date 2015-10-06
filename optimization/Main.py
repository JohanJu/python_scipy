# -*- coding: utf-8 -*-
import sys
from scipy import *
from H import *
#from Generic import QuasiNewton
from Line import *
from Problem import Problem

def f(x):
    return sum([(i) ** 2 for i in x])
    
def r(x):
    return 100*(x[1]-x[0]**2)**2+(1-x[0])**2

#print(Problem(f).grad(array([1.,1])))

#qn = QuasiNewton(Problem(f),BadBroyden(),ExactLine())
#print(qn.slove(array([1.,1]),0.01))

p=Problem(f)
#e=InExactLine(0.1,0.7,0.1,9.)
a=InExactLine()
#res = a(p,array([10.,10]),array([1.,1]))
#print(res)
qn = GoodBroyden(p,a)
#print("4")
#sys.stdout.flush()
#print(qn.solve(array([5.,-10]),0.1))
#sys.stdout.flush()
#print("test")
delta = matrix([1,2])
gamma = array([1,2])
#m = array([[1,3],[5,7]])
#print("m1",m.dot(m))
#mt = m.transpose()
#print("m2",m)
#print("mt",mt)
print("delta")
print(delta.transpose())
print(delta*delta.transpose())
print(delta.transpose()*delta)

print("gamma")
print(gamma.transpose())
print(gamma*gamma.transpose())
print(gamma.transpose()*gamma)

