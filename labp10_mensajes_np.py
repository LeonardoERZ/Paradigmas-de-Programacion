#===============================================
# Práctica 10 Parte 5 Paradigmas de Programación
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
import numpy as np

#=================
# Objeto mensaje 
#=================
class Mensaje: 
    def __init__(self,rank):
        #===============================
        # Arreglo de numpy (optimizado)
        #===============================
        # Iterador
        self.x = np.array([float(x+rank) for x in range(10)])
        # String 
        self.p = "Vengo del proceso "+ str(rank)

#====================
# Programa principal 
#====================
if __name__ == '__main__':
    comm = MPI.COMM_WORLD   # Crea el objeto comunicador 
    size = comm.Get_size()  # Obten el tamaño de procesos 
    rank = comm.Get_rank()  # Obten el identificador de cada proceso 
    s = Mensaje(rank)

    #===========================================================
    # Que te mande el anterior, y si es cero, que sea el último
    #===========================================================
    src = rank-1 if rank!=0 else size-1

    #=============================================================
    # Mándalo al siguiente y si eres el último mandalo al primero
    #=============================================================
    dst = rank+1 if rank!=size-1 else 0

    #=====================
    # Arreglo para enviar
    #=====================
    m = s.x

    #====================================
    # Isend Irecv son para comunicación 
    # no bloqueante de arreglos de numpy 
    #====================================
    comm.Isend(m, dest=dst)

    #===================================
    # Arreglo vacío para recibir 
    # con dimensión 10 y tipo de datos 
    # float64(doble precisión)
    #===================================
    a = np.zeros(10,dtype=np.float64)
    req = comm.Irecv(a,source=src)
    req.Wait()

    print("Soy el proceso ",rank,", el resultado es ", a)

#====================================
#       FIN DE LA PRÁCTICA
#====================================