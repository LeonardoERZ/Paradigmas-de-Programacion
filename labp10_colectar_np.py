#=================================================
# Práctica 10 Parte 12 Paradigmas de Programación
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
import numpy

comm = MPI.COMM_WORLD   # Crea el objeto comunicador 
size = comm.Get_size()  # Obten el tamaño de procesos 
rank = comm.Get_rank()  # Obten el identificador de cada proceso

n = 10 

#===========================================
# Arreglo con ceros de tamaño n
# sumando con un escalara (en cada entrada)
#===========================================
sendarray = numpy.zeros(n, dtype='i')+rank

recvarray = None

if rank == 0:
    #========================================
    # Matríz vacía de tamaño procesos * n
    # dtype es el tipo de dato (i) es entero
    #========================================
    recvarray = numpy.empty([size,n],dtype='i')

#==============================
# Gather es rápido para numpy 
# enviar datos al proceso root
#==============================
comm.Gather(sendarray, recvarray, root=0)

if rank == 0:
    for i in range(size):
        #============================================================
        # Revisa por fila la matriz
        # : significa todos los elementos de esa dimensión
        # allclose es un método de numpy que compara a los elementos 
        #============================================================
        assert numpy.allclose(recvarray[i,:],i)

print(recvarray)

# Función de assert: Activar las alarmas cuando aparece un error en un programa
#====================================
#       FIN DE LA PRÁCTICA
#====================================
