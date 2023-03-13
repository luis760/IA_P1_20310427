# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 13:39:01 2023

@author: 52331
"""

#librerias
import numpy as np
import cv2
#metodo que muestra el dato del comandante
def metodo(**kwargs):#como argumento le especificamos que va a ser un dato de tipo diccionario
#mostramos los datos de acuerdo al nombre de cada parametro
    print("Altura : " ,kwargs['Altura'] ,"\n","Equipo : " ,kwargs['Equipo'] ,"\n" ,"Precio : " ,kwargs['Precio'] ,"\n" ,"Goles : " ,kwargs['Goles'] ,"\n"  )

#mandamos llamar al metodo con los datos que va a recibir
metodo(Altura='1.88' , Equipo='All Nassar' ,Precio='2,000,000 euros' ,Goles='786' )
