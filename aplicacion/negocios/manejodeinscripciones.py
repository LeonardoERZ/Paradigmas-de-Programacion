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

#=======================
#  Clase storemanager  
# ¡NO TIENE VARIABLES! 
#=======================
class ManejoDeInscripciones:
    #=================================================================
    # Decorador staticmethod                     
    # El objeto sólo tiene la función inscribirUsuario        
    # ENVUELVE LA FUNCIÓN SIN LLAMAR VARIABLES LOCALES        
    # el objeto ManejoDeInscripciones contiene la interface intercambiable
    # 
    # ------------------- Mis Observaciones ----------------------------
    # Cuando necesitamos alguna funcionalidad no con un objeto sino con 
    # la clase completa, hacemos que un método sea estático.
    #
    # No necesita acceder a ninguna propiedad de sí mismo y solo requiere 
    # los parámetros a utilizar.
    #
    # Los métodos estáticos no pueden modificar el estado de un objeto, 
    # ya que no están vinculados a él.
    #==================================================================
    @staticmethod
    def inscribirUsuario(usuario:Usuario, repositoriodeusuarios: RepositorioDeUsuarios) -> None:
        print("----------> Guardando usuario...\n")
        repositoriodeusuarios.abrir()
        repositoriodeusuarios.guardar(usuario)
        repositoriodeusuarios.cerrar()

#=====================================
#           FIN DEL MÓDULO 
#=====================================