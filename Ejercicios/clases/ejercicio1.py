'''
Created on 14 mar. 2018

@author: diago
'''
#!\usr\env python
# -*- coding: utf-8 -*-

"""
Ejercicio 1
Enunciado: Cree una clase llamada Cuenta. Como atributo tendrá un número 
float llamado saldo, con una cantidad inicial de 0 euros.
Tendra dos metodos:
  - ingresar, con un parámetro que indica la cantidad a sumar al saldo.
  - retirar, con un parámetro que sera un numero float de euros a restar 
  del saldo.
Cree un programa para ingresar 125.23, 503.4 y 50 euros y luego retire, 
333.34 euros.
Muestre tras cada operacion, el saldo de la cuenta.

"""

class Cuenta (object):
    def __init__ (self):
        self.saldo = 0

    # otra posibilidad de constructor    
#    def __init__ (self, cantidad = 0):
#        self.saldo = cantidad
        
    def ingresar (self, cantidad):
        self.saldo += cantidad
    
    def retirar (self, cantidad):
        self.saldo -= cantidad
        
if __name__ == '__main__':

    objeto_cuenta = Cuenta ()
    print ('Cuenta recien creada: saldo = ', objeto_cuenta.saldo)
    ingresos = [125.23, 503.4, 50]
    for i in ingresos:
        objeto_cuenta.ingresar (i)
        print ('Ingreso nuevo: saldo = ', objeto_cuenta.saldo )
    objeto_cuenta.retirar (333.34)
    print ('Retirada de efectivo: saldo = ', objeto_cuenta.saldo)
    objeto_cuenta.retirar (340.29)
    print ('Retirada de efectivo: saldo = ', objeto_cuenta.saldo)