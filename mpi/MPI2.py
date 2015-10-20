# -*- coding: utf-8 -*-
import scipy as sci
import scipy.linalg as linalg
from mpi4py import MPI
import matplotlib.pyplot as plt
import pylab as py
py.rcParams['figure.figsize'] = 12, 12

'''
ln = lambda neumann
ld = lambda dirichlet
ldo = lambda dirichlet old

'''
rank = MPI.COMM_WORLD.rank
#rank = 1

N = 3
dx = 1./N
Tn = 15.
Tw = 5.
Th = 40.
T0 = 20
w = 0.8

NbrItr = 1


def setAb(r,k,m,n):
    
    pos = r+k*m 
    A[pos][pos] = -4    
    
    #rutan under
    if(r+1 is m):
        if(rank is 1):
            b[pos] -= Tw
        else:
            b[pos] -= Tn
    else:
        A[pos][pos+1] = 1
        
    #rutan ovanför
    if(r is 0):
        if(rank is 1):
            b[pos] -= Th
        else:
            b[pos] -= Tn
    else:
        A[pos][pos-1] = 1  
        
    #rutan vänster
    if(k is 0):
        if(rank is 1):
            if(r>=N):
                b[pos] -= ld0[r-N]
            else:
                b[pos] -= Tn
        else:
            b[pos] -= Th
    else:
        A[pos][pos-m] = 1  
        
    #rutan höger
    if(k+1 is n):
        if(rank is 1):
            if(r<n):
                b[pos] -= ld1[r]
            else:
                b[pos] -= Tn
        else:
            A[pos][pos] += 1
            b[pos] -=ln[r]
    else:
        A[pos][pos+m] = 1  


if(rank is 1):
    m = 2*N-1
    n = N-1
    ld0 = sci.ones(n)*T0
    ld1 = sci.ones(n)*T0
else:
    m = N-1
    n = N-1
    ldo = sci.ones(n)*T0
size = m*n
A = sci.zeros((size, size), dtype=sci.int8)
b = sci.zeros(size)
uo = sci.ones(size)*T0



for i in range(NbrItr):
                
    if(rank is 1):
        for j in range(n):
            for k in range(m):
                setAb(k,j,m,n)
        u = sci.linalg.solve(A,b)
        u = w*u+(1-w)*uo
        uo=u
        print(u)
        ln0 = ld0-u[n+1:m]
        ln1 = ld1-u[m*(n-1):m*(n-1)+n]
        MPI.COMM_WORLD.Send(ln0, dest = 0)
        MPI.COMM_WORLD.Send(ln1, dest = 2)
        ld0 = sci.zeros(n)
        ld1 = sci.zeros(n)
        MPI.COMM_WORLD.Recv(ld0, source = 0)
        MPI.COMM_WORLD.Recv(ld1, source = 2)
#        print(ln0)
#        print(ln1)
#        print(ld0)
#        print(ld1)
        MPI.COMM_WORLD.Send(u, dest = 3)
        MPI.COMM_WORLD.Send(ld0, dest = 3)
        MPI.COMM_WORLD.Send(ld1, dest = 3)
        
    if(rank is 0):
        ln = sci.zeros(n)
        MPI.COMM_WORLD.Recv(ln, source = 1)
        for j in range(n):
            for k in range(m):
                setAb(k,j,m,n)
        u = sci.linalg.solve(A,b)
        u = w*u+(1-w)*uo
        uo=u
        
        ld = u[(n-1)*n:]-ln
        ld = w*ld + (1-w)*ldo
        ldo = ld        
        MPI.COMM_WORLD.Send(ld, dest = 1)
        MPI.COMM_WORLD.Send(u, dest = 3)
    #Rum 2
    if(rank is 2):
        ln = sci.zeros(n)
        MPI.COMM_WORLD.Recv(ln, source = 1)
        for j in range(n):
            for k in range(m):
                setAb(k,j,m,n)
        ln = ln[::-1]
        u = sci.linalg.solve(A,b)
        u = w*u+(1-w)*uo
        uo=u
        ld = u[(n-1)*n:]-ln
        ld = w*ld + (1-w)*ldo
        ldo = ld
        ldr = sci.array(ld[::-1])
        ur = sci.array(u[::-1])
#        print(ldr)
        MPI.COMM_WORLD.Send(ldr, dest = 1)
        MPI.COMM_WORLD.Send(ur, dest = 3)
        
    if(rank is 3):
#        print("hello")
        u1 = sci.ones((N-1)*(2*N-1))*20
        u0 = sci.ones((N-1)**2)*20
        u2 = sci.ones((N-1)**2)*20
        ld0 = sci.zeros(N-1)
        ld1 = sci.zeros(N-1)
        MPI.COMM_WORLD.Recv(u0, source = 0)
        MPI.COMM_WORLD.Recv(u2, source = 2)
        MPI.COMM_WORLD.Recv(u1, source = 1)       
        MPI.COMM_WORLD.Recv(ld0, source = 1)
        MPI.COMM_WORLD.Recv(ld1, source = 1)
            
        pmat=sci.zeros([2*N+1,3*N+1])
        pmat.fill(-20)
        
        for r in range(N-1):
            for k in range(N-1):
                pmat[r+4][k+1] = round(u0[k*(N-1)+r],1)
                
        for r in range(2*N-1):
            for k in range(N-1):
                pmat[r+1][k+4] = round(u1[k*(2*N-1)+r],1)
                
        for r in range(N-1):
            for k in range(N-1):
                pmat[r+1][k+7] = round(u2[k*(N-1)+r],1)
                
        for r in range(N-1):
            pmat[r+4][3] = round(ld0[k],1)
            pmat[r+1][6] = round(ld1[k],1)
#        print(pmat)