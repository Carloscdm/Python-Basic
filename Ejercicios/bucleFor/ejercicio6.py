'''
Created on 14 mar. 2018

@author: diago
'''
""" A partir de dos listas de enteros, 'numeros1' y 'numeros2' de igual tamano,
    generar otra cuyo primer elemento es el producto del primer elemento de
    las listas 'numeros1' y 'numeros2', y asi sucesivamente. """


numeros1 = [1, 7, 13, 21, 27]
numeros2 = [4, 6, 10, 18, 23]

resultado = []
for index in range(len(numeros1)):
    resultado.append(numeros1[index] * numeros2[index])
print (resultado)


#  Mucho mejor asi
resultado = []
for x, y in zip(numeros1, numeros2):
    resultado.append(x * y)