#===============================================
# Práctica 8 Parte 4 Paradigmas de Programación
# Autor:     Rivera Zacarias Leonardo Enrique
# Grupo:     2AV1
# Profesor:  Dr. Julian Tercero Becerra Sagredo
#===============================================

#====================
# Modulos a utilizar
#====================
import random
import matplotlib.pyplot as plt       # biblioteca para graficar 
import matplotlib.patches as patches

#==============================
# Definimos la clase Particula
#==============================
class Particula():
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

#==============================
# Definimos la clase Nodo
#==============================
class Nodo():
    def __init__(self, x0:float, y0:float, w:float, h:float, particula):
        self.x0 = x0
        self.y0 = y0
        self.ancho = w
        self.alto = h
        self.particulas = particula
        self.hijos = []

    def get_ancho(self):
        return self.alto

    def get_particulas(self):
        return self.particulas

#===============================
# Funcion para elegir el área de
# las particulas
#================================
def subdivision_recursiva(nodo:Nodo, k:int):
    if len(nodo.particulas) <= k:
        return

    w__ = float(0.5*nodo.ancho)
    h__ = float(0.5*nodo.alto) 

    p = cuantas_contiene(nodo.x0, nodo.y0, w__, h__, nodo.particulas)
    nodo.x1 = Nodo(nodo.x0, nodo.y0, w__, h__, p)
    subdivision_recursiva(nodo.x1, k)

    p = cuantas_contiene(nodo.x0, nodo.y0+h__, w__, h__, nodo.particulas)
    nodo.x2 = Nodo(nodo.x0, nodo.y0+h__, w__, h__, p)
    subdivision_recursiva(nodo.x2, k) 

    p = cuantas_contiene(nodo.x0+w__, nodo.y0, w__, h__, nodo.particulas)
    nodo.x3 = Nodo(nodo.x0 + w__, nodo.y0, w__, h__, p)
    subdivision_recursiva(nodo.x3, k) 

    p = cuantas_contiene(nodo.x0+w__, nodo.y0+h__, w__, h__, nodo.particulas)
    nodo.x4 = Nodo(nodo.x0+w__, nodo.y0+h__, w__, h__, p)
    subdivision_recursiva(nodo.x4, k)

    nodo.hijos = [nodo.x1, nodo.x2, nodo.x3, nodo.x4]

#===============================
# Funciones para las particulas
#===============================
def cuantas_contiene(x:float, y:float, w:float, h:float, particulas):
    pts = []
    for particula in particulas:
        if particula.x >= x and particula.x <= x+w and particula.y >= y and particula.y <= y+h:
            pts.append(particula)
    return pts

def encontrar_hijos(nodo):
    if not nodo.hijos:
        return[nodo]
    else:
        hijos = []
        for hijo in nodo.hijos:
            hijos += (encontrar_hijos(hijo)) 
    return hijos

#===========================
# Definimos la clase Qtree
#===========================
class QTree():
    def __init__(self, k:int, n:int):
        self.umbral = k
        self.particulas = [Particula(random.uniform(0,10), random.uniform(0, 10)) for x in range(n)]
        self.root = Nodo(0, 0, 10, 10, self.particulas)

    def add_particulas(self, x:float, y:float):
        self.particulas.append(Particula(x,y))

    def get_particulas(self):
        return self.particulas

    def subdividir(self):
        subdivision_recursiva(self.root, self.umbral)

    def visualizacion(self):
        fig = plt.figure(figsize=(12, 8)) 
        plt.title("Quadtree")
        c = encontrar_hijos(self.root)
        print("Número de segmentos: %d" %len(c)) 
        areas = set()
        for el in c: 
            areas.add(el.ancho*el.ancho)
        print("Mínima área por segmento: %.3f units" %min(areas))
        for n in c: 
            plt.gcf().gca().add_patch(patches.Rectangle((n.x0, n.y0), n.ancho, n.alto, fill = False))
        x = [particula.x for particula in self.particulas]
        y = [particula.y for particula in self.particulas]
        plt.plot(x,y,'ro') # muestra las partículas como puntos rojos 
        plt.show()
        return

#======================
# Imprimimos el QTree
#======================
qtree = QTree(2,200)
qtree.subdividir()
qtree.visualizacion()

#====================================
#       FIN DE LA PRÁCTICA
#====================================