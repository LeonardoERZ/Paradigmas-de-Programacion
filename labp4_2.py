#===============================================
# Práctica 4 Parte 2 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#======================================
# La clase A tiene tres números reales
#======================================
class A:
    __a:float=0.0
    __b:float=0.0
    __c:float=0.0 # se declaara así la variable para indicar que es una 
                  # variable que queremos que se encapsule

    def __init__(self,a:float,b:float,c:float):
        self.a = a
        self.b = b
        self.c = c

#======================================
# La clase B tiene dos números reales
#======================================
class B:
    __d:float=0.0
    __e:float=0.0

    def __init__(self,d:float,e:float):
        self.d = d
        self.e = e
        # Obs: Primero se declara un objeto para ocuparlo en otro objeto
        # Ejm: Primero declaras las llantas y después el carro, no al revés

    #========================================
    # Método sumar todo (internos + externos)
    #========================================
    def sumar_todo(self,aa:float,bb:float):
        x:float=self.d+self.e+aa+bb
        return x

#============
# ASOCIACIÓN  (Pasarle los valores un objeto a otro)
#============
# Usando objetos independientes
objetoA = A(1.0,2.0,3.0)
objetoB = B(4.0,5.0)
print(objetoB.sumar_todo(objetoA.a,objetoA.b))

#============================================
# El objeto C tiene dos reales y un objeto A
# El objeto A se instancia dentro de C
#============================================
class C: 
    __d:float=0.0
    __e:float=0.0
    __Aa:A=None

    def __init__(self,d:float,e:float):
        self.d = d
        self.e = e
        # A está instanciado adentro
        self.Aa = A(1.0,2.0,3.0)

    def sumar_todo(self):
        x:float=self.d+self.e+self.Aa.a+self.Aa.b
        return x

#============================
# COMPOSICIÓN
# Contiene otro objeto dentro  (un objeto dentro de otro objeto)
#============================
objetoC = C(4.0,5.0)
print(objetoC.sumar_todo())

#===========================================
# Objeto D tiene dos reales y  un objeto A 
# definido por fuera
#===========================================
class D: 
    __d:float = 0.0
    __e:float = 0.0
    __Aa: A = None

    def __init__(self,d:float,e:float,Aa:A):
        self.d = d
        self.e = e 
        self.Aa = Aa 

    def sumar_todo(self):
        x:float = self.d+self.e+self.Aa.a+self.Aa.b
        return x 

#========================================
# AGREGACIÓN
# Construye el objeto agregado por fuera 
#========================================
objetoD = D(4.0,5.0,objetoA)
print(objetoD.sumar_todo())

#=====================================
#       FIN DE LA PRÁCTICA
#=====================================