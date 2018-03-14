'''
Created on 14 mar. 2018

@author: diago
'''
def encuentra(lista, elemento):
    """ Devuelve la posicion de elemento en lista y -1 si no esta en ella """

    try:
        return lista.index(elemento)
    except ValueError:
        return -1

numeros = range(20)
buscado = 78
print (encuentra(numeros, buscado))