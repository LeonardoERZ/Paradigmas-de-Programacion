#===============================================
# Práctica 8 Parte 2 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

mi_lista = [1,2,3]
tu_lista = (10,20,30)
su_lista = (40,50,100)
def multiplicar_por2(elemento):
    return elemento*2

def solo_impar(elemento):
    return elemento % 2 != 0

# Lista de pares de datos ordenados de las tres listas
# Obs: El orden de impresion es por posicion de los elementos 
print(list(zip(mi_lista, tu_lista, su_lista)))

una_lista = ["a", "b", "c", "b", "d", "m", "n", "n"]
#============================
# ----------- SET -----------
# Construye una colección 
# desordenada de elementos 
# únicos.
#===========================
duplicados = set([x for x in una_lista if una_lista.count(x) > 1])
print(duplicados)

# Expresión generadora
cuadrados = (x*x for x in range (5))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))

# Pasar una función generadora
import math 
print(sum(x*x for x in range(5)))

# Lista de comprehesión pasada com función 
numeros_pares = [x for x in range(21) if x%2 == 0]
print([x for x in range (21) if x%2 == 0])
print(numeros_pares)

#====================================
#       FIN DE LA PRÁCTICA
#====================================