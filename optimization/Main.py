# -*- coding: utf-8 -*-
import pylab as py
py.rcParams['figure.figsize'] = 12, 12
from scipy import *
import scipy.optimize as so
from H import *
from Line import *
from Problem import Problem
import chebyquad_problem_3x as ch

def plot(f,result):
    n = 100
    x = linspace(-0.2,1.2,n)
    y = linspace(-0.2,1.2,n)
    X, Y = meshgrid(x, y)
    Z = zeros([n,n])
    for i in range(n):
        for j in range(n):
            Z[i,j] = r(array([X[i,j],Y[i,j]]))
    V = [0.03,0.11,0.2,0.5,1,4,10,20,40,80]
    #colors=['r','b','g','k']
    #V = [0.003,0.01,0.018,0.025]
    py.contour(X, Y, Z, V)
    x=[]
    y=[]
    for i in range(len(result)):
        x.append(result[i][0,0])
        y.append(result[i][1,0])
    py.plot(x,y,'k',linewidth=3)
    py.plot(x,y,'o',markersize=10,color='k')
    py.plot(x0[0,0],x0[1,0],'o',markersize=20,color='b')
    py.plot(result[-1][0,0],result[-1][1,0],'o',markersize=20,color='r')
    

def f(x):
    return sum([(i) ** 2 for i in x])
    
def r(x):
    return 100*(x[1]-x[0]**2)**2+(1-x[0])**2

x=linspace(0,1,4)
print("xx",x)
xmin= so.fmin_bfgs(ch.chebyquad,x,ch.gradchebyquad)  # should converge after 18 iterations
print("fmin",xmin)

#x0 = matrix(x).transpose()
#p=Problem(ch.chebyquad,ch.gradchebyquad)
#a=ExactLine()
#a=Goldstein()
#a=WolfePowell()
#qn = GoodBroyden(p,a)
#result = qn.solve(x0,2**(-10))
#ares = squeeze(asarray(result[-1]));
#print("gbxv",ares)
#print("gbfv",ch.chebyquad(ares))
#print("diff",ares-xmin)
#print("L1 diff",sum(abs(ares-xmin)))

#L1 4:  6.4161e-07
#L1 8:  0.0707
#L1 11: 1.3271


x0 = matrix([0.,-0.1]).transpose()
p=Problem(r)
a=Goldstein()
#qn = GoodBroyden(p,a)
#qn = BadBroyden(p,a)
#qn = DFPRank2Update(p,a)
qn = BFGSRank2Update(p,a)
result = qn.solve(x0,2**(-10))
plot(r,result)
print(result[-1])

