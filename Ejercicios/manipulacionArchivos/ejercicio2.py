'''
Created on 14 mar. 2018

@author: diago
'''
""" Determina el numero de lineas de 'datos_ficheros' """

fd = open("datos_ficheros", "r")
nlineas = 0
for linea in fd:
    nlineas += 1
fd.close()
print ("Numero de lineas:", nlineas)