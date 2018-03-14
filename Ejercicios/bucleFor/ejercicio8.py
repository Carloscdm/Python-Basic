'''
Created on 14 mar. 2018

@author: diago
'''
""" Para cada una de las cadenas de texto almacenadas en una lista, imprimir por
    pantalla el indice y la cadena en si e indicar si la palabra es demasiado
    corta (cinco o menos caracteres) o larga (mas de cinco caracteres) """


frase = """ Programmers are, in their hearts, architects, and the first thing
            they want to do when they get to a site is to bulldoze the place
            flat and build something grand """

listado = frase.split()    # listado = ["Programmers", "are", ",",...]

for index, palabra in enumerate(listado):
    print ("La palabra numero", index, "(", palabra, ") es demasiado") ,
    if len(palabra) > 5:
        print ("larga!")
    else:
        print ("corta!")