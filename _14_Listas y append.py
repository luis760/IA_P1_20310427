# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 09:06:28 2023

@author: 52331
"""


#librerias
import numpy as np
import cv2

#creamos la lista con los colores
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#por medio del metodo append agregamos los elementos fluxia y celeste a nuestra lista
colores.append("fluxia")
colores.append("celeste")
#Mostramos la lista y los colores agregados
print(colores)
print("Se han agregado los colores " , colores[10] , " y " , colores[11] )