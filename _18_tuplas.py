# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 10:10:53 2023

@author: 52331
"""

#librerias
import numpy as np
import cv2
#generamos una tupla de nombre "numeros"
numeros = (10, 5, 11,"el resultado es: ")
#imprimimos una operacion con esa misma tupla
print(numeros[3], (numeros[2]*numeros[1])/numeros[0])
#mostramos todos los elementos de la tupla 
for i in range(3):
    print(numeros[i])