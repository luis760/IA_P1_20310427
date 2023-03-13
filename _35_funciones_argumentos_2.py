# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 13:29:16 2023

@author: 52331
"""


#librerias
import numpy as np
import cv2
#metodo que muestra el dato del comandante
def metodo(*args):#le especificamos que va a ser un arreglo pero no le decimos ni 
#tipo nilongitud
#Mostramos los datos del arreglo en un ciclo for
    for i in range(len(args)):
        print('\ndatos del comandante : ', args[i])

#creamos la lista con los datos de altura, equipo, precio y goles
cr7=["Goleador","el mejor de la historia","SIIIIUUUUU"]
#mandamos llamar al metodo
metodo(cr7)