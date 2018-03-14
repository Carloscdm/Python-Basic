'''
Created on 14 mar. 2018

@author: diago
'''
def extrae(lista, indice):
    """ Devuelve en elemento que ocupa la posicion 'indice' en 'lista',
        o None si el indice esta fuera de los limites de la lista """

    try:
        return lista[indice]
    except IndexError:
        return None

lista    = range(34, 89, 3)
posicion = 13
print (extrae(lista, posicion))
print (extrae(lista, 100))