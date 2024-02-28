# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 08:59:52 2023
@author: ramarilla
"""
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
from tkinter.messagebox import askyesno
import sqlite3
import re
# Decorador con parametro el cual es un log de seguimiento de las acciones en la base de datos.


def log(fichero_log):
    def decorador_log(funcion_parametro):
        def decorador_funcion(*args, **kwargs):
            with open(fichero_log, 'a') as opened_file:
                output = funcion_parametro(*args, **kwargs)
                opened_file.write(f"{output}\n\n")
        return decorador_funcion
    return decorador_log
class BaseDeDatos():
    def conexion(self):
        con = sqlite3.connect("mibase.db") 
        return con
    def crear_tabla(self):
        con = self.conexion()
        cursor = con.cursor()
        sql = """CREATE TABLE fondos
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nombre_del_fondo varchar(255) NOT NULL,
                  tipo_de_inversion varchar(255) NOT NULL,	 
                  horizonte varchar(255) NULL,
                  sociedad_gerente varchar(255) NOT NULL,
                  sociedad_depositaria varchar(255) NOT NULL,
                  region varchar(255) NULL,
                  cotizado_originalmente varchar(255) NULL, 
                  calificacion varchar(255) NULL,
                  fecha_de_calificacion varchar(255) NULL, 
                  calificadora_de_riesgo varchar(255) NULL,	 
                  pais_sede varchar(255) NULL,
                  tipo_de_activo varchar(255) NULL,
                  estado varchar(255) NULL,
                  bolsa varchar(255) NULL,
                  codigo_cafci varchar(255) NULL, 
                  comision_de_ingreso varchar(255) NULL,	 
                  honorarios_de_administracion varchar(255) NULL,	 
                  comision_de_egreso varchar(255) NULL,
                  comision_de_transferencia varchar(255) NULL,
                  gastos_ordinarios_de_gestion varchar(255) NULL, 
                  cobra_comision_por_desempeno varchar(255) NULL,
                  inversion_minima varchar(255) NULL,
                  plazo_de_liquidacion varchar(255) NULL)
        """
        cursor.execute(sql)
        con.commit()
        try:
            self.conexion()
            self.crear_tabla()
        except:
            print("Hay un error en la creacion de la base de datos")
    def actualizar_treeview(self,mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)
        sql = "SELECT id,nombre_del_fondo,tipo_de_inversion,codigo_cafci FROM fondos ORDER BY id DESC"
        con=self.conexion()
        cursor=con.cursor()
        datos=cursor.execute(sql)
        resultado = datos.fetchall()
        for fila in resultado:
            mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))
    @log('base_de_datos.log')
    def alta(self,nombre_del_fondo,tipo_de_inversion,horizonte,sociedad_gerente,
    sociedad_depositaria,region,cotizado_originalmente,calificacion,
    fecha_de_calificacion,calificadora_de_riesgo,pais_sede,
    tipo_de_activo,estado,bolsa, codigo_cafci,comision_de_ingreso,	 
    honorarios_de_administracion,comision_de_egreso,comision_de_transferencia,
    gastos_ordinarios_de_gestion,cobra_comision_por_desempeno,
    inversion_minima,plazo_de_liquidacion, tree):
        cadena = nombre_del_fondo
        patron="[A-Za-z0-9\sáéíóú]*"  #regex para el campo cadena
        if(re.match(patron, cadena)):
            if nombre_del_fondo !="" and tipo_de_inversion !="" and sociedad_gerente !="" and sociedad_depositaria !="" and codigo_cafci !="":
                con=self.conexion()
                cursor=con.cursor()
                data=(nombre_del_fondo,tipo_de_inversion,horizonte,sociedad_gerente,
                sociedad_depositaria,region,cotizado_originalmente,calificacion,
                fecha_de_calificacion,calificadora_de_riesgo,pais_sede,
                tipo_de_activo,estado,bolsa, codigo_cafci,comision_de_ingreso,	 
                honorarios_de_administracion,comision_de_egreso,comision_de_transferencia,
                gastos_ordinarios_de_gestion,cobra_comision_por_desempeno,
                inversion_minima,plazo_de_liquidacion)
                sql="""INSERT INTO fondos(nombre_del_fondo,tipo_de_inversion,
                    horizonte,sociedad_gerente,
                    sociedad_depositaria,region,cotizado_originalmente,calificacion,
                    fecha_de_calificacion,calificadora_de_riesgo,pais_sede,
                    tipo_de_activo,estado,bolsa, codigo_cafci,comision_de_ingreso,	 
                    honorarios_de_administracion,comision_de_egreso,
                    comision_de_transferencia,
                    gastos_ordinarios_de_gestion,cobra_comision_por_desempeno,
                    inversion_minima,plazo_de_liquidacion) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                                                                  ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                                                                  ?, ?, ?)"""
                cursor.execute(sql, data)
                con.commit()
                self.actualizar_treeview(tree)
                return f"Se han dado de alta el fondo con los siguiente datos: {data}"
                showinfo("Base de datos: Actualizacion","Se ha creado el nuevo registro con exito")
            else:
                showerror("Error en campos obligatorios","Es necesario completar el/los campo/os obligatorio/os(*)")
        else:
            print("error en campo nombre_del_fondo")
    @log('base_de_datos.log')
    def borrar(self,tree):
        item_del_treeview = tree.focus()
        id_del_fondo = str(tree.item(item_del_treeview)['text'])
        if item_del_treeview == "":
            showinfo("Treeview","Debe seleccionar un fondo de la tabla de abajo para continuar, luego de haber consultado la ddbb. Gracias")
        elif item_del_treeview != "":
            sql = "DELETE FROM fondos WHERE id = " + id_del_fondo 
            con=self.conexion()
            cursor=con.cursor()
            cursor.execute(sql)
            con.commit()
            self.actualizar_treeview(tree)
            return f"Se ha eliminado de la dd bb el fondo con el siguiente id: {id_del_fondo}"
            showinfo("Base de datos: Actualizacion","Se ha borrado el registro con id "+id_del_fondo +" con exito")
    @log('base_de_datos.log')        
    def modificar(self,nombre_del_fondo,tipo_de_inversion,horizonte,sociedad_gerente,
    sociedad_depositaria,region,cotizado_originalmente,calificacion,
    fecha_de_calificacion,calificadora_de_riesgo,pais_sede,
    tipo_de_activo,estado,bolsa, codigo_cafci,comision_de_ingreso,	 
    honorarios_de_administracion,comision_de_egreso,comision_de_transferencia,
    gastos_ordinarios_de_gestion,cobra_comision_por_desempeno,
    inversion_minima,plazo_de_liquidacion, tree):
        item_del_treeview = tree.focus()
        id_del_fondo_a_modificar = str(tree.item(item_del_treeview)['text'])
        if item_del_treeview == "":
            showinfo("Treeview","Debe seleccionar un fondo de la tabla de abajo para continuar, luego de haber consultado la ddbb. Gracias")
        elif item_del_treeview != "":
            if askyesno("Modificar registro de la ddbb","¿Esta seguro que desea modificar el registro?"):
                if nombre_del_fondo !="" and tipo_de_inversion !="" and sociedad_gerente !="" and sociedad_depositaria !="" and codigo_cafci !="":
                    con = self.conexion()
                    cursor = con.cursor()
                    data = (nombre_del_fondo, tipo_de_inversion, horizonte, sociedad_gerente,
                            sociedad_depositaria, region, cotizado_originalmente, calificacion,
                            fecha_de_calificacion, calificadora_de_riesgo, pais_sede,
                            tipo_de_activo, estado, bolsa, codigo_cafci, comision_de_ingreso,	 
                            honorarios_de_administracion, comision_de_egreso, comision_de_transferencia,
                            gastos_ordinarios_de_gestion, cobra_comision_por_desempeno,
                            inversion_minima, plazo_de_liquidacion)
                    sql = """UPDATE fondos
                           SET nombre_del_fondo =?,
                               tipo_de_inversion = ?,
                               horizonte = ?,
                               sociedad_gerente = ?,
                               sociedad_depositaria  = ?,
                               region  = ?,
                               cotizado_originalmente  = ?,
                               calificacion  = ?,
                               fecha_de_calificacion  = ?,
                               calificadora_de_riesgo  = ?,
                               pais_sede  = ?,
                               tipo_de_activo  = ?,
                               estado  = ?,
                               bolsa  = ?,
                               codigo_cafci  = ?,
                               comision_de_ingreso  = ?,
                               honorarios_de_administracion  = ?,
                               comision_de_egreso  = ?,
                               comision_de_transferencia  = ?,
                               gastos_ordinarios_de_gestion  = ?,
                               cobra_comision_por_desempeno  = ?,
                               inversion_minima  = ?,
                               plazo_de_liquidacion  = ?
                           WHERE id = """ + id_del_fondo_a_modificar
                    cursor.execute(sql, data)
                    con.commit()
                    self.actualizar_treeview(tree)
                    return f"Se ha modificado el fondo con el id {id_del_fondo_a_modificar} con los siguiente datos: {data}"
                    showinfo("Base de datos: Actualizacion",
                             "Se ha modificado el registro con id " + id_del_fondo_a_modificar + " con exito")
                else:
                    showerror("Error en campos obligatorios", "Es necesario completar el/los campo/os obligatorio/os(*)")
            else:
                showinfo("Modificar registro de la ddbb", "Gracias por su tiempo")

    def consulta(self, tree):
        self.actualizar_treeview(tree)
