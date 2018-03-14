'''
Created on 14 mar. 2018

@author: diago
'''
""" Lee valores del usuario hasta que teclee un numero par, utilizando
    un bucle while """

while True:
    numero = int(input("Introduzca numero par: "))
    if not numero % 2 == 0:
        print ("Lo siento,", numero, "no es par")
    else:
        print (numero, "es par!")
        break