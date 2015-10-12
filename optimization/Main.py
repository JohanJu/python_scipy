# -*- coding: utf-8 -*-
from pylab import *
rcParams['figure.figsize'] = 12, 12
from scipy import *
from H import *
from Line import *
from Problem import Problem

def f(x):
    x = squeeze(asarray(x))
    return sum([(i) ** 2 for i in x])
    
def r(x):
    x = squeeze(asarray(x))
    return 100*(x[1]-x[0]**2)**2+(1-x[0])**2


x0 = matrix([0.,-0.1]).transpose()
p=Problem(r)
a=ExactLine()
qn = GoodBroyden(p,a)
result = qn.solve(x0,2**(-10))



#qn = BadBroyden(p,a)
#qn = DFPRank2Update(p,a)
#qn = BFGSRank2Update(p,a)



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
contour(X, Y, Z, V)
x=[]
y=[]
for i in range(len(result)):
    x.append(result[i][0,0])
    y.append(result[i][1,0])
plot(x,y,'k',linewidth=3)
plot(x,y,'o',markersize=10,color='k')
plot(x0[0,0],x0[1,0],'o',markersize=20,color='b')
plot(result[-1][0,0],result[-1][1,0],'o',markersize=20,color='r')
print(result[-1])