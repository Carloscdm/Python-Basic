'''
Created on 14 mar. 2018

@author: diago
'''
""" Determina el numero de numeros que contiene la primera
    linea de 'datos_ficheros' """

fd = open("datos_ficheros", "r")
linea = fd.readline()
fd.close()
numeros = linea.split()
print ("En la primera linea hay:", len(numeros), "enteros")