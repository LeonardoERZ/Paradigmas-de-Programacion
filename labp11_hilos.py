#===============================================
# Práctica 11 Parte 1 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#====================
# Modulos a utilizar
#====================
from threading import Thread
import os
import math
import time 

def calc():
    for i in range(0,4000000):
        math.sqrt(i)

threads = [] # arreglo vacio 
cpus = os.cpu_count()
print("Núcleos en tu PC: ", cpus)
for i in range(cpus):
    print("registrando el hilo %d" %i)
    threads.append(Thread(target=calc))

start = time.time()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end = time.time()
print("Se tardó: ",end-start)

#====================================
#       FIN DE LA PRÁCTICA
#====================================