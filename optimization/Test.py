# -*- coding: utf-8 -*-
from Problem import Problem
from Line import *
from scipy import *
from scipy import linalg
#from Main import plot
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
        for i in range(50):
            re.append(x)
            g=self.problem.grad(x)
            G = self.calcG(self.problem,x)
            
            try:
                L = linalg.cholesky(G, lower=True)     
            except LinAlgError:
                print("linalgerror")
            ch = linalg.cho_factor(G,L)
            s=-linalg.cho_solve(ch,g)
            
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
    
x0 = matrix([0.,-0.1]).transpose()
p=Problem(f)
#a=ExactLine()
print("test.py")
qn = Newton(p)
result = qn.solve(x0,2**(-20))
print(result[-1])
#plot(f,result)