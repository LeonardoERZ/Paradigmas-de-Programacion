#===============================================
# Práctica 8 Parte 3 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#=================================================
# Gráficos usando la tortuga que pinta al caminar
#=================================================
import turtle
import time
tortuga = turtle.Turtle()
print(tortuga.position())   # Saber la posición de la tortuga
tortuga.shape("turtle")     # La figura a mostrar en pantalla sea una tortuga 
tortuga.left(90)            # Giro a la izquierda de 90 grados
#================================
# Velocidad de la tortuga
#================================
"""
 - El rango puede ser entre 0-10.
 - Si la entrada es un número mayor que 10 o menor que 0.5, la velocidad se establece en 0.
 - Las cadenas de velocidad se asignan a los valores de velocidad de la siguiente manera:
    
    Caso I:   más rápido: 0

    Caso II:  rápido: 10

    Caso III: normal: 6

    Caso IV:  lento: 3

    Caso V:   más lento: 1

 - Las velocidades de 1 a 10 refuerzan la animación cada vez más rápida del dibujo de líneas 
   y del giro de la tortuga.

 - Si velocidad = 0 significa que no se produce ninguna animación. adelante/atrás hace que la 
   tortuga salte y del mismo modo izquierda/derecha hace que la tortuga gire instantáneamente.
"""
tortuga.speed(500)         # Velocidad de la tortuga
#tortuga.speed(6)            # Velocidad normal
#tortuga.speed(0)            # Velocidad más rapida (es igual a la de 500)
time.sleep(5)               # Damos 5 segundos para asegurarnos que nos muestre la pantalla con la tortuga

#===================================
# Con ángulos de 90 es un árbol H
#===================================
angulo:float = 90

#======================================
# El árbol se construye recursivamente
#======================================
def arbol(i:float,angulo:float):
    if i<10.0:
        return
    else:
        tortuga.forward(i)        # Camina i
        tortuga.left(angulo)      # Gira a la izquierda 90 grados 
        arbol(3.0*i/4.25,angulo)  # Pide otro arbol y cambia la longitud del paso
        tortuga.right(2*angulo)   # Gira a la derecha 180 grados 
        arbol(3.0*i/4.25,angulo)  # Pide otro arbol y cambia la longitud del paso
        tortuga.left(angulo)      # Gira a la izquierda 90 grados 
        tortuga.backward(i)

arbol(100,angulo)                 # i es la recursividad 
turtle.exitonclick()              # Sse cierra la ventana hasta que demos click

#====================================
#       FIN DE LA PRÁCTICA
#====================================

