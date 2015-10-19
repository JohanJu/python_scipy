import scipy as sci
#from mpi4py import MPI
import time
import sys
import pylab as py
from scipy import linalg
py.rcParams['figure.figsize'] = 12, 12
sci.set_printoptions(linewidth =1000)
sci.set_printoptions(threshold=50000)
'''

rank = MPI.COMM_WORLD.rank
a = sci.array([1,2,3])*(rank*9+1)
#print("rank ",rank," a1 ",a)

if rank == 0:
        print("hej")
        sys.stdout.flush()
        time.sleep(2)
        MPI.COMM_WORLD.Send(a, dest = 1)
        
else:
        MPI.COMM_WORLD.Recv(a, source = 0)
        print("hejdå")
        
        sys.stdout.flush()
        x = sci.linspace(0,10)
        py.plot(x,x)
        py.show()
        
        
#print("rank ",rank," a2 ",a)

#run with "mpiexec -n 2 python test.py"
'''
Tn = 15.
Tw = 5.
Th = 40.
N = 3
size = (N-1)*(2*N-1)
u = sci.zeros(size)
b = sci.zeros(size)
A = sci.zeros((size, size), dtype=sci.int8)
#A = sci.sparse.coo_matrix((size, size), dtype=sci.int8).toarray()
#print(A)
ld0 = sci.ones(N-1)*20
ld1 = sci.ones(N-1)*20

def setAb(r,k):
    pos = r+k*(2*N-1) 
    #    print(r," ",k," ",pos," ",pos+(2*N-1))
    A[pos][pos] = -4    
    
    #rutan under
    if(r+1 is 2*N-1):
        b[pos] += Tw
    else:
        A[pos][pos+1] = 1
        
    #rutan ovanför
    if(r-1 is -1):
        b[pos] += Th
    else:
        A[pos][pos-1] = 1  
        
    #rutan vänster
    if(k-1 is -1):
        if(r>=N):
            b[pos] += ld0[r-N]
        else:
            b[pos] += Tn
    else:
        A[pos][pos-(2*N-1)] = 1  
        
    #rutan höger
    if(k+1 is N-1):
        if(r<N-1):
            b[pos] += ld1[r]
        else:
            b[pos] += Tn
    else:
        A[pos][pos+(2*N-1)] = 1  
        
for i in range(N-1):
    for j in range(2*N-1):
        setAb(j,i)

#b = -b
#print(A)
u=sci.linalg.solve(A,b)
#print(A)
print(b.reshape(N-1,-1).transpose())
#print(u)

