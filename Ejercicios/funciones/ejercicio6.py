'''
Created on 14 mar. 2018

@author: diago
'''
""" Funcion que recibe un numero y devuelve una lista con todos sus divisores """

def divisores(n):
    """ Devuelve los divisores de  n """
    
    lista_divisores = []
    for divisor in range(1, n + 1):
        if n % divisor == 0:
            lista_divisores.append(divisor)
    return lista_divisores
    
print (divisores(22))