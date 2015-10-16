# -*- coding: utf-8 -*-
import scipy as sci
from mpi4py import MPI

'''
ln = lambda neumann
ld = lambda dirichlet
ldo = lambda dirichlet old

'''

rank = MPI.COMM_WORLD.rank

N = 3.
dx = 1./N
Tn = 15.
Tw = 5.
Th = 40.
w = 0.8

if(1 is 1):
    u1o = sci.ones((N-1)*(2*N-1))*20
    u0o = sci.ones((N-1)**2)*20
    u2o = sci.ones((N-1)**2)*20
    ld0 = sci.ones(N-1)*20
    ld1 = sci.ones(N-1)*20
    ldo0 = ld0
    ldo1 = ld1
    
    for i in range(10):
        size = 2*N-1
        main = sci.ones(size)*-4
        sub = sci.ones(size-1)
        T = sci.diag(main)+sci.diag(sub,-1)+sci.diag(sub,+1)
        I = sci.eye(size)
        A1=sci.hstack((sci.vstack((T,I)),sci.vstack((I,T))))
        
        b1 = -sci.array([Tn+Th,Tn,Tn,ld0[0],ld0[1]+Tw,ld1[0]+Th,ld1[1],Tn,Tn,Tn+Tw])
        u1 = sci.linalg.solve(A1,b1)
        u1 = w*u1+(1-w)*u1o
        u1o=u1
        
        ln0 = sci.array([ld0[0]-u1[3],ld0[1]-u1[4]])/dx#to 0
        ln1 = sci.array([ld1[0]-u1[5],ld1[1]-u1[6]])/dx#to 2
        #Rum 0
        size = N-1
        main = sci.ones(size)*-4
        sub = sci.ones(size-1)
        T = sci.diag(main)+sci.diag(sub,-1)+sci.diag(sub,+1)
        main = sci.ones(size)*-3
        Tneu = sci.diag(main)+sci.diag(sub,-1)+sci.diag(sub,+1)
        I = sci.eye(size)
        A0=sci.hstack((sci.vstack((T,I)),sci.vstack((I,Tneu))))
        
        b0 = -sci.array([Tn+Th,Th+Tn,Tn-ln0[0]*dx,Tn-ln0[1]*dx])
        
        u0 = sci.linalg.solve(A0,b0)
        u0 = w*u0+(1-w)*u0o
        u0o=u0
        
        ld0 = sci.array([u0[2]-ln0[0]*dx,u0[3]-ln0[1]*dx])#to 1
        ld0 = w*ld0 + (1-w)*ldo0
        ldo0 = ld0        
        
#        print(ld0)
        #Rum 2
        size = N-1
        main = sci.ones(size)*-4
        sub = sci.ones(size-1)
        T = sci.diag(main)+sci.diag(sub,-1)+sci.diag(sub,+1)
        main = sci.ones(size)*-3
        Tneu = sci.diag(main)+sci.diag(sub,-1)+sci.diag(sub,+1)
        I = sci.eye(size)
        A2=sci.hstack((sci.vstack((Tneu,I)),sci.vstack((I,T))))
    
        b2 = -sci.array([Tn+dx*ln1[0],Tn+dx*ln1[1],Th+Tn,Th+Tn])
        
        u2 = sci.linalg.solve(A2,b2)
        u2 = w*u2+(1-w)*u2o
        u2o=u2
        
        ld1 = sci.array([u2[0]-ln1[0]*dx,u2[1]-ln1[1]*dx])#to 1
        ld1 = w*ld1 + (1-w)*ldo1
        ldo1 = ld1
        
#        pmat=sci.zeros([2*N+1,3*N+1])
        
#        for r in range(N-1):
#            for k in range(N-1):
#                pmat[r+4][k+1] = round(u0[k*(N-1)+r],1)
#                
#        for r in range(N-1):
#            for k in range(N-1):
#                pmat[r+4][k+1] = round(u0[k*(N-1)+r],1)
#                
#        for r in range(N-1):
#            for k in range(N-1):
#                pmat[r+4][k+1] = round(u0[k*(N-1)+r],1)
                
#    print(pmat)
                
        print("\n\n",i)
        print(u0)
        print(u1)
        print(u2)
        
