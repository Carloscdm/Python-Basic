'''
Created on 14 mar. 2018

@author: diago
'''
""" Lee una cadena de texto del usuario y para cada letra indica si es una
    vocal o una consonante. """


# Fijate en que no necesitamos especificar las vocales mayusculas tambien,
# ya que utilizamos lower() para hacer la comparacion siempre entre minusculas
vocales = ["a", "e", "i", "o", "u"]
vocales = "aeiou" # tambien sirve
palabra = input("Introduzca palabra: ")

for letra in palabra:
    print (letra) ,
    if letra.lower() in vocales:
        print ("es una vocal")
    else:
        print ("es una consonante")