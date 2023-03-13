# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 10:26:37 2023

@author: 52331
"""

#librerias
import numpy as np
import cv2

#le pedimos al usuario su edad
edad = int(input('¿Cuál es tu edad?\n'))
#aplicamos diferentes condicionales para los diferentes rangos de edad y
#mostramos cierto mensaje al usuario
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
    print("no estas ni viejo ni eres un niño")
elif edad >= 18 and edad <= 100:
	print('Eres mayor de edad.')
elif   edad >= 120:
    print("hijole carnal la neta ya andas en las ultimas")
else:
	print('Edad no válida.')