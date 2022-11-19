#===============================================
# Práctica 6 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#==================================================================
# Del directorio aplicacion, el subdirectorio banco, 
# el archivo cliente_bancario.py : trae el objeto ClienteBancario
#==================================================================
from aplicacion.banco.cliente_bancario import ClienteBancario

#=============================================
# try: intenta (correr las instrucciones)    
# except: atrapar el error en una variable e 
# e se puede convertir a String              
#=============================================
try:
    cliente = ClienteBancario("Jaime Andrade", "Hernández Sánchez", 28, 0.0)
    cliente.guardarDinero(300)
    print(cliente)
    cliente.retirarDinero(400)
    print(cliente)
#==============================================
# Exception es el objeto más general de error 
#==============================================
except Exception as e:
    print("Error PDEH "+str(e))

#=====================================
# Error por usar un atributo privado 
#=====================================
try:
    print(cliente.__nombres)
except Exception as ex:
    print("Error PDEH "+str(ex))

#=================
# Forma correcta 
#=================
print(cliente.nombres)

#====================================
#       FIN DE LA PRÁCTICA
#====================================