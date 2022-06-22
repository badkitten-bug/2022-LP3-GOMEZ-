# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 08:56:06 2022

@author: USER
"""

# PROBLEM : Necesitamos mostrar los nombres de una cadena
# presentando las prinmeras letrs n mayuscula
#~En word se conoce como formato Título

#Importar la libreria

import camelcase

nombre="steve edward gomez huamani"

print(nombre.upper())
print(nombre.title())

#Creamos un objeto llamado cam

cam=camelcase.CamelCase()

print("con camelcase.....")

#Imprimimos el nombre en formato titulo
#utilizamos camelcase

print(cam.hump(nombre))

#para resolver el siguiente problema
#creamos otro objeto lamado cam2
#al definir el objeto,incluimos los argumentos
# 'steve' y 'gomez'

cam2=camelcase.CamelCase('steve','gomez')
print(cam2.hump(nombre))