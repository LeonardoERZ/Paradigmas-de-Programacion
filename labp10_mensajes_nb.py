#===============================================
# Práctica 10 Parte 4 Paradigmas de Programación
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
        self.x = [i for i in range(rank*10)]
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
    # Envío no bloqueante 
    #=====================
    comm.isend(s, dest=dst)

    #==================================
    # Recibir no bloqueante con espera 
    # req: request (petición)
    #==================================
    req = comm.irecv(source=src)
    a = req.wait()

    # x y p son variables del objeto Mensaje
    print("Soy el proceso ",rank,", el resultado es ", len(a.x),",",a.p)

#====================================
#       FIN DE LA PRÁCTICA
#====================================
