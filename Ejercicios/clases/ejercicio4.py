'''
Created on 14 mar. 2018

@author: diago

Cree una clase llamada Punto. Tendra como atributos las 
coordenadas x0 e y0 del origen (0, 0) por defecto, y las coordenadas x e y 
del punto en cuestion.

Los metodos seran: 
distancia y muestra_punto. El primero devolvera la 
distancia del punto a su origen. El segundo imprimira por pantalla el mensaje 
de texto: (x,y), donde x e y son las coordenadas del punto.

Ejecute un programa que cree dos puntos con origen en (0,0) y muestre por 
pantalla el que tenga una distancia menor al centro:
distancia = math.sqrt ((x-x0)**2 + (y-y0)**2)

'''

import math

class Punto (object):
    def __init__ (self, x, y, x0=0, y0=0):
        self.x = x
        self.y = y
        self.x0 = x0
        self.y0 = y0
    
    def distancia (self):
        'Devuelve la distancia euclidea entre el punto y su origen de coordenadas'
        return math.sqrt ((self.x - self.x0)**2 + (self.y - self.y0)**2)
    
    def muestra_punto (self):
        print ('(%(x)f, %(y)f)' % {'x': self.x, 'y': self.y})

if __name__ == '__main__':
    punto1 = Punto (2, 2)
    punto2 = Punto (0, 3)
    min_dist = punto1.distancia ()
    cercano = punto1
    if min_dist > punto2.distancia ():
        min_dist = punto2.distancia () 
        cercano = punto2
    print ('Punto mas cercano = ',) 
    cercano.muestra_punto ()
    print ('Distancia = ', min_dist)