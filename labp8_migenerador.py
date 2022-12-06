#===============================================
# Práctica 8 Parte 1 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#=============================================
# -------------- Generadores -----------------
# Permiten extraer valores de una función y 
# almacenarlo (de uno en uno) en objetos 
# iterables (que se pueden recorrer), sin la
# necesidad de almacenar TODOS A LA VEZ en
# la memoria RAM.
#=============================================
def migenerador():
    print("Primero")
    #============================
    # ---------- Yield ----------  (ceder / producir )
    # Genera un objeto iterable.
    #============================
    yield 10
    print("Segundo")
    yield 20
    print("Tercero")
    yield 30

gen = migenerador()
#===========================
# ---------- Next ----------
# Nos retorna el siguiente 
# elemento de un objeto 
# iterable.
#===========================
val1 = next(gen)
print(val1)
val2 = next(gen)
print(val2)
val3 = next(gen)
print(val3)

#==========================================================================================
# ---------------------------- Ventajas de utilizar generadores ---------------------------
# 1) Son más eficientes que las funciones tradicionales.
# 2) Muy útiles con listas de valores infinitos. 
# 3) Entre llamada y llamada, el objeto iterable entra en un estado de pausa(suspensión).
# =========================================================================================

#====================================
#       FIN DE LA PRÁCTICA
#====================================