import scipy as sci
from mpi4py import MPI
rank = MPI.COMM_WORLD.rank
a = sci.array([1,2,3])*(rank*9+1)
print("rank ",rank," a1 ",a)

if rank == 0:
        MPI.COMM_WORLD.Send(a, dest = 1)
        MPI.COMM_WORLD.Recv(a, source = 1)
else:
        MPI.COMM_WORLD.Send(a, dest = 0)
        MPI.COMM_WORLD.Recv(a, source = 0)
        
print("rank ",rank," a2 ",a)

#run with "mpiexec -n 2 python test.py"