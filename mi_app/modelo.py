# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 08:03:57 2023
@author: ramarilla
"""
# from tkinter import *
# from tkinter import ttk
# import sqlite3
# import re
from tkinter.messagebox import showinfo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from base_de_datos import BaseDeDatos
from observador import Sujeto

mi_base_de_datos = BaseDeDatos()

# Decorador con parametro el cual es un log de seguimiento de las simulaciones realizadas.


def log(fichero_log):

    def decorador_log(funcion_parametro):

        def decorador_funcion(*args, **kwargs):
            with open(fichero_log, 'a') as opened_file:
                output = funcion_parametro(*args, **kwargs)
                opened_file.write(f"{output}\n\n")
        return decorador_funcion

    return decorador_log

# ##############################################
# MODELO
# ##############################################


class Modelo(Sujeto):

    def consultar_especifica(self, id_del_fondo, numero_de_años, tree2, root):
        if id_del_fondo == "":
            showinfo("Consulta especifica",
                     "Debe seleccionar un id de fondo para continuar," +
                     " luego de haber consultado la ddbb. Gracias")
        elif id_del_fondo != "":
            if numero_de_años == 0:
                showinfo("Consulta especifica",
                         "Debe seleccionar año para analisis de " +
                         "rentabilidad para continuar. Gracias")
            elif numero_de_años != 0:
                id_del_fondo = str(id_del_fondo)
                sql = "SELECT * FROM fondos WHERE id =" + id_del_fondo+" ORDER BY id ASC"
                con = mi_base_de_datos.conexion()
                cursor = con.cursor()
                datos = cursor.execute(sql)
                resultado = datos.fetchall()
                df = pd.DataFrame(resultado, columns=["id", "nombre_del_fondo",
                                                      "tipo_de_inversion", "horizonte",
                                                      "sociedad_gerente", "sociedad_depositaria",
                                                      "region", "cotizado_originalmente",
                                                      "calificacion", "fecha_de_calificacion",
                                                      "calificadora_de_riesgo", "pais_sede",
                                                      "tipo_de_activo", "estado", "bolsa",
                                                      "codigo_cafci", "comision_de_ingreso",
                                                      "honorarios_de_administracion", "comision_de_egreso",
                                                      "comision_de_transferencia",
                                                      "gastos_ordinarios_de_gestion", "cobra_comision_por_desempeno",
                                                      "inversion_minima", "plazo_de_liquidacion"])
                df_transposed = df.T
                df_transposed['campo'] = df.columns.values
                consulta_especifica = df_transposed.iloc[:, [1, 0]]
                consulta_especifica.index = list(range(0, len(df_transposed.iloc[:, 1]), 1))
                consulta_especifica.columns = ['campo', "variable"]
                tabla_de_retornos = {"Variables": [
                                                   "Retorno de 1 semana",
                                                   "Retorno 1 mes",
                                                   "Retorno de 3 meses",
                                                   "Retorno de 6 meses",
                                                   "Retorno de 9 meses",
                                                   "Retorno de 12 meses",
                                                   "Retorno de 2 años",
                                                   "Retorno de 3 años",
                                                   "Retorno de 4 años",
                                                   "Retorno de 5 años",
                                                   "Volatilidad anual",
                                                   "Inflacion del año",
                                                   "Var. dolar CCL del año",
                                                    ], "Tasa": [
                                                                float(np.random.normal(7, 2, 1)),
                                                                float(np.random.normal(20, 5, 1)),
                                                                float(np.random.normal(60, 10, 1)),
                                                                float(np.random.normal(80, 10, 1)),
                                                                float(np.random.normal(100, 10, 1)),
                                                                float(np.random.normal(200, 10, 1)),
                                                                float(np.random.normal(290, 10, 1)),
                                                                float(np.random.normal(360, 10, 1)),
                                                                float(np.random.normal(400, 10, 1)),
                                                                float(np.random.normal(500, 10, 1)),
                                                                float(np.random.normal(640, 10, 1)),
                                                                100,
                                                                120
                                                                ]}
                self.actualizar_treeview2(tabla_de_retornos, consulta_especifica, tree2)
                self.simulacion_cotizaciones_del_fondo(numero_de_años, root)
                showinfo("Base de datos: Consulta",
                         "La consulta a la base de datos del fondo con id " + id_del_fondo +
                         " se ha realizado con exito")

    def limpiar_treeview(self, mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)

    def actualizar_treeview2(self, tabla_de_retornos, consulta_especifica, mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)
        campo = list(consulta_especifica.iloc[:, 0])
        variable = list(consulta_especifica.iloc[:, 1])
        rentabilidad = list(tabla_de_retornos["Variables"])
        tasa = list(tabla_de_retornos["Tasa"])
        for indice in range(0, len(consulta_especifica.iloc[:, 1])):
            if indice < len(rentabilidad):
                mitreview.insert("", "end", text=str(campo[indice]),
                                 values=(str(variable[indice]), str(rentabilidad[indice]), 
                                         str(tasa[indice])))
            else:
                mitreview.insert("", "end", text=str(campo[indice]), values=(str(variable[indice]), ))

    @log('simulaciones_de_cotizaciones_de_fondos.log')
    def simulacion_cotizaciones_del_fondo(self, numero_de_años, root):
        numero_de_años = int(numero_de_años)
        numbers = range((2023-numero_de_años), 2023)
        años = []
        for number in numbers:
            años.append(number)
        valor_de_cuota_parte = np.random.normal(10000, 4000, numero_de_años)
        patrimonio_de_fondo = np.random.normal(100000000, 7000000, numero_de_años)
        cantidad_de_cuotapartes = patrimonio_de_fondo/valor_de_cuota_parte
        cotizaciones_graph = {"años": años, "vcp": list(valor_de_cuota_parte)}
        patrimonio_graph = {"años": años, "PN": list(patrimonio_de_fondo)}
        cantidad_de_cuotas_graph = {"años": años, "CCP": list(cantidad_de_cuotapartes)}
        retornos = []
        for x in range(0, len(cotizaciones_graph["vcp"])):
            if x == 0:
                retorno_periodo = float(np.random.normal(40, 10, 1))
            else:
                valor_actual = float(cotizaciones_graph['vcp'][x])
                valor_anterior = float(cotizaciones_graph['vcp'][x-1])
                retorno_periodo = (((valor_actual/valor_anterior)-1)*100)
            retornos.append(retorno_periodo)
        rentabilidad_anual_graph = {"años": años, "retorno anual": retornos}
        df1 = pd.DataFrame(cotizaciones_graph)
        df2 = pd.DataFrame(patrimonio_graph)
        df3 = pd.DataFrame(cantidad_de_cuotas_graph)
        df4 = pd.DataFrame(rentabilidad_anual_graph)
        figure1 = plt.Figure(figsize=(4, 4), dpi=100)
        ax1 = figure1.add_subplot(111)
        line1 = FigureCanvasTkAgg(figure1, root)
        line1.get_tk_widget().grid(row=0, column=4, columnspan=4, rowspan=23)
        df1 = df1[['años', 'vcp']].groupby('años').sum()
        df1.plot(kind='line', legend=True, ax=ax1, color='r', marker='o', fontsize=8)
        ax1.set_title('Valor de Cuota Parte')
        figure2 = plt.Figure(figsize=(4, 4), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, root)
        line2.get_tk_widget().grid(row=0, column=10, columnspan=4, rowspan=23)
        df2 = df2[['años', 'PN']].groupby('años').sum()
        df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
        ax2.set_title('Patrimonio neto del Fondo')
        figure3 = plt.Figure(figsize=(4, 4), dpi=100)
        ax3 = figure3.add_subplot(111)
        line3 = FigureCanvasTkAgg(figure3, root)
        line3.get_tk_widget().grid(row=25, column=4, columnspan=4, rowspan=23)
        df3 = df3[['años', 'CCP']].groupby('años').sum()
        df3.plot(kind='line', legend=True, ax=ax3, color='r', marker='o', fontsize=10)
        ax3.set_title('Cantidad de Cuotapartes')
        figure4 = plt.Figure(figsize=(4, 4), dpi=100)
        ax4 = figure4.add_subplot(111)
        bar4 = FigureCanvasTkAgg(figure4, root)
        bar4.get_tk_widget().grid(row=25, column=10, columnspan=4, rowspan=23)
        df4 = df4[['años', 'retorno anual']].groupby('años').sum()
        df4.plot(kind='bar', legend=True, ax=ax4)
        ax4.set_title('Retorno Anual')
        self.notificar(rentabilidad_anual_graph)
        t1 = "El resultado de la simulacion es la siguiente: "
        return f"{t1}{rentabilidad_anual_graph}"

    def listado_de_ids(self):
        sql = "SELECT id FROM fondos ORDER BY id ASC"
        con = mi_base_de_datos.conexion()
        cursor = con.cursor()
        datos_de_id = cursor.execute(sql)
        listado = datos_de_id.fetchall()
        listado_de_ids = []
        for element in range(0, len(listado)):
            listado_de_ids.append(listado[element][0])
        return listado_de_ids

    def actualizar_treeview3(self, tabla_de_retornos, mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)
        for indice in range(0, len(tabla_de_retornos["Variables"])):
            mitreview.insert("", "end", text=str(tabla_de_retornos["Variables"][indice], ),
                             values=(str(tabla_de_retornos["Tasa"][indice]), ))

    def hola(self):
        print("Menu a completarse")
