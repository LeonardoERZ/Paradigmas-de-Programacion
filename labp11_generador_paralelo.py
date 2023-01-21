#=================================================
# Práctica 11 Parte 10 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#=================================================

#====================
# Modulos a utilizar
#====================
from multiprocessing import Process
import random
import os 

N:int = 10

def generador(N:float) -> None:
    semilla:float = random.uniform(-1,1)
    print("La semilla es: ",semilla)
    random.seed(semilla)
    for i in range(N):
        x:float = random.uniform(-1,1)
        y:float = random.uniform(-1,1)
        print("x = ",x,"\t y = ",y)

procesos = []
cpus = os.cpu_count()
print("Procesadores = ",cpus)
for i in range(cpus):
    procesos.append(Process(target=generador,args=(N,)))

# Comienza con los procesos en paralelo 
for proceso in procesos:
    proceso.start()

# Espera a que todos los procesos terminen 
for proceso in procesos:
    proceso.join()

#====================================
#       FIN DE LA PRÁCTICA
#====================================