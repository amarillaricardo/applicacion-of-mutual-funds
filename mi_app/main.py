#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 20:36:57 2023

@author: ramarilla
"""

from tkinter import Tk
from vista import VistaPrincipal
from excepciones import RegistroLogError
from excepciones import registrar
import observador






if __name__=="__main__":
    
    root_tk = Tk()
    
    mi_app = VistaPrincipal(root_tk)
    
    observador_de_simulaciones_de_cotizaciones_de_fondos = observador.ConcreteObserverA(mi_app.mi_modelo)
    
    root_tk.mainloop()
    
try:
   registrar()
except RegistroLogError as log:
   log.registrar_error()
    
   
    

