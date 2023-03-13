# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 09:09:17 2023

@author: 52331
"""


#librerias
import numpy as np
import cv2

#creamos la lista con los colores
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#por medio del metodo insert agregamos el elemento magenta despues del elemento lila
# y el elemento turquesa en la pneultima posicion, insert recive dos parametros
#posicion y el elemento a insertar

colores.insert(6,"magenta")
colores.insert(10,"turquesa")
#Mostramos la lista y los colores agregados
print(colores)
print("Se han agregado los colores " , colores[6] , " y " , colores[10] )