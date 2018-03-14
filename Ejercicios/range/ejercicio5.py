'''
Created on 14 mar. 2018

@author: diago

Resultado:
La lista quedaría así: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
# ‐*‐ coding: utf‐8 ‐*‐

lista = list()

for i in range(0, 11):
    lista.append(i**2)

print ("La lista quedaría así: " + str(lista))