#===============================================
# Práctica 10 Parte 6 Paradigmas de Programación
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

comm = MPI.COMM_WORLD   # Crea el objeto comunicador 
rank = comm.Get_rank()  # Obten el identificador de cada proceso 

#==============================
# Arreglo con un solo elemento
#==============================
randNum = np.zeros(1) 

if rank == 1:
    randNum = np.random.random_sample(1)
    print("Proceso", rank,"generó", randNum[0])
    comm.Isend(randNum, dest=0)
    req = comm.Irecv(randNum, source=0)
    req.Wait()
    print("Proceso", rank, "recibió el número", randNum[0])

if rank == 0:
    randNum = np.random.random_sample(1)
    print("Proceso", rank,"generó", randNum[0])
    comm.Isend(randNum, dest=1)
    req = comm.Irecv(randNum, source=1)
    req.Wait()
    print("Proceso", rank, "recibió el número", randNum[0])

# Como no tiene la instrucción: size = comm.Get_size()  # Obten el tamaño de procesos 
# Entonces solo hará los primeros dos procesos, y los demás los va a ignorar pues no 
# están definifidos (observe la condición del la estructura de control if).

# La fuente 0 recibe la información de la fuente uno y viceversa.

#====================================
#       FIN DE LA PRÁCTICA
#====================================
