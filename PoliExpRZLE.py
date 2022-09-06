#======================================================
# Codigo 2 Práctica 2 Paradigmas de Programación
# Autor:    Rivera Zacarias Leonardo Enrique 
# Grupo:    2AV1
# Profesor: Dr. Julian Tercero Becerra Sagredo
#======================================================
from os import system
#system("cls")   # Para Windows
system("clear") # Para Ubuntu
print("Programa que calcula el valor de la "\
       "función exp(x) en su forma polinomial")
n = int(input("¿Hasta que valor llega la suma?: ")) 
x = int(input("Ingresa el valor del exponente: "))  # e^x
suma = 0                                            # Suma del polinomio
for i in range(0,n+1,1):
    num = x**i                                      # x^0,x^1,x^2,...,x^n
    fact = 1
    if i>1:                                         #Realizamos el factorial para i>=2
        j = 1
        while j<=i:
            fact *= j                               # Calculamos 2!,3!,...,n! 
            j+=1
    suma = suma+num/fact                            # Realizamos la suma
print(f"El valor de exp({x}) con redondeo es de",round(suma,5))
print(f"El valor de exp({x}) sin redondeo es de",suma)
print("FIN DEL PROGRAMA")

'''
    Observaciones: 
Para exp(1): n = 17
Para exp(2): n = 22
Para exp(3): n = 26
Para exp(4): n = 28

Los valores con rendondeo fueron comparados con la funcion exp() de MATLAB
Los valores sin rendondeo fueron comparados con la funcion math.exp() de python
'''