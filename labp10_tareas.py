#===============================================
# Práctica 10 Parte 2 Paradigmas de Programación
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

#=========================
# Objeto de comunicadores 
#=========================
comm = MPI.COMM_WORLD

#=========================
# Cuántos somos en total 
#=========================
size = comm.Get_size()

#============
# Quién soy 
#============
rank = comm.Get_rank()

#=============================
# Si yo soy el cero hago esto 
#=============================
if rank == 0:
    print("Yo soy el proceso 0")

#=========================================
# Si yo soy el proceso uno hago esto otro
#=========================================
elif rank == 1:
    print("Yo soy el proceso 1");

#===============================================
# Si yo no soy ni el cero, ni el uno, hago esto 
#===============================================
else:
    print("Yo no soy ninguno de los dos primeros procesos")

print("Reportandome, soy el proceso ", str(rank), "de ", str(size))

#====================================
#       FIN DE LA PRÁCTICA
#====================================