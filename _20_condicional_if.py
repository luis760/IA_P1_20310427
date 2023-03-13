# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 10:22:12 2023

@author: 52331
"""

#librerias
import numpy as np
import cv2
#creamos una lista con diferentes colores
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#utilizamos un ciclo for para recorrer toda la lista
for i in range(len(colores)):
    #utilizamos un if para ubicar el color azul dentro de la lista 
    if(colores[i]=='azul'):
        print("He encontrado el color azul y esta en la posicion" , i )
    
    