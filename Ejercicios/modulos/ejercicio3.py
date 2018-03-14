# ‐*‐ coding: utf‐8 ‐*‐
'''
Created on 14 mar. 2018

@author: diago

Cree un nuevo directorio en su directorio de usuario llamado modulos. Copie el modulo 
operaciones_basicas.txt en dicho directorio. Haga lo necesario, en su código o en el 
sistema, para que se ejecute el apartado (a) del ejercicio 2 desde cualquier otro directorio que no sea modulos. 
'''
# Creamos el subdirectorio 'modulos'
# Copiamos el módulo 'operaciones_basicas.py' en ese subdirectorio

#Para hacer accesible el modulo, la forma más sencilla para que pueda ejecutar el primer #apartado del ejercicio 2 es retocar el código agregando las dos primeras lineas siguientes

import sys
sys.path.append ('C:\\Users\\alumno\\modulos')

# Luego ponemos el codigo el ejercicio 2 (a)

import operaciones_basicas
a, b = 13, 3
print ('Operandos =', a, b)
print ('sumar = ', operaciones_basicas.sumar (a, b))
print ('restar = ', operaciones_basicas.restar (a, b))
print ('multiplicar = ', operaciones_basicas.multiplicar (a, b))
print ('dividir = ', operaciones_basicas.dividir (a, b))