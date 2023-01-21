#=================================================
# Práctica 10 Parte 11 Paradigmas de Programación
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

comm = MPI.COMM_WORLD   # Crea el objeto comunicador 
size = comm.Get_size()  # Obten el tamaño de procesos 
rank = comm.Get_rank()  # Obten el identificador de cada proceso

data = (rank+1)**2

#====================================
# Manden sus datos al proceso root=0
# (en orden)
#====================================
datas = comm.gather(data, root=0)

#==============================
# Asegurarse que todo funcione
#==============================
if rank == 0: # Solo en el identificador cero se imprimirá la información 
    for i in range(size):
        assert datas[i] == (i+1)**2
else:   # Los demás valores tendrán None
    assert datas is None 

print(datas)

#====================================
#       FIN DE LA PRÁCTICA
#====================================