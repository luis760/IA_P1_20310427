# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 10:04:27 2023

@author: 52331
"""


#librerias
import numpy as np
import cv2
#creamos una lista con los diferentes colores
colores = ["rojo", "azul", "verde", "amarillo", "marrón", "lila", "negro", "rosa"]

#por medio de el metodo len() sacamos la cantidad de elementos que hay en el arreglo colores

print("existen " , len(colores), " colores en el arreglo")
#por medio de un for que empieza en 0 y termina en el numero de elementos del arreglo
#vamos 
for i in range (len(colores)):
        print(colores[i])
   