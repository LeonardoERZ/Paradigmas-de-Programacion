#===============================================
# Práctica 7 Parte 4 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#=================
# Uso de filtros
#=================

#========================================================
# Hacer una lista de los números por arriba del promedio
#========================================================

# Módulo de estadística 
import statistics

bigdata = [1.3,2.7,0.8,4.1,4.3,-0.1]
promedio = statistics.mean(bigdata)
print(promedio)

#===================================================================
# Hazme una lista de elementos que cumplan la condicion x >promedio
# filter( condición, datos )
#===================================================================
print(list(filter(lambda x: x > promedio, bigdata)))

#====================
# Limpiar los datos 
#====================
paises = [
            "",
            "Argentina",
            "",
            "Brasil",
            "",
            "Chile",
            "México",
            "",
            "Colombia",
            "",
            "",
            "Cuba",
            "Venezuela"
        ]

#=================================
# Filtra lo que no contiene nada 
#=================================
print(list(filter(None, paises)))

#====================================
#       FIN DE LA PRÁCTICA
#====================================