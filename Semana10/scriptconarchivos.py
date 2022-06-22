# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:34:26 2022

@author: USER
"""

noticia = open("noticia.txt","rt",encoding='utf-8-sig')
datos_noticia = noticia.read()
lista = datos_noticia.split()
print(datos_noticia)

print(lista)