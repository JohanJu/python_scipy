# -*- coding: utf-8 -*-
import pylab as py
py.rcParams['figure.figsize'] = 12, 12
from Problem import Problem
from Line import *
from scipy import *
from scipy import linalg
#from Main import plot

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

def r(x):
    return 100*(x[1]-x[0]**2)**2+(1-x[0])**2
    
def f(x):
    return sum([(i) ** 2 for i in x])

#print((x))
#print(p.grad(x))


class Newton():
    def __init__(self,problem,a=None):
        self.problem = problem
        self.a = a
       
    def solve(self,x,tolerance):
        re = []
        for i in range(10):
            re.append(x)
            print("x",x)
            g=self.problem.grad(x)
            G = self.calcG(self.problem,x)
            print("g",g)
            print("G",G)
#            try:
#                L = linalg.cholesky(G, lower=True)     
#            except Exception:
#                print("linalgerror")
#            ch = linalg.cho_factor(G,L)
#            s=-linalg.cho_solve(ch,g)
            s=-linalg.solve(G,g)
            print("s",s)
            print()
#            print("h",h)
            s=s/sum(abs(s))
            if(sum(abs(g)) < tolerance):
                return re
            if (self.a is not None):
                a = self.a(self.problem(),x,s)
#                if(a < 0.000001):
#                    a = 0.01
            else:
                a = 1
            x = x+(a*s)
        print("felllll")
        return re
    
    def calcG(self,p,x):
        x = squeeze(asarray(x));
        n = len(x)
        h = matrix(zeros([n,n]))
        g1  = p.grad(x).transpose();
        for i in range(n):   
#            print("g1",g1)
            eps = max(1,abs(x[i]))*(2**(-20))
            x[i] += eps
            g2 = p.grad(x).transpose();
#            print("g2",g2)
            x[i] -= eps
            h[i] = (g2-g1)/eps
        return 0.5*(h+h.transpose())
    
#x0 = matrix([1.,1.]).transpose()
x0 = matrix([0.1,0.1]).transpose()

p=Problem(r)
a=ExactLine()
print("test.py")
#qn = Newton(p)
qn = Newton(p,a)
result = qn.solve(x0,2**(-4))
print(result[-1])
plot(f,result)