'''
Created on 14 mar. 2018

@author: diago
'''
""" Calcula el producto de los numeros de la antepenultima linea
    de 'datos_ficheros' """

fd = open("datos_ficheros", "r")
antepenultima = fd.readlines()[-3]
fd.close()

numeros = [int(x) for x in antepenultima.split()]
total = 1
for i in numeros:
    total *= i
print("antepenultima linea:",antepenultima)
print ("Producto antepenultima linea:", total)