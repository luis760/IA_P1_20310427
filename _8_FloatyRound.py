# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 21:14:20 2023

@author: 52331
"""

#librerias
import numpy as np
import cv2
#especificamos el numero al cual le vamos a redondear los decimales y lo guaradmos 
#en una variable de tipo float

numeroaredondear = 17.567383292929200234
#El comando round espera dos argumentos , el numero y el numero de 
#decimales que se utilizaran para redondear, despues mostramos el resultado por
#medio de un print
print(round(numeroaredondear,5))