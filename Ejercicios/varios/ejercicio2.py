'''
Created on 14 mar. 2018

@author: diago
'''
# ‐*‐ coding: utf‐8 ‐*‐

nombre = input("Introduce nombre de usuario: ")

if (len(nombre) < 6):
    print ("El nombre de usuario debe contener al menos 6 caracteres")
if (len(nombre) > 12):
    print ("El nombre de usuario no puede contener más de 12 caracteres")
if not (nombre.isalnum()):
    print ("El nombre de usuario puede contener solo letras y números")
else:
    print ("El nombre de usuario es válido")