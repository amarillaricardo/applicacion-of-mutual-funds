#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:37:58 2023
@author: ramarilla
"""
import os
import datetime
class RegistroLogError(Exception):


    BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
    ruta = os.path.join(BASE_DIR, "log.txt")

    def __init__(self, linea, archivo, fecha):
        self.linea = linea
        self.archivo = archivo
        self.fecha = fecha

    def registrar_error(self):
        log = open(self.ruta, "a")
        print("Se ha dado un error:", self.archivo, self.linea, self.fecha, file=log)

def registrar():
    raise RegistroLogError(7, "archivo1.txt", datetime.datetime.now())
