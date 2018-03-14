'''
Created on 14 mar. 2018

@author: diago
'''
# ‐*‐ coding: utf‐8 ‐*‐

archivo_texto = open("archivo.txt", "r")
lineas_texto = archivo_texto.readlines()
archivo_texto.close()

print (lineas_texto)
print (lineas_texto[0])
print (lineas_texto[1])