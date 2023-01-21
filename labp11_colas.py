#===============================================
# Práctica 11 Parte 4 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#====================
# Modulos a utilizar
#====================
from multiprocessing import Process, Queue

def cuadrado(x,q):
    q.put((x,x*x))

#====================
# Programa Principal
#====================
if __name__ == "__main__":
    q = Queue()
    procesos = [Process(target=cuadrado,args=(i,q)) for i in range(2,10)]
    for p in procesos:
        p.start()
    for p in procesos:
        p.join
    resultado = [q.get() for p in procesos]
    print(resultado) # No los imprimira en orden

#====================================
#       FIN DE LA PRÁCTICA
#====================================
