#===============================================
# ------ Módulo para labp5_interfaces.py -------
# Práctica 5 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#===========================================================================
# Del directorio aplicacion, el subdirectorio modelos,
# el archivo usuario.py: trae el objeto Usuario
#===========================================================================
from aplicacion.modelos.usuario import Usuario

#=============================================================================
# Del directorio aplicacion, el subdirectorio repositorio,
# el archivo repositoriodeusuarios.py : trae el objeto RepositorioDeUsuarios
#=============================================================================
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#====================================================
# Para llenar la interface hay que heredar la clase 
#====================================================
class BaseDeDatos(RepositorioDeUsuarios):
    __host: str
    __user: str
    __password: str

    def __init__(mi, host: str, user: str, password: str):
        mi.__host = host
        mi.__user = user
        mi.__password = password
    
    def abrir(mi) -> None:
        print(f"Abriendo la conexión a la base de datos: {mi.__host}:{mi.__user}@{mi.__password}")

    def guardar(mi, usuario:Usuario) -> None:
        userElements = {
            "nombre": usuario.getNombre(),
            "apellido": usuario.getApellido(),
            "edad": usuario.getEdad()
        }
        print(f"Guardando el usuario en la base de datos {usuario.getNombre()}\n")
        print(f"INSERTAR DATOS DEL USUARIO ('{userElements['nombre']}','{userElements['apellido']},'{userElements['edad']}')")
    
    def cerrar(mi) -> None:
        print("Cerrando la conexión")

#=====================================
#           FIN DEL MÓDULO 
#=====================================