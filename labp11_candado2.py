#===============================================
# Práctica 11 Parte 8 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#===================================================================
# Ejemplo de comunicación bloqueada a una misma variable compartida
# ==================================================================

#====================
# Modulos a utilizar
#====================
from multiprocessing import Process, Value, Lock
import time

def sumale100(numero,candado):
    for i in range(100):
        time.sleep(0.1)
        # Usando candado 
        with candado:
            # Hacer la operación
            numero.value += 1

#====================
# Programa Principal
#====================
if __name__ == "__main__":

    # Candado para evitar que dos procesos se empalmen 
    candado = Lock()
    # Número común a los procesos, i de entero, comienza en 0
    numero_compartido = Value('i', 0)
    print("Al principio vale = ", numero_compartido.value)
    p1 = Process(target=sumale100, args=(numero_compartido, candado))
    p2 = Process(target=sumale100, args=(numero_compartido,candado))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Al final vale = ", numero_compartido.value)

#====================================
#       FIN DE LA PRÁCTICA
#====================================