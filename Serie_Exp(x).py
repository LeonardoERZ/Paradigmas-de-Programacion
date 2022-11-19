#=======================================
#       Algoritmo 1
#=======================================
#   Serie exponencial 
#   Factorización de x
#   Negativos con función inversa
#========================================
from os import system
#system("cls")    # Para Windows
#system("clear") # Para Ubuntu
n = 200          # valor de n en la suma 
x = 2.0          # valor de x en exp(x)
flag = False
if x<0:
    flag = True
    x = -x
s = 1.0
for i in range(n,0,-1):
    s *= x/float(i)
    s += 1.0
if flag == True:
    s = 1/s
print(s)
