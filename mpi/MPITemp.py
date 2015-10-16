# -*- coding: utf-8 -*-
import scipy as sci
import scipy.linalg as linalg
from mpi4py import MPI

'''
ln = lambda neumann
ld = lambda dirichlet
ldo = lambda dirichlet old

'''

rank = MPI.COMM_WORLD.rank

N = 3
dx = 1./N
Tn = 15.
Tw = 5.
Th = 40.
w = 0.8

NbrItr = 10

u1o = sci.ones((N-1)*(2*N-1))*20
u0o = sci.ones((N-1)**2)*20
u2o = sci.ones((N-1)**2)*20
ld0 = sci.ones(N-1)*20
ld1 = sci.ones(N-1)*20
ldo0 = ld0
ldo1 = ld1

for i in range(NbrItr):
    
    if(rank is 1):
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
        MPI.COMM_WORLD.Send(ln0, dest = 0)
        MPI.COMM_WORLD.Send(ln1, dest = 2)
        MPI.COMM_WORLD.Recv(ld0, source = 0)
        MPI.COMM_WORLD.Recv(ld1, source = 2)
        if(i is NbrItr-1):
            MPI.COMM_WORLD.Send(u1, dest = 3)
            MPI.COMM_WORLD.Send(ld0, dest = 3)
            MPI.COMM_WORLD.Send(ld1, dest = 3)
        
        #Rum 0
    if(rank is 0):
        ln0 = sci.zeros(N-1)
        MPI.COMM_WORLD.Recv(ln0, source = 1)
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
        MPI.COMM_WORLD.Send(ld0, dest = 1)
        if(i is NbrItr-1):
            MPI.COMM_WORLD.Send(u0, dest = 3)
#        print(ld0)
    #Rum 2
    if(rank is 2):
        ln1 = sci.zeros(N-1)
        MPI.COMM_WORLD.Recv(ln1, source = 1)
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
        MPI.COMM_WORLD.Send(ld1, dest = 1)
        if(i is NbrItr-1):
            MPI.COMM_WORLD.Send(u2, dest = 3)
        
if(rank is 3):
    u1 = sci.ones((N-1)*(2*N-1))*20
    u0 = sci.ones((N-1)**2)*20
    u2 = sci.ones((N-1)**2)*20
    ld0 = sci.zeros(N-1)
    ld0 = sci.zeros(N-1)
    MPI.COMM_WORLD.Recv(u0, source = 0)
    MPI.COMM_WORLD.Recv(u2, source = 2)
    MPI.COMM_WORLD.Recv(u1, source = 1)       
    MPI.COMM_WORLD.Recv(ld0, source = 1)
    MPI.COMM_WORLD.Recv(ld1, source = 1)
        
    pmat=sci.zeros([2*N+1,3*N+1])
    
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
        
    print("\n\n",i)
    pmat[0][4] = round(Th)
    pmat[0][5] = round(Th)
    pmat[0][3] = round((Th+Tn)/2)
    pmat[3][0] = round((Th+Tn)/2)
    pmat[4][0] = round(Th)
    pmat[5][0] = round(Th)
    pmat[6][0] = round((Th+Tn)/2)
    pmat[0][9] = round((Th+Tn)/2)
    pmat[1][9] = round(Th)
    pmat[2][9] = round(Th)
    pmat[3][9] = round((Th+Tn)/2)
    pmat[6][4] = round(Tw)
    pmat[6][5] = round(Tw)
    pmat[6][6] = round((Tw+Tn)/2)
    pmat[3][1] = Tn
    pmat[3][2] = Tn
    pmat[3][3] = Tn
    pmat[2][3] = Tn
    pmat[1][3] = Tn
    pmat[3][6] = Tn
    pmat[4][6] = Tn
    pmat[5][6] = Tn
    pmat[3][7] = Tn
    pmat[3][8] = Tn
    pmat[6][1] = Tn
    pmat[6][2] = Tn
    pmat[6][3] = (Tn+Tw)/2
    pmat[0][6] = (Tn+Th)/2
    pmat[0][7] = Tn
    pmat[0][8] = Tn        
    print(pmat)
    print()     


        
