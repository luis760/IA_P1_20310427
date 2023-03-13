# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 09:13:07 2023

@author: 52331
"""

#librerias
import numpy as np
import cv2

#creamos la lista con los colores
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#por medio del metodo sort ordenamos los elementos de la lista de manera alfabetica 
#y con la condicion "reverse=true" los ordenamas de manera descendente z-a
colores.sort(reverse=True)
print(colores)