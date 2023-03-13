# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 12:38:23 2023

@author: 52331
"""

#librerias
import numpy as np
import cv2
#inicializamos x=1 ya que va a ser nuestro contador
x=1
#le pedimos al usuario que digite el numero de veces que se va a repetir el ciclo while
entrada = int(input('Cuantas veces quieres que te diga hola? 1-10:\n'))
#aplicamos condicionales para que el usuario no pueda digitar numeros fuera del rango
if(entrada <=0 or entrada >10):
    print("ese numero no es valido")
else:
    while x<=entrada:
        print("hola" , x )
        x+=1