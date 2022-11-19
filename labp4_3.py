#===============================================
# Práctica 4 Parte 3 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#=======================
# Clase computadora 
#=======================
class Computadora:
    marca: str = None 
    capacidad: int = 0
    ram: int = 0

    #===========================
    # Constructor
    #===========================
    def __init__(self, marca:str, capacidad:int, ram:int):
        print(f"Accediendo al constructor de la pc: {marca}")
        self.marca = marca
        self.capacidad = capacidad
        self.ram = ram
    
    def imprimirInfoPC(self):
        print(f"Esta es la computadora marca: {self.marca} con almacenamiento de {self.capacidad} y memoria de {self.ram} GB")

    #============================
    # Destructor 
    #============================
    def __del__(self):
        print(f"se eliminó la computadora: {self.marca}")

#=========================
# Objeto persona
#=========================
class Persona: 
    nombres: str = None
    apellidos: str = None
    edad: int = 0
    direccion: str = None
    computadora: Computadora = None

    #================================
    # Constructor de persona
    #================================
    def __init__(self, nombres:str, apellidos:str, edad:int, direccion:str, marca:str, capacidad:int, ram:int):
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.direccion = direccion
        self.Computadora = Computadora(marca, capacidad, ram)
        print(f"--- Accedimos al constructor de la persona: {nombres} {apellidos}")

    def imprimirInfo(self) -> None:
        print(f"--- Mi nombre es {self.nombres} {self.apellidos}, tengo {self.edad} años de edad, vivo en {self.direccion} ")
        self.Computadora.imprimirInfoPC()
    
    #======================
    # Destructor
    #======================
    def __del__(self):
        print(f"--- Eliminamos el objeto... {self.nombres} {self.apellidos}")

#========================================
#   Funcion 1 es el programa 
#========================================
def funcion1():
    persona = Persona("Carlos", "Perez", 40, "Xochimilco", "Lenovo", 700, 8)
    print("\n")
    persona.imprimirInfo()
    print("\n")
    persona2 = Persona("Magdalena", "Carrillo", 35, "Jalapa", "IBM", 200, 4)
    print("\n")
    persona2.imprimirInfo()
    print("\n")

#============================
# Llamar a funcion 1
#============================
funcion1()

#=====================================
#       FIN DE LA PRÁCTICA
#=====================================