'''
Created on 14 mar. 2018

@author: diago
'''
""" Determina la longitud de la primera linea de 'datos_ficheros' """

fd = open("datos_ficheros", "r")
linea = fd.readline()
fd.close()
print ("Primera linea:", len(linea), "caracteres")