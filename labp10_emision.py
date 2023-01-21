#===============================================
# Práctica 10 Parte 9 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#=====================================
# mpiexec -n 4 python3 hola_mpi.py
# mpirun  -n 4 python3 hola_mpi.py
#=====================================

#========================
# Broadcast con MPI
# distribución de datos 
#========================

#====================
# Modulos a utilizar
#====================
from mpi4py import MPI 

comm = MPI.COMM_WORLD   # Crea el objeto comunicador 
rank = comm.Get_rank()  # Obten el identificador de cada proceso 

#=========================================
# El proceso 0 tiene datos y los otros no 
#=========================================
if rank == 0:
    data = {'key1':[7, 2.7, 2+3],
            'key2':('abc', 'xyz')}
else:
    data = None     

#====================================================
# Enviar diccionario a todos los procesos desde root
#====================================================
data = comm.bcast(data, root=0)
print(data)

# Análisis de lo que se hizo: 

# Lo que ocurre es que, primero, asignamos algunos datos al rango 0, el nodo maestro. 

# A continuación, queremos "difundir" con bcast los datos a todos los demás nodos. 

# Para ello, primero establecemos todos los datos en None, de modo que todos los demás 
# nodos tengan None como dato.

# A continuación, utilizamos comm.bcast() para difundir los datos desde el rango 0. 

# Así, el primer parámetro son los datos, el segundo, "root", significa "desde qué nodo". 

# Con broadcast, todos los nodos aceptan automáticamente los datos, bajo el nombre var "data".

#====================================
#       FIN DE LA PRÁCTICA
#====================================