#===============================================
# Práctica 10 Parte 3 Paradigmas de Programación
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

#=================
# Objeto mensaje 
#=================
class Mensaje: 
    def __init__(self,rank):
        # Iterador
        self.x = range(rank*10)
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
    fuente = rank-1 if rank!=0 else size-1

    #=============================================================
    # Mándalo al siguiente y si eres el último mandalo al primero
    #=============================================================
    destino = rank+1 if rank!=size-1 else 0

    #==============================================================
    # send y recieve son operaciones bloqueantes y generan que el 
    # código se atore esperando que alguien reciba un mensaje 
    # esto puede resolverse enviando con los pares y recibiendo con 
    # los impares 
    #===============================================================

    # Si soy par 
    if rank%2 == 0:
        #==========================
        # Enviar mensaje s al dest
        #==========================
        comm.send(s, dest=destino)

        #==================================
        # Recibir de source y lo pone en m
        #==================================
        m = comm.recv(source=fuente)

    # Si no soy par 
    else:
        #==========================================
        # Recibir primero y mandar mensaje después 
        #==========================================
        m = comm.recv(source=fuente)
        comm.send(s,dest=destino)

    # x y p son variables del objeto Mensaje
    print("Soy el proceso ",rank,", el resultado es  ",len(m.x),",",m.p)

#====================================
#       FIN DE LA PRÁCTICA
#====================================