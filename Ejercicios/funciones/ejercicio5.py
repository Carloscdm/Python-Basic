'''
Created on 14 mar. 2018

@author: diago
'''
""" Funcion que calcula el factorial de un numero """

def factorial(n):
    """ Calcula n! """
    
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print (factorial(13))
