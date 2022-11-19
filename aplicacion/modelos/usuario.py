#===============================================
# --- Módulo para labp5_interfaces.py y más ---
# Práctica 5 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#================
# Clase Usuario 
#================
class Usuario:
    __nombre: str
    __apellido: str
    __edad: int
    
    #==============
    # Constructor 
    #==============
    def __init__(mi, nombre:str, apellido:str, edad:int):
        mi.__nombre = nombre
        mi.__apellido = apellido
        mi.__edad = edad

    #==========
    # Getters 
    #==========
    def getNombre(mi) -> str:
        return mi.__nombre

    def getApellido(mi) -> str:
        return mi.__apellido

    def getEdad(mi) -> str:
        return mi.__edad

#=====================================
#           FIN DEL MÓDULO 
#=====================================