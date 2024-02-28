# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 22:11:05 2024
@author: ramarilla
"""
from IPython.display import display
import numpy as np
import pandas as pd
import statsmodels.api as sm
from tkinter.messagebox import showinfo


class Sujeto:
    observadores=[]

    def agregar(self, obj):
        self.observadores.append(obj)
    def quitar(self, ):
        pass
    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(args)


class Observador:
    def update(self):
        raise NotImplementedError("Delegación de actualización")


class ConcreteObserverA(Observador):

    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self, args):
        print("Actualización dentro de ObservadorConcretoA")
        data,=args        
        df=pd.DataFrame(data)
        display(df)
        print("---"*23)
        print("Procesando simulacion de retornos del S&P Merval para realizar regresion")
        retornos = []
        for x in range(0,len(df)):        
            retorno_periodo = float(np.random.normal(40,10,1))
            retornos.append(retorno_periodo)
        display(df)
        df['retorno anual Merval']=retornos
        display(df)
        print("---"*23)
        print("Procesando el calculo de Regresion por MCO")
        x=df[['retorno anual']]
        y=df[['retorno anual Merval']]
        model = sm.OLS(y, x)
        results = model.fit()
        print(results.summary())
        with open("resumen_de_la_regresion.txt", 'a') as opened_file:
            output=f"Dataframe de retornos del fondo vs S&P Merval\n\n{df}\n\nResumen de la Regresion\n\n{results.summary()}"
            opened_file.write(f"{output}\n\n")
        t1 = "El analisis incluye la estimacion de una Regresion por MCO "
        t2 = "y se ha generado el archivo resumen_de_la_regresion.txt en la carpeta principal en donde hay"
        t3 = " un completo detalle de la misma."
        t4 = "Principales datos de la Regresion: "
        t5 = "El Coeficiente de Determination de la Regresion es igual a "
        t6 = "El Coeficiente de Determinacion Ajustado de la Regresion es igual a: "
        mensaje_resumen_de_la_regresion=f"{t1}{t2}{t3}\n\n{t4}\n\n{t5}{results.rsquared}\n\n{t6}{results.rsquared_adj}\n\n"
        showinfo("Regresion",mensaje_resumen_de_la_regresion)
