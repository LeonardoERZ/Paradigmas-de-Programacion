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

#================================================
# Implementa la interface RepositorioDeUsuarios 
#================================================
class SistemaDeArchivos(RepositorioDeUsuarios):
	__directorio: str

	def __init__(mi, directorio: str):
		mi.__directorio = directorio
	
	def abrir(mi) -> None:
		print(f"Abrir directorio: {mi.__directorio}")

	def guardar(mi, usuario:Usuario) -> None:
		xml = f"</root></name>{usuario.getNombre()}</name></lastName>{usuario.getApellido()}</lastName></age>{usuario.getEdad()}</age></root>"
		print(f"Guardando usuario en el archivo: {mi.__directorio}/{usuario.getNombre()}")
		print(xml)

	def cerrar(mi) -> None:
		print("Cerrando el archivo")

#=====================================
#           FIN DEL MÓDULO 
#=====================================