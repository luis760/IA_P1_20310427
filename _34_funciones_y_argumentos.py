# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 13:28:09 2023

@author: 52331
"""

#librerias
import numpy as np
import cv2
#metodo que muestra el dato del comandante
def metodo(nombre):
    print('dato del comandante : ', nombre)

#creamos el diccionario con los datos de altura, equipo, precio y goles
cr7={
	'Altura': '1.88',
	'Equipo': 'All Nassar',
	'Precio': '2,000,000 euros' ,
    'Goles' : '786'   
    
    }
#le pedimos al usuario que nos diga que dato quiere borrar sobre el comandante
entrada = int(input('Que quiere saber del comandante SIUUUUU?: \n 1-ALTURA \n 2-EQUIPO \n 3-PRECIO \n 4-GOLES \n ' ))
#serie de condicionales para borrar el dato deseado
if(entrada == 1):
    #llamamos al metodo y de parametro le mandamos el dato que el usuario desea saber
   metodo(cr7['Altura'])
if(entrada == 2):
    metodo(cr7['Equipo'])
if(entrada == 3):
    metodo(cr7['Precio'])
if(entrada == 4):
    metodo(cr7['Goles'])