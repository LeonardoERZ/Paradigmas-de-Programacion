#===============================================
# Práctica 11 Parte 5 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#====================
# Modulos a utilizar
#====================
import multiprocessing as mp
import numpy as np
import time

def my_function(i,param1, param2, param3):
    # Calcula un polinomio
    result = param1**2 + param2 + param3
    # Se hace tonta dos segundos
    time.sleep(2)
    return(i,result)

def get_result(result):
    # Se inscriben en la lista globlal
    # (mal estilo de programacion)
    global results
    results.append(result)

#====================
# Programa Principal
#====================
if __name__ == "__main__":

    # Matriz de 10x3 números al azar 
    params = np.random.random((10,3))*100.0
    results = []
    ts = time.time()

    # Un grupo de procesos (pool)
    pool = mp.Pool(mp.cpu_count())

    # loop de primera dimensión del arreglo 
    for i in range(0, params.shape[0]):
        # Correr asíncronicamente my_function con argumentos args y cuando termine correr get_result
        pool.apply_async(my_function, args=(i, params[i,0], params[i,1], params[i,2]),callback=get_result)

    # Cerrar el grupo 
    pool.close()

    # Esperar a que termine el grupo
    pool.join()
    
    print("Tiempo en paralelo = ", time.time()-ts)
    print(results)

#====================================
#       FIN DE LA PRÁCTICA
#====================================