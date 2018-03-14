'''
Created on 14 mar. 2018

@author: diago
'''
""" Imprime por pantalla las primeras 15 potencias de dos """

for exponente in range(0, 15):
    print (2 ** exponente)


# Reutilizando la potencia anterior...
n = 1
for iteracion in range(15):
    print (n)
    n = n * 2