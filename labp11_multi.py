#===============================================
# Práctica 11 Parte 2 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#====================
# Modulos a utilizar
#====================
from multiprocessing import Process
import os
import math
import time 

def calc():
    for i in range(0,4000000):
        math.sqrt(i)

procesos = [] # arreglo vacio 
cpus = os.cpu_count()
print("Núcleos en tu PC: ", cpus)
for i in range(cpus):
    print("registrando el hilo %d" %i)
    procesos.append(Process(target=calc))

start = time.time()

for proceso in procesos:
    proceso.start()

for proceso in procesos:
    proceso.join()

end = time.time()
print("Se tardó: ",end-start)

#====================================
#       FIN DE LA PRÁCTICA
#====================================