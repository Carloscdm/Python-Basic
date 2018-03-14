'''
Created on 14 mar. 2018

@author: diago
'''
""" Guarda la suma de los enteros de la primera linea 'datos_ficheros'
    a otro fichero, llamado 'primera_linea_suma' """

fd = open("datos_ficheros", "r")
linea = fd.readline()
fd.close()

# Utilizamos una lista por comprension para convertir cada entero
# de la primera linea a int (ya que split() nos los da como str)
numeros = [int(x) for x in linea.split()]

fout = open("primera_linea_suma", "w")
fout.write(str(sum(numeros)) + "\n")
fout.close()

print ("Hecho!")