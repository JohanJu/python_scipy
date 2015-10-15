# -*- coding: utf-8 -*-
# @author: Caroline Brandberg, Johan Ju
from scipy import *
from H import *
from Generic import Newton
from Line import *
from Problem import Problem
from Plot import plot
import scipy.optimize as so
import chebyquad_problem_3x as ch

task = 1 # 0=Newton 1=QuasiNewton 2=chebyquad

def f(x):
    return sum([(i) ** 2 for i in x])
    
def r(x):
    return 100*(x[1]-x[0]**2)**2+(1-x[0])**2

if(task is 0):
    x0 = matrix([1.,1.]).transpose()
    p=Problem(f)
    a=ExactLine()
    qn = Newton(p)
#    qn = Newton(p,a)
    result = qn.solve(x0,2**(-4))
    print(result[-1])
    plot(f,result)

if(task is 1):
    x0 = matrix([0.,-0.1]).transpose()
    p=Problem(r)
    a=Goldstein()
    qn = GoodBroyden(p,a)
#    qn = BadBroyden(p,a)
#    qn = DFPRank2Update(p,a)
#    qn = BFGSRank2Update(p,a)
    result = qn.solve(x0,2**(-10))
    plot(r,result)
    print(result[-1])


if(task is 2):
    x=linspace(0,1,8)
    print("xx",x)
    xmin= so.fmin_bfgs(ch.chebyquad,x,ch.gradchebyquad)  # should converge after 18 iterations
    print("fmin",xmin)
    x0 = matrix(x).transpose()
    p=Problem(ch.chebyquad,ch.gradchebyquad)
#    a=ExactLine()
#    a=Goldstein()
    a=WolfePowell()
    qn = GoodBroyden(p,a)
    result = qn.solve(x0,2**(-10))
    ares = squeeze(asarray(result[-1]));
    print("gbxv",ares)
    print("gbfv",ch.chebyquad(ares))
    print("diff",ares-xmin)
    print("L1 diff",sum(abs(ares-xmin)))

#L1 4:  6.4161e-07
#L1 8:  0.0707
#L1 11: 1.3271

