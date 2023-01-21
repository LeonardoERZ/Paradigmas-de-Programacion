#===============================================
# Práctica 10 Parte 7 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#=====================================
# mpiexec -n 4 python3 hola_mpi.py
# mpirun  -n 4 python3 hola_mpi.py
#=====================================

#=============================
# Forma compacta de random_nb
#=============================

#====================
# Modulos a utilizar
#====================
from mpi4py import MPI
import numpy 

comm = MPI.COMM_WORLD   # Crea el objeto comunicador 
rank = comm.Get_rank()  # Obten el identificador de cada proceso 

#==============================
# Arreglo con un solo elemento
#==============================
randNum = numpy.zeros(1) 

if rank == 1:
    dst = 0
    src = 0
if rank == 0:
    dst = 1  
    src = 1
    
randNum = numpy.random.random_sample(1)
print("Proceso", rank, "generó el número", randNum[0])
comm.Isend(randNum, dest=dst)
req = comm.Irecv(randNum, source=src)
req.Wait()
print("Proceso", rank, "recibió el número", randNum[0])

# Como no tiene la instrucción: size = comm.Get_size()  # Obten el tamaño de procesos 
# Entonces solo hará los primeros dos procesos, y los demás los va a ignorar pues no 
# están definifidos (observe la condición del la estructura de control if). Particularmente
# SI SE EXCEDEN O NO SE PONE EL NUMERO DE PROCESOS DECLARADOS, NOS MANDARA UN MENSAJE DE ERROR.

# La fuente 0 recibe la información de la fuente uno y viceversa.

#====================================
#       FIN DE LA PRÁCTICA
#====================================