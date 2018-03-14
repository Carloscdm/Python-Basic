'''
Created on 14 mar. 2018

@author: diago
'''
# ‐*‐ coding: utf‐8 ‐*‐

import datetime as dt, time

def abrir_log(nombre):
    archivo = open(nombre, "a")
    fecha = str(dt.datetime.now())
    mensaje = fecha + ": Iniciando registro de errores\n"
    archivo.write(mensaje)
    return archivo

def guardar_log(archivo, mensaje):
    fecha = str(dt.datetime.now())
    mensaje = fecha + ": " + mensaje + "\n"
    archivo.write(mensaje)

def cerrar_log(archivo):
    fecha = str(dt.datetime.now())
    mensaje = fecha + ": Finalizando registro de errores\n"
    archivo.write(mensaje)
    archivo.close()

archivo_log = abrir_log("log.txt")
time.sleep(5)
guardar_log(archivo_log, "Primer mensaje")
time.sleep(1)
guardar_log(archivo_log, "Segundo mensaje mensaje")
time.sleep(1)
guardar_log(archivo_log, "Ultimo mensaje")
time.sleep(5)
cerrar_log(archivo_log)