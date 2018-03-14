'''
Created on 14 mar. 2018

@author: diago
'''
# -*- coding: utf-8 -*-

"""
Cree una clase llamada Persona. Contendra el nombre, DNI, 
direccion, telefono y e-mail (este ultimo opcional) de un individuo.

Por metodo tendra mostrar que imprimira por pantalla los datos de la persona. 
Utilice esa clase para crear una lista de personas y mostrar cada una de ellas.
 
Los datos de cada persona estan en el fichero personas.txt. El formato de este 
fichero es una linea con los datos de cada persona. Estan separados por ';'. 
Contiene informacion por este orden:
nombre;DNI;direccion;telefono;e-mail;saldo

"""

import sys

class Persona (object):
    def __init__ (self, nombrep, DNIp, direccionp, telefonop, emailp = '' ):
        self.nombre = nombrep
        self.dni = DNIp
        self.direccion = direccionp
        self.telefono = telefonop
        self.email = emailp
    
    def mostrar (self):
        print ('Nombre = ', self.nombre)
        print ('DNI = ', self.dni)
        print ('Direccion = ', self.direccion)
        print ('Telefono = ', self.telefono)
        print ('E-mail = ', self.email)

if __name__ == '__main__':
    fichero = 'personas.txt'
    #opcionalmente, podemos pasar la ruta al fichero cuando ejecutemos el programa    
    if len (sys.argv) > 1: 
        fichero = sys.argv [1]
    
    lineas = list ()

    try:
        lineas = open (fichero).read ().split ('\n')
    except IOError:
        print ('ERROR: No se pudo abrir el fichero ', fichero)
    
    # Creo la lista de Personas
    lista_personas = list ()
    
    #proceso cada linea del fichero
    for l in lineas:
        if len (l) < 10:
            continue
        datos = l.split(';') [:-1] # el ultimo dato (saldo) no me interesa
        p = Persona (datos [0], datos [1], datos [2], datos [3], datos [4])        
        lista_personas.append (p)
    
    #ahora, muestro la lista de personas
    for p in lista_personas: # itero por cada elemento de la lista
        p.mostrar ()
        print ('-' * 70)