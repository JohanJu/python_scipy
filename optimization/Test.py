# -*- coding: utf-8 -*-
from Problem import Problem
from scipy import *
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
            h = nextH(problem,x)
#            print("h",h)
#            print("g",g)
            s=-h*self.problem.grad(x)
            s=s/sum(abs(s))
            if(sum(abs(g)) < tolerance):
                return re
            if (a is not None):
                a = self.a(self.problem(),x,s)
#            if(a < 0.000001):
#                return re
#               a = 0.01
            else:
                a = 1
            xn = x+(a*s)
        return re
    
    def nextH(self,p,x):
        x = squeeze(asarray(x));
        n = len(x)
        h = matrix(zeros([n,n]))
        g1  = p.grad(x).transpose();
        for i in range(n):   
            print("g1",g1)
            eps = max(1,abs(x[i]))*(2**(-20))
            x[i] += eps
            g2 = p.grad(x).transpose();
            print("g2",g2)
            x[i] -= eps
            h[i] = (g2-g1)/eps
            
        return 0.5*(h+h.transpose())
    
x = matrix([111.,111.]).transpose()
p=Problem(f)
new = Newton(p)
res = new.nextH(p,x)
print(res)  