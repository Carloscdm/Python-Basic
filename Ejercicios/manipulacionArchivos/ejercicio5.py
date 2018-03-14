'''
Created on 14 mar. 2018

@author: diago
'''
""" Anadimos la linea [1... 10] a 'datos_ficheros' """

fd = open("datos_ficheros", "a")   # a de "append"

# Generamos la linea que vamos a anadir al fichero, dejando tres
# espacios, por ejemplo, entre cada numero. En un programa real
# utilizariamos tecnicas mas avanzadas para asegurarnos de que
# todos los numeros estan alineados:
# http://docs.python.org/tutorial/inputoutput.html

for numero in range(1, 11):
    fd.write(str(numero) + "   ")
fd.write("\n")

# Lo hacemos de nuevo, ahora con srt.join()
numeros = [str(x) for x in range(1, 11)]
linea = "\t".join(numeros)
fd.write(linea + "\n")

fd.close()


print ("Hecho!")