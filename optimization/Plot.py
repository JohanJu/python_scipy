# -*- coding: utf-8 -*-
# @author: Caroline Brandberg, Johan Ju
import pylab as py
py.rcParams['figure.figsize'] = 12, 12
from scipy import *

def plot(f,result):
    n = 100
    x = linspace(-0.2,1.2,n)
    y = linspace(-0.2,1.2,n)
    X, Y = meshgrid(x, y)
    Z = zeros([n,n])
    for i in range(n):
        for j in range(n):
            Z[i,j] = f(array([X[i,j],Y[i,j]]))
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
#    py.plot(x0[0,0],x0[1,0],'o',markersize=20,color='b')
    py.plot(result[-1][0,0],result[-1][1,0],'o',markersize=20,color='r')