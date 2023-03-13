"""
Created on Sat Mar 11 13:10:03 2023

@author: 52331
"""

#librerias
import numpy as np
import cv2
#creamos el diccionario con los datos de altura, equipo, precio y goles
cr7={
	'Altura': '1.88',
	'Equipo': 'All Nassar',
	'Precio': '2,000,000 euros' ,
    'Goles' : '786'   
    
    }
#iteramos en el diccionario para mostrar todos los datos
for x in cr7:
    print("dato ", x, " = ", cr7[x])