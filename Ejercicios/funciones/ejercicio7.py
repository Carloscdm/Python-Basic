'''
Created on 14 mar. 2018

@author: diago
'''
""" Funcion que determina si un numero es primo o no (devuelve True o False) """

# Del ejercicio anterior (func-07.py)
def divisores(n):
    """ Devuelve los divisores de  n """
    
    lista_divisores = []
    for divisor in range(1, n + 1):
        if n % divisor == 0:
            lista_divisores.append(divisor)
    return lista_divisores
    
def es_primo(n):

    # Si es primo solo sera divisible entre 1 y si mismo
    return len(divisores(n)) == 2

print (es_primo(13))