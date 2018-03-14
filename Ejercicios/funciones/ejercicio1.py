'''
Created on 14 mar. 2018

@author: diago
'''
""" Funcion que recibe una lista de enteros y devuelve la suma de todos sus
    elementos. Hay que implementarlo sin utilizar sum(), claro esta """

def suma_todos(enteros):
    """ Suma todos los numeros de la lista """
    
    total = 0
    for numero in enteros:
        total = total + numero
    return total

print (suma_todos(range(10)))


