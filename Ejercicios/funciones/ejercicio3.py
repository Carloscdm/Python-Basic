'''
Created on 14 mar. 2018

@author: diago
'''
""" Funcion que recibe una lista de enteros y devuelve otra lista con aquellos
    que son pares y >= 113 """

def pares_y_mayores_113(enteros):
    """ Devuelve lista con los numeros pares y >= 113 """
    
    seleccionados = []
    for numero in enteros:
        if numero % 2 == 0 and numero >= 113:
            seleccionados.append(numero)
    return seleccionados

numeros = [5, 28, 675, 113, 45, 676, 89, 12, -213, 232, 39, 42, 877]
print (pares_y_mayores_113(numeros))
