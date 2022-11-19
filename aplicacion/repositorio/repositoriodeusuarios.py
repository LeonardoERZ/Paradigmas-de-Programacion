#===============================================
# --------- Módulo para varios Módulos --------
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

#===============================
# Este objeto es una interface 
#===============================
class RepositorioDeUsuarios:
    
    def abrir(mi) -> None:
        pass
    
    def guardar(mi, usuario: Usuario) -> None:
        pass
    
    def cerrar(mi) -> None:
        pass

#=====================================
#           FIN DEL MÓDULO 
#=====================================
