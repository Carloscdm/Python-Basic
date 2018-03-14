'''
Created on 14 mar. 2018

@author: diago
'''
def suma(lista):
    """ Devuelve la suma de todos los elementos de la lista, o
        None en caso de que uno o mas de ellos no puedan sumarse """

    try:
        return sum(lista)
    except TypeError:
        return None

a_sumar = [1, 4, 5, 3.2, 4.4, "2,3", 3.5]
b_sumar = [1,4,5]
print (suma(a_sumar))
print (suma(b_sumar))