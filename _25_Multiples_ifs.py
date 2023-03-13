# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 12:27:22 2023

@author: 52331
"""
#librerias
import numpy as np
import cv2
#Le pedimos al usario que digite un numero del uno al 4 y lo guaradmos en una variable
entrada = int(input('Vas a entrar una rifa, elije un numero dl 1 al 4:\n'))
#serie de condicionales para mostrar diferentes mensajes al usuario de acuerdo al numero que eligio
if(entrada ==1): print("Usted se ha ganado un poderoso set de ollas de royal prestige")
if(entrada ==2): print("Usted se ha ganado un boleto de ida y vuelta a tangamandapio")
if(entrada ==3 or entrada ==4): print("Usted no gano nada")
