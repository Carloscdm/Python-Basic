'''
Created on 14 mar. 2018

@author: diago
'''
""" Programa que lee nombres de fichero hasta que se
    introduce alguno que realmente existe """

while True:
    ruta = input("fichero: ")
    try:
        fd = open(ruta, "r")
        fd.close()
        break
    except IOError:
        print (ruta, "no existe, lo siento")