# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 08:47:43 2023

@author: 52331
"""

#librerias
import numpy as np
import cv2
#creamos la lista con los colores
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#borramos a los colores rojo verde y marron
del colores[0]
del colores[1]
del colores[2]
#mostramos la lista
print(colores)
print("Se han borrado los colores rojo, verde y marron  ")