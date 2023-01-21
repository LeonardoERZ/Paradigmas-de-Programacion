#=================================================
# Práctica 10 Parte 13 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#=================================================

#=====================================
# mpiexec -n 4 python3 hola_mpi.py
# mpirun  -n 4 python3 hola_mpi.py
#=====================================

#====================
# Modulos a utilizar
#====================
from mpi4py import MPI
import math  

comm = MPI.COMM_WORLD   # Crea el objeto comunicador 
size = comm.Get_size()  # Obten el tamaño de procesos 
rank = comm.Get_rank()  # Obten el identificador de cada proceso

#====================
# Tamaño del arreglo
#====================
n = 40
x = range(n)
m = int(math.ceil(float(len(x))/ size))
x_chunk = list(x[rank*m:(rank+1)*m])
r_chunk = list(map(math.sqrt, x_chunk))

#===================================
# Una sola lista de todos los datos
#===================================
r = comm.allreduce(r_chunk)

#================================
# Una matriz con todos los datos
#================================
rr = comm.allgather(r_chunk)

#================================
# Una matriz con todos los datos
#================================
rrr = comm.gather(r_chunk,root=1)

if rank == 0:
    print(r)
    print(rr)
    print(rrr)
if rank == 1:
    print(rrr)

#====================================
#       FIN DE LA PRÁCTICA
#====================================




