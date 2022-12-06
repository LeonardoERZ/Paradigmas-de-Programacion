#===============================================
# Práctica 7 Parte 3 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#==========================================
# Uso de reducciones (colapsar resultados)
#==========================================

#===================================================
# Multiplicación de todos los números de la lista
#===================================================
from functools import reduce

bigdata = [2,3,5,7,11,13,17,19,23,29]

#==============
# Funcion x*y
#==============
multiplicar = lambda x,y: x*y 

x = print(reduce(multiplicar,bigdata))

#============================================================
# Reduce le aplica la función por pares a los resultados y 
# el siguiente elemento comenzando con los dos primeros 
# elementos
#============================================================

# Propuesta de análisis y síntesis 
def observa_reduce(a:float, b:float):
    result = a*b
    print(f"{a} * {b} = {result}")
    return result
    
print("La justificación es la siguiente: ")
reduce(observa_reduce,bigdata)

#====================================
#       FIN DE LA PRÁCTICA
#====================================