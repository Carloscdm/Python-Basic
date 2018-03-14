'''
Created on 14 mar. 2018

@author: diago
'''
# ‐*‐ coding: utf‐8 ‐*‐

archivo_texto = open("archivo.txt", "r")

archivo_texto.seek(5)
print (archivo_texto.read())

archivo_texto.seek(0)
print (archivo_texto.read())