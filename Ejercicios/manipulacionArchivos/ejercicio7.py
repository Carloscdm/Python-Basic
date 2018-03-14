'''
Created on 14 mar. 2018

@author: diago
'''
""" La suma de todos los numeros impares del documento """

fd = open("datos_ficheros", "r")

total = 0
for linea in fd:
    for n in linea.split():
        numero = int(n)
        if numero % 2 != 0:
            total += numero
fd.close()

print ("Suma de los numeros impares:", total)