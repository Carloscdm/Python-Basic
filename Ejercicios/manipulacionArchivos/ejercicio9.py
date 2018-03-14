'''
Created on 14 mar. 2018

@author: diago
'''
# ‐*‐ coding: utf‐8 ‐*‐

archivo_texto = open("archivo.txt", "r")
archivo = archivo_texto.readlines()

for i in range(len(archivo)):
    print (i+1), archivo[i]