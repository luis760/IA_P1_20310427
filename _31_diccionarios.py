# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 13:10:03 2023

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
#le pedimos al usuario que nos diga que dato quiere saber sobre el comandante
entrada = int(input('Que quiere saber del comandante SIUUUUU?: \n 1-ALTURA \n 2-EQUIPO \n 3-PRECIO \n 4-GOLES \n ' ))
#serie de condicionales para mostrar el dato deseado
if(entrada == 1):
    print(cr7['Altura'])
if(entrada == 2):
    print(cr7['Equipo'])
if(entrada == 3):
    print(cr7['Precio'])
if(entrada == 4):
    print(cr7['Goles'])