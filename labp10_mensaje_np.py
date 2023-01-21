#===============================================
# Práctica 10 Parte 8 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

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
rank = comm.Get_rank()  # Obten el identificador de cada proceso 

#===========================================
# Se indica el tipo de datos explícitamente 
#===========================================

#==========================
# EJEMPLO 1 USANDO ENTEROS 
#==========================
if rank == 0:
    #===============================
    # Arreglo de enteros del 0 al 9
    #===============================
    data = numpy.arange(10, dtype = 'i') # 'i' indica que el dato será entero 
    #================================================
    # Envío bloqueante especificando el tipo de dato
    #================================================
    comm.Send([data, MPI.INT], dest=1, tag=77) # tag es como el canal de comunicación 

elif rank == 1:
    data = numpy.empty(10, dtype='i') # también se puede poner 'int' (cambialos en ambos dtype)
    comm.Recv([data, MPI.INT], source=0, tag=77) # como tag=77, recibira lo que tiene el destino 1
    print(data)

#==========================================================
# También se puede sin decir el tipo de dato pero deben 
# coincidir el tipo de arreglos a los extremos del mensaje
#==========================================================

#============================
# EJEMPLO 2 USANDO FLOTANTES 
#============================
if rank == 0:
    data = numpy.arange(10, dtype=numpy.float64)
    comm.Send(data, dest=1, tag=13)
elif rank == 1:
    data = numpy.empty(10, dtype=numpy.float64)
    comm.Recv(data, source=0, tag=13)
    print(data)

#====================================
#       FIN DE LA PRÁCTICA
#====================================