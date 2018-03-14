'''
Created on 14 mar. 2018

@author: diago
'''
# ‐*‐ coding: utf‐8 ‐*‐

dinero = float(input("Introduce la cantidad de dinero: "))

interes = float(input("Introduce el interés: "))

years = float(input("Introduce el número de años: "))

dineroFinal = round(dinero * (1 + interes/100) ** years, 2)

print ("La cantidad final será de", dineroFinal)