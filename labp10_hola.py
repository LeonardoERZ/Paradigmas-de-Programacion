#===============================================
# Práctica 10 Parte 1 Paradigmas de Programación
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

#=============================
# Crear un objeto comunicador
#=============================
comunicadores = MPI.COMM_WORLD

#==========================
# Número total de procesos
#==========================
n_procesos = comunicadores.Get_size()

#======================================
# Número identificador de este proceso
#======================================
quien_soy = comunicadores.Get_rank()

print("Saludos desde el proceso ",str(quien_soy), "de ", str(n_procesos))

#====================================
#       FIN DE LA PRÁCTICA
#====================================