'''
Created on 14 mar. 2018

@author: diago
'''
# ‐*‐ coding: utf‐8 ‐*‐

import re

password = input("Introduce contraseña: ")

if (len(password) < 8 or  # Longitud
    re.search('[A-Z]', password) is None or  # Mayuscula
    re.search('[a-z]', password) is None or  # Minuscula
    re.search('[0-9]', password) is None or  # Numero
    re.search('[^a-zA-Z0-9_]', password) is None or  # Alfanumerico
    ' ' in password):  # Espacio en blanco
    print ("La contraseña no es segura")

else:
    print ("Contraseña establecida correctamente")