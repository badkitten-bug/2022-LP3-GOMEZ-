# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:23:09 2022

@author: USER
"""

import sqlite3

#con el comando connect buscara la base de datos
# que temga ese nombre

conexion=sqlite3.connect("bdbiblioteca.db")
conexion.close()