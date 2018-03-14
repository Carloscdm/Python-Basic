'''
Created on 14 mar. 2018

@author: diago

Funcion que recibe dos enteros y divide el mayor por el menor, mostrando un mensaje de error si esos 
significa dividir entre cero (excepcion ZeroDivisionError. Escribir un programa que utilice esta funcion, 
pidiendo los valores al usuario.
'''
def divide(x, y):
    """ Divide el mayor entre el menor, mostrando un mensaje
        de error si se produce una division entre cero. """

    dividendo = max(x, y)
    divisor   = min(x, y)

    try:
        return float(dividendo) / divisor
    except ZeroDivisionError:
        print ("Error; el dividendo es igual a cero")
        return None

x = int(input("x: "))
y = int(input("y: "))
print (x, "/", y, "=", divide(x, y))