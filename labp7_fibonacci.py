#===============================================
# Práctica 7 Parte 1 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#==============================
# Recursividad y memoización
#==============================

#================================
# Herramientas para memoización
#================================
from functools import lru_cache

def fibonacci_lento(n):
    if n == 1:
        return 1
    if n == 2:
        return 1 
    if n > 2:
        return fibonacci_lento(n-1) + fibonacci_lento(n-2)

for i in range(1,36):
    print(str(i) + ":", fibonacci_lento(i))

#========================================
# Optimización 2: Uso de conjuntos para 
#                 guardar valores
#========================================

#=========================
# Conjunto de fibonaccis
#=========================
fibonaccis = {}
def fibonacci(n):

    #=========================================
    # Revisa si ya existe y regresa el valor 
    #=========================================
    if n in fibonaccis:
        return fibonaccis[n]

    if n == 1:
        valor = 1
    elif n == 2:
        valor = 1 
    elif n > 2:
        valor = fibonacci(n-1) + fibonacci(n-2)

    #============
    # Guárdalo
    #============
    fibonaccis[n] = valor 
    return valor 

for i in range(1,10001):
    print(str(i) + ":", fibonacci(i))

#=======================================
# Uso de decoradores para memoización
# maxsize: es cuantos anteriores guarde
#=======================================

#===========================================================
# LRU : Least Recently Used (Menos Utilizado Recientemente)
#===========================================================
"""
                    Análisis de LRU

Si tomamos que el tamaño máximo es 3. tenmos lo siguiente:

Caso 1. Datos:    3,5,3 
        Memoria : [3,5, ]

Caso 2. Datos:   3,5,3,9
        Memoria: [3,5,9]

Caso 3. Datos:   3,5,3,9,1
        Memoria: [3,1,9]

Para obtener el LRU, se traza una linea desde 1 (último elemento agregado)
y se cuentan 3 posiciones (maxsize), así obtenemos: 

                    3 5 3 9 1
                      <------   El valor 5 sería el menos usado recientemente (LRU)

Por eso la memoria en el Caso 3 queda como [3,1,9]. Pongamos un ejemplo más: 

Caso 4. Datos:   3,5,3,9,1,4
        Memoria: [4,1,9]
"""

@lru_cache(maxsize = 3)
def nfibonacci(n):
    if type(n) != int:
        raise TypeError ("n debe ser entero positivo")
    if n < 1: 
        raise ValueError("n debe ser entero positivo")
    
    if n == 1:
        return 1
    if n == 2:
        return 1 
    elif n > 2:
        return nfibonacci(n-1) + nfibonacci(n-2)

for i in range(1,10001):
    print(str(i) + ":", nfibonacci(i))

#====================================
#       FIN DE LA PRÁCTICA
#====================================
