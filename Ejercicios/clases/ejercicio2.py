
'''
Created on 14 mar. 2018

@author: diago

Cree una clase llamada Fichero. Esa clase tendra un atributo 
llamado ruta y otro llamado texto.
Implemente dos metodos:
   - leer_fichero, que leera el fichero dado por el atributo ruta y 
   guardara su contenido en el atributo texto.
   - mostrar_fichero, que imprimira por pantalla el texto del fichero leido.
Use su nueva clase para leer el fichero que contiene al ejercicio 1.
'''

import sys

class Fichero (object):
    def __init__ (self, ruta_fichero):
        self.ruta = ruta_fichero
        self.texto = ''
    
    def leer_fichero (self):
        'Lee el fichero dado por ruta.'
        try:
            self.texto = open (self.ruta).read ()
        except IOError:
            print ('ERROR: No puedo abrir el fichero ', self.ruta)
#        return self.texto
    
    def mostrar_fichero (self):
        print (self.texto)
    
if __name__ == '__main__':
    print("-----")
    lugar = 'ejercicio1.py'    
    if len (sys.argv) > 1: # hemos pasado la ruta del fichero al script
        lugar = sys.argv [1]
    objeto = Fichero (lugar)
#    print objeto.leer_fichero ()
    objeto.leer_fichero ()
    objeto.mostrar_fichero ()