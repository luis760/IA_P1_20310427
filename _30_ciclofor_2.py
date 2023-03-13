# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 13:06:40 2023

@author: 52331
"""

#librerias
import numpy as np
import cv2
#declaramos las variables para los ciclos while
entrada2=1
x=1
#Este while repite el cilo de manera indenfinida hasta que el usuario decida lo contrario
while entrada2==1:
    #le preguntamos al usuario si quiere seguir repitiendo el programa y almacenamos su respuesta
    entrada = int(input('Cuantas veces quieres que te diga hola? 1-10:\n'))
    #aplicamos condicionales para que el usuario no pueda digitar numeros fuera del rango
    if(entrada <=0 or entrada >10):
        print("ese numero no es valido")
    else:
      for i in range (x):
          print("hola" , x )
    entrada2 = int(input('Desea seguir repitiendo el ciclo:\n SI=1 \n NO=2\n'))
    if(entrada2==2):
        print("adios")
