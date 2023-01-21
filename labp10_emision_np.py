#=================================================
# Práctica 10 Parte 10 Paradigmas de Programación
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
rank = comm.Get_rank()  # Obten el identificador de cada proceso 

#====================
# Tamaño del arreglo
#====================
n = 10
if rank == 0:
    # Arreglo de enteros del 0 al n-1
    data = numpy.arange(n, dtype='i')
else:
    # Arreglo vacío de enteros de tamaño n 
    data = numpy.empty(n, dtype='i')

#===========================================
#  Broadcast pro que indica el tipo de dato
#  Optimizado para comunicación rápida 
#===========================================
comm.Bcast([data, MPI.INT], root=0)

#================================
# Asegurarse que todo salió bien
#================================
for i in range(n):
    assert data[i] == i
print(data)

# La función principal de las aserciones es activar las alarmas cuando aparece un error en un programa.
# En este contexto, las aserciones significan Asegúrese de que esta condición sigue siendo verdadera. 
# En caso contrario, lanzar un error (error = "AsertionError").

#====================================
#       FIN DE LA PRÁCTICA
#====================================













