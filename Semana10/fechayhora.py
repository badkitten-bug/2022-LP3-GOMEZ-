# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 08:40:01 2022

@author: USER
"""

#Fecha y Hora
from datetime import datetime

fechayhora = datetime.now()

print(f"Hoy: {fechayhora}")
print(fechayhora.year)
print(fechayhora.month)
print(fechayhora.day)
print(fechayhora.hour)
print(fechayhora.min)
print(fechayhora.second)
print(fechayhora.microsecond)

