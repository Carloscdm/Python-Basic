'''
Created on 14 mar. 2018

@author: diago
'''
""" Lee una cadena de texto del usuario e imprime por pantalla un mensaje
    simpatico si y solo si contiene todas las vocales """


# Fijate en que no necesitamos especificar las vocales mayusculas tambien,
# ya que utilizamos lower() para hacer la comparacion siempre entre minusculas
vocales = ["a", "e", "i", "o", "u"]
palabra = input("Introduzca palabra: ")

for vocal in vocales:
    if vocal not in palabra.lower():
        break
else: # Solo se ejecuta si el for no hace 'break'
    print ("Probablemente has escrito 'murcielago' :-)")