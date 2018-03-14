'''
Created on 14 mar. 2018

@author: diago
'''
"""Modulo Operaciones_basicas."""

def sumar (op1, op2):
    """Funcion que suma los dos parametros y devuelve el resultado."""
    return op1 + op2

def restar (op1, op2):
    """Funcion que resta los dos parametros y devuelve el resultado."""
    return op1 - op2

def multiplicar (op1, op2):
    """Funcion que multiplica los dos parametros y devuelve el resultado."""
    return op1 * op2

def dividir (op1, op2):
    """Funcion que divide los dos parametros y devuelve el resultado."""
    try:
        resultado = op1 / op2
    except ZeroDivisionError:
        print ('ERROR: No se puede dividir por cero')
        return -1
    return resultado