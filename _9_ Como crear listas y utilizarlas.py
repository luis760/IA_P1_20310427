# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 08:34:57 2023

@author: 52331
"""

#librerias
import numpy as np
import cv2
#creamos una lista con los diferentes colores
colores = ["rojo", "azul", "verde", "amarillo", "marrón", "lila", "negro", "rosa"]

#mediante un cilo for recorremos la lista de principio a fin y mediante una
#condicional if-else definimos cual es la posicion numero 3 de la lista 
for i in range (len(colores)):
    if(i==3):
        print("Esta es la posicion 3 del arreglo")
    else:
        print("el color que esta en la posicion ", i ," es : " , colores[i])