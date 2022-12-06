#===============================================
# Práctica 7 Parte 2 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#====================
# Función pura x**2
#====================
def alcuadrado(x):
    return x*x

#====================
# Función pura x**3
#====================
def alcubo(x):
    return x*x*x 

#===========================
# Mapeo de una función pura
#===========================
def mapeo(func,lista_numeros):
    resultado = []

    for i in lista_numeros:
        resultado.append(func(i))
    return resultado

cuadrados = mapeo(alcuadrado,[2.5,2,3.8,1.2,6.6,1j,7,8])
cubos = mapeo(alcubo,[1,2,3,4,5,6,7,8])
print(cuadrados)
print(cubos)

#===============================
# Funciones dentro de funciones
#===============================
def en_mayusculas(texto):
    return texto.upper()

def en_minusculas(texto):
    return texto.lower()

def saludar(func):
    saludo = func("Hola, ¿qué tal?")
    print(saludo)

#================
# Con strings
#================
saludar(en_mayusculas)
saludar(en_minusculas)

#==========================================
# Funciones abstractas dentro de funciones
#==========================================
def divisor(x):
    def dividendo(y):
        return y/x
    return dividendo 

#===================================
# Primero generamos la función y/2
#===================================
división = divisor(2)
#===================================
# La usamos para calcular 3/2
#===================================
print(división(3))

#=====================================
# Uso de la función map con una lista
#=====================================

#======================================
# Lista de ciudades y su temperatura
#======================================
temps = [ ("Berlin", 29),
          ("Cairo", 36),
          ("Buenos Aires", 19),
          ("Los Angeles", 26),
          ("Tokyo", 27),
          ("Nueva York", 28),
          ("Londres", 22),
          ("Pekín", 32),
          ("México Tenochtitlan", 23)
        ]
#==============================================================
# ----------------------- Análisis ----------------------------
# datos[0] := es la posición del nombre de los paises
# datos[1] := es la posición del valor numerico de Temperatura
#===============================================================

C_a_F = lambda datos: (datos[0], (9/5)*datos[1] + 32)

#==============================================================
# Si quisiera ver la temperatura en °C y °F a la vez, se vería
# así la instrucción C_a_F:
#==============================================================
#C_a_F = lambda datos: (datos[0], datos[1], (9/5)*datos[1] + 32)

print(list(map(C_a_F,temps)))

#====================================
#       FIN DE LA PRÁCTICA
#====================================