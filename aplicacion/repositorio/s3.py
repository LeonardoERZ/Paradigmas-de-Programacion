#===============================================
# ------ Módulo para labp5_interfaces.py -------
# Práctica 5 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#=============================================================================
# Del directorio aplicacion, el subdirectorio repositorio,
# el archivo repositoriodeusuarios.py : trae el objeto RepositorioDeUsuarios
#=============================================================================
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#===========================================================================
# Del directorio aplicacion, el subdirectorio modelos,
# el archivo usuario.py: trae el objeto Usuario
#===========================================================================
from aplicacion.modelos.usuario import Usuario

#======================================
# S3 es hijo de RepositorioDeUsuarios 
#======================================
class S3(RepositorioDeUsuarios):
    __clientId: str
    __secretKey: str
    __bucket: str
    
    def __init__(mi, clientId:str, secretKey:str, bucket:str):
        mi.__clientId = clientId
        mi.__secretKey = secretKey
        mi.__bucket = bucket

    def abrir(mi) -> None:
        print(f"Estableciendo conexión a AWS S3 {mi.__clientId}: {mi.__secretKey}")

    def guardar(mi, usuario:Usuario) -> None:
        usrData = {
            "nombre": usuario.getNombre(),
            "apellido": usuario.getApellido(),
            "edad": usuario.getEdad()
        }
        print(f"Guardando usuario de la bandeja: {mi.__bucket}: {usrData}") 
    
    def cerrar(mi) -> None:
        print("Cerrando conexión AWS S3")

#=====================================
#           FIN DEL MÓDULO 
#=====================================