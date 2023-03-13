# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 13:20:26 2023

@author: 52331
"""
#librerias
import numpy as np
import cv2

#creamos el diccionario con los datos de altura, equipo, precio y goles
cr7={
	'Altura': '1.88',
	'Equipo': 'All Nassar',
	'Precio': '2,000,000 euros' ,
    'Goles' : '786'   
    
    }
#le pedimos al usuario que nos diga que dato quiere borrar sobre el comandante
entrada = int(input('Que quiere borrar del comandante SIUUUUU?: \n 1-ALTURA \n 2-EQUIPO \n 3-PRECIO \n 4-GOLES \n ' ))
#serie de condicionales para borrar el dato deseado
if(entrada == 1):
    del(cr7['Altura'])
if(entrada == 2):
    del(cr7['Equipo'])
if(entrada == 3):
    del(cr7['Precio'])
if(entrada == 4):
    del(cr7['Goles'])
for x in cr7:
    #mostramos los datos restantes
    print("dato ", x, " = ", cr7[x])