# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 10:33:18 2023

@author: 52331
"""
#librerias
import numpy as np
import cv2
#generamos una tupla con los colores que se admiten
colores=("rojo","azul","amarillo","verde")
#dejamos que el usuario digite su color
entrada = input('Introduce un color:\n')
#validamos que el color este en la tupla
if entrada in colores:
    print("el color es admitido")
else:
    print("el color es invalido")