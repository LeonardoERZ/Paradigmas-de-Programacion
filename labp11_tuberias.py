#===============================================
# Práctica 11 Parte 3 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#====================
# Modulos a utilizar
#====================
from multiprocessing import Process
import multiprocessing as mp  # Agregué esta instrucción para evitar el problema de Pipe() 

def f(extremo):
    extremo.send([0,1,2,3,4])
    extremo.close()

def g(extremo):
    a = extremo.recv()
    for i in a:
        a[i] += 100
    print(a)

#====================
# Programa Principal
#====================
if __name__ == "__main__":
    extremo1, extremo2 = mp.Pipe()
    proceso1 = Process(target=f, args=(extremo1,)) # La coma es para resaltar que no es una función
    proceso2 = Process(target=g, args=(extremo2,))
    proceso2.start()
    proceso1.start()
    proceso1.join()
    proceso2.join()

#====================================
#       FIN DE LA PRÁCTICA
#====================================
