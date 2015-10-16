import scipy as sci
from mpi4py import MPI
import time
import sys
import pylab as py
py.rcParams['figure.figsize'] = 12, 12


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

