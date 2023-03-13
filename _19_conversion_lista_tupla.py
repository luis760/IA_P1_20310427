# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 10:17:08 2023

@author: 52331
"""

#librerias
import numpy as np
import cv2
#creamos un objeto tipo lista de nombre colores
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#convertimos la lista anterior a un objeto de tipo tupla 
colores_tupla = tuple(colores)
#imprimos el tipo de objeto que es la variable : colores tupla para asegurarnos
#de que se haya hecho la comversion correctamente
print(type(colores_tupla))
#imprimimos los elementos de la tupla
for i in range(10):
    print(colores_tupla[i])