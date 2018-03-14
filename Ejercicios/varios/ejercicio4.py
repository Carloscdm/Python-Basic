'''
Created on 14 mar. 2018

@author: diago
'''
# ‐*‐ coding: utf‐8 ‐*‐

def addAlumno():
    alumno = input("Introduce nombre del alumno: ")
    alumnos[alumno] = ''
    print ("Alumno", alumno, "añadido")
    showMenu()

def deleteAlumno():
    alumno = input("Introduce nombre del alumno: ")
    alumnos.pop(alumno)
    print ("Alumno", alumno, "eliminado")
    showMenu()

def showNotas():
    for key in alumnos:
        print (key, ":", alumnos[key])
    showMenu()

def addNota():
    alumno = input("Introduce nombre del alumno: ")
    nota = input("Introduce nota para " + alumno + ": ")
    alumnos[alumno] = nota
    showMenu()

def showMenu():
    print
    print ("1 - Añadir Alumno")
    print ("2 - Eliminar alumno")
    print ("3 - Mostrar Notas")
    print ("4 - Añadir Nota")
    print ("5 - Mostrar el Menú")
    print ("6 - Salir")
    print
    
    opcion = input("Seleccione una opción: ")
    
    try:
        opciones[opcion]()
    except KeyError:
        print ("La opción", opcion, "no es válida")
        showMenu()

def salir():
    print ("Exiting...")

opciones = {1 : addAlumno,
            2 : deleteAlumno,
            3 : showNotas,
            4 : addNota,
            5 : showMenu,
            6 : salir,}

alumnos = {}

showMenu()

