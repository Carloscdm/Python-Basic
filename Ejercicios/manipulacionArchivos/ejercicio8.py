'''
Created on 14 mar. 2018

@author: diago
'''
""" Contar el numero de lineas del fichero si ignoramos aquellas
comentadas (es decir, que empiezan por #) """

fd = open("datos_ficheros", "r")

total = 0
for linea in fd:
    if not linea.strip().startswith("#"):
        total += 1

fd.close()
print ("Hay", total, "lineas no comentadas")