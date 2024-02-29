# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 08:04:12 2023
@author: ramarilla
"""
from tkinter import Label
from tkinter import StringVar
from tkinter import DoubleVar
from tkinter import IntVar
from tkinter import Entry
from tkinter import ttk
from tkinter import Button
from tkinter import Menu
from base_de_datos import BaseDeDatos
from modelo import Modelo
# from base_de_datos import conexion
# from base_de_datos import crear_tabla
# from base_de_datos import alta
# from base_de_datos import borrar
# from base_de_datos import modificar
# from modelo import actualizar_treeview
# from modelo import actualizar_treeview2
# from modelo import simulacion_cotizaciones_del_fondo
# from modelo import actualizar_treeview3

mi_base_de_datos = BaseDeDatos()

# ##############################################
# VISTA
# ##############################################


class VistaPrincipal():

    def __init__(self, root):
        root.title("Sistema de análisis de Fondos Común de Inversión(FCI)")
        titulo = Label(root, text="Ingrese datos del FCI para crear el nuevo registro",
                       bg="DarkOrchid3", fg="thistle1", height=1, width=60)
        titulo.grid(row=0, column=0, columnspan=4,
                    padx=1, pady=1, sticky="w"+"e")
        self.mi_modelo = Modelo()
        menubar = Menu(root)
        menu_archivo = Menu(menubar, tearoff=0)
        menu_archivo.add_command(label="Abrir", command=self.mi_modelo.hola)
        menu_archivo.add_command(label="Guardar", command=self.mi_modelo.hola)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=root.quit)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)
        menu_datos = Menu(menubar, tearoff=0)
        menu_datos.add_command(label="Impotar datos desde Excel",
                               command=self.mi_modelo.hola)
        menu_datos.add_command(label="Importar datos desde .txt",
                               command=self.mi_modelo.hola)
        menu_datos.add_command(label="Conectar a base de datos",
                               command=self.mi_modelo.hola)
        menu_datos.add_separator()
        menu_datos.add_command(label="Salir", command=root.quit)
        menubar.add_cascade(label="Datos", menu=menu_datos)
        menu_ayuda = Menu(menubar, tearoff=0)
        menu_ayuda.add_command(label="Consultar manual",
                               command=self.mi_modelo.hola)
        menu_ayuda.add_command(label="Actualizaciones de la App",
                               command=self.mi_modelo.hola)
        menu_ayuda.add_command(label="Acerca de los datos",
                               command=self.mi_modelo.hola)
        menu_ayuda.add_separator()
        menu_ayuda.add_command(label="Salir", command=root.quit)
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)
        root.config(menu=menubar)
        etiqueta1 = Label(root, text="nombre_del_fondo*", fg='#f00')
        etiqueta1.grid(row=1, column=0, sticky="w")
        etiqueta2 = Label(root, text="tipo_de_inversion*", fg='#f00')
        etiqueta2.grid(row=2, column=0, sticky="w")
        etiqueta3 = Label(root, text="horizonte")
        etiqueta3.grid(row=3, column=0, sticky="w")
        etiqueta4 = Label(root, text="sociedad_gerente*", fg='#f00')
        etiqueta4.grid(row=4, column=0, sticky="w")
        etiqueta5 = Label(root, text="sociedad_depositaria*", fg='#f00')
        etiqueta5.grid(row=5, column=0, sticky="w")
        etiqueta6 = Label(root, text="region")
        etiqueta6.grid(row=6, column=0, sticky="w")
        etiqueta7 = Label(root, text="cotizado_originalmente")
        etiqueta7.grid(row=7, column=0, sticky="w")
        etiqueta8 = Label(root, text="calificacion")
        etiqueta8.grid(row=8, column=0, sticky="w")
        etiqueta9 = Label(root, text="fecha_de_calificacion")
        etiqueta9.grid(row=9, column=0, sticky="w")
        etiqueta10 = Label(root, text="calificadora_de_riesgo")
        etiqueta10.grid(row=10, column=0, sticky="w")
        etiqueta11 = Label(root, text="pais_sede")
        etiqueta11.grid(row=11, column=0, sticky="w")
        etiqueta12 = Label(root, text="tipo_de_activo")
        etiqueta12.grid(row=12, column=0, sticky="w")
        etiqueta13 = Label(root, text="estado")
        etiqueta13.grid(row=13, column=0, sticky="w")
        etiqueta14 = Label(root, text="bolsa")
        etiqueta14.grid(row=14, column=0, sticky="w")
        etiqueta15 = Label(root, text="codigo_cafci*", fg='#f00')
        etiqueta15.grid(row=15, column=0, sticky="w")
        etiqueta16 = Label(root, text="comision_de_ingreso")
        etiqueta16.grid(row=16, column=0, sticky="w")
        etiqueta17 = Label(root, text="honorarios_de_administracion")
        etiqueta17.grid(row=17, column=0, sticky="w")
        etiqueta18 = Label(root, text="comision_de_egreso")
        etiqueta18.grid(row=18, column=0, sticky="w")
        etiqueta19 = Label(root, text="comision_de_transferencia")
        etiqueta19.grid(row=19, column=0, sticky="w")
        etiqueta20 = Label(root, text="gastos_ordinarios_de_gestion")
        etiqueta20.grid(row=20, column=0, sticky="w")
        etiqueta21 = Label(root, text="cobra_comision_por_desempeno")
        etiqueta21.grid(row=21, column=0, sticky="w")
        etiqueta22 = Label(root, text="inversion_minima")
        etiqueta22.grid(row=22, column=0, sticky="w")
        etiqueta23 = Label(root, text="plazo_de_liquidacion")
        etiqueta23.grid(row=23, column=0, sticky="w")
        etiqueta24 = Label(root, text="Seleccionar id para realizar una consulta especifica")
        etiqueta24.grid(row=33, column=0, sticky="w")
        etiqueta25 = Label(root, text="Seleccionar la cantidad de años " +
                           "del análisis de rentabilidad del fondo")
        etiqueta25.grid(row=34, column=0, sticky="w")
        # Defino variables para tomar valores de campos de entrada
        nombre_del_fondo = StringVar()
        tipo_de_inversion = StringVar()
        horizonte = StringVar()
        sociedad_gerente = StringVar()
        sociedad_depositaria = StringVar()
        region = StringVar()
        cotizado_originalmente = StringVar()
        calificacion = StringVar()
        fecha_de_calificacion = StringVar()
        calificadora_de_riesgo = StringVar()
        pais_sede = StringVar()
        tipo_de_activo = StringVar()
        estado = StringVar()
        bolsa = StringVar()
        codigo_cafci = StringVar()
        comision_de_ingreso = DoubleVar()
        honorarios_de_administracion = DoubleVar()
        comision_de_egreso = DoubleVar()
        comision_de_transferencia = DoubleVar()
        gastos_ordinarios_de_gestion = DoubleVar()
        cobra_comision_por_desempeno = DoubleVar()
        inversion_minima = DoubleVar()
        plazo_de_liquidacion = StringVar()
        id_consulta_especifica = StringVar()
        numero_de_años = IntVar()
        w_ancho = 20
        entrada1 = Entry(root, textvariable=nombre_del_fondo, width=w_ancho)
        entrada1.grid(row=1, column=1)
        entrada2 = ttk.Combobox(root, textvariable=tipo_de_inversion, width=w_ancho)
        entrada2['values'] = ["Renta Fija", "Renta Variable", "Renta Mixta",
                              "Mercado de Dinero", "Pymes", "Total Return", "Otro"]
        entrada2['state'] = 'readonly'
        entrada2.grid(row=2, column=1)
        entrada3 = ttk.Combobox(root, textvariable=horizonte, width =w_ancho)
        entrada3['values'] = ["Corto Plazo", "Mediano Plazo", "Largo Plazo",
                              "Flexible", "Sin asignar", "Otro"]
        entrada3['state'] = 'readonly'
        entrada3.grid(row =3, column=1)
        entrada4 = ttk.Combobox(root, textvariable=sociedad_gerente, width=w_ancho)
        entrada4['values'] = [
                              "Balanz S.G.F.C.I.S.A.",
                              "Santander Rio Asset Management G.F.C.I.S.A.",
                              "ICBC Investments Argentina S.A.U.S.G.F.C.I.",
                              "Mega QM S.A.",
                              "Allaria Ledesma Fondos Administrados S.G.F.C.I.S.A.",
                              "StoneX Asset Management S.A.",
                              "Delta Asset Management S.A.",
                              "Adcap Asset Management S.G.F.C.I.S.A.",
                              "SBS Asset Management S.A.S.G.F.C.I.",
                              "Argenfunds S.A.",
                              "Southern Trust S.G.F.C.I.S.A.",
                              "Investis Asset Management S.A.S.G.F.C.I.",
                              "Schroder S.A.S.G.F.C.I.",
                              "Supervielle Asset Management S.A.S.G.F.C.I.",
                              "Consultatio Asset Management G.F.C.I.S.A.",
                              "Industrial Asset Management S.G.F.C.I.S.A.",
                              "HSBC Administradora de Inversiones S.A.S.G.F.C.I.",
                              "Galicia Administradora de Fondos S.A.S.G.F.C.I.",
                              "Macro Fondos S.G.F.C.I.S.A.",
                              "Mariva Asset Management S.A.U.S.G.F.C.I.",
                              "Axis S.G.F.C.I.S.A.",
                              "BACS Administradora de Activos S.A.S.G.F.C.I.",
                              "Zofingen Investment S.A.",
                              "BNP Paribas Asset Management Arg. S.A.S.G.F.C.I.",
                              "BBVA Asset Management Argentina S.A.G.F.C.I.",
                              "Galileo Argentina S.G.F.C.I.S.A.",
                              "Itau Asset Management S.A.S.G.F.C.I.",
                              "First Capital Markets S.A.",
                              "IEB S.A.",
                              "Novus Asset Management S.A.",
                              "Capital Markets Argentina S.G.F.C.I.S.A.",
                              "Cohen S.A.",
                              "Pellegrini S.A.S.G.F.C.I.",
                              "Alamerica S.G.F.C.I.S.A.",
                              "Cima S.G.F.C.I.S.A.",
                              "Frances Administradora de Inversiones S.A.G.F.C.I.",
                              "Bancor Fondos S.G.F.C.I.S.A.U.",
                              "Max Capital Asset Management S.A.",
                              "CMF Asset Management S.A.U.",
                              "Quiron Asset Management S.A.",
                              "Patagonia Inversora S.A.S.G.F.C.I.",
                              "Valiant Asset Management S.G.F.C.I.S.A.U.",
                              "QM Asset Management S.G.F.C.I.S.A",
                              "Nuevo Chaco Fondos S.A.S.G.F.C.I.",
                              "Grupo SS S.A.S.G.F.C.I.",
                              "Standard Investments S.A.S.G.F.C.I.",
                              "Mercofond S.G.F.C.I.S.A.",
                              "Deal S.A.",
                              "Magna Asset Management S.A.",
                              "Provinfondos S.A.S.G.F.C.I.",
                              "C y C Administradora de Fondos S.A.",
                              "Proahorro Administradora de Activos S.A.",
                              "Dracma S.A.",
                              "Tavelli y Cia. S.A.",
                              "Bull Market Asset Management S.A.",
                              "BAVSA Fondos S.A.",
                              "Puente Hnos Adm. De Invers. S.A.S.G.F.C.I.",
                              "Ualintec Inversiones S.A.U.S.G.F.C.I.",
                              "MBA Asset Management S.G.F.C.I.S.A.",
                              "Nativa S.G.F.C.I.S.A.",
                              "Administradora de Titulos y Valores S.A.S.G.F.C.I.",
                              "Banespa S.A.S.G.F.C.I.",
                              "Tutelar Inversora S.A.",
                              "BBVA Frances Asset Management S.A.G.F.C.I.",
                              "Proahorro Administradora de Activos S.A.S.G.F.C.I.",
                              "Fondcapital S.A.S.G.F.C.I.",
                              "Bayfe S.A.S.G.F.C.I.",
                              "Safimar S.A.S.G.F.C.I."
                             ]
        entrada4['state'] = 'readonly'
        entrada4.grid(row=4, column=1)
        entrada5 = ttk.Combobox(root, textvariable=sociedad_depositaria, width=w_ancho)
        entrada5['values'] = [
                              "Banco de Valores S.A.",
                              "Banco Comafi S.A.",
                              "Banco Macro S.A.",
                              "Banco Santander Rio S.A.",
                              "ICBC (Arg) S.A.",
                              "Banco Supervielle S.A.",
                              "Banco Industrial S.A.",
                              "Banco de Galicia y Buenos Aires S.A.",
                              "HSBC Bank Argentina S.A.",
                              "Banco Mariva S.A.",
                              "Banco Credito y Securitizacion S.A.",
                              "BBVA Argentina S.A.",
                              "Banco de Servicios y Transacciones S.A.",
                              "BNP Paribas",
                              "Banco Itau Argentina S.A.",
                              "Banco de La Nación Argentina",
                              "BBVA Banco Frances S.A.",
                              "Banco de Cordoba S.A.",
                              "Banco C.M.F.S.A.",
                              "Banco Patagonia S.A.",
                              "Nuevo Banco del Chaco S.A.",
                              "Standard Bank Argentina S.A.",
                              "Banco Credicoop Coop. Ltdo.",
                              "Banco Provincia de Buenos Aires",
                              "Deutsche Bank S.A.",
                              "MBA Lazard Banco de Inversiones S.A.",
                              "Banco de la Provincia de Cordoba S.A.",
                              "Banco Ciudad de Buenos Aires",
                              "HSBC Bank Argentina S.A.(por fusión con BNL S.A.)",
                              "Custodia Soc. Depositaria FCI S.A.",
                              "Banco Piano S.A.",
                              "Sodefon S.A."
                             ]
        entrada5['state'] = 'readonly'
        entrada5.grid(row=5, column=1)
        entrada6 = ttk.Combobox(root, textvariable=region, width=w_ancho)
        entrada6['values'] = [
                              "Argentina",
                              "Global",
                              "Latinoamerica",
                              "EEUU",
                              "Brasil",
                              "Europa"
                              ]
        entrada6['state'] = 'readonly'
        entrada6.grid(row=6, column=1)
        entrada7 = ttk.Combobox(root, textvariable=cotizado_originalmente, width=w_ancho)
        entrada7['values'] = [
                              "Peso Argentina",
                              "Dollar US",
                              "Euro"
                              ]
        entrada7['state'] = 'readonly'
        entrada7.grid(row=7, column=1)
        entrada8 = Entry(root, textvariable=calificacion, width=w_ancho)
        entrada8.grid(row=8, column=1)
        entrada9 = Entry(root, textvariable=fecha_de_calificacion, width=w_ancho)
        entrada9.grid(row=9, column=1)
        entrada10 = ttk.Combobox(root, textvariable=calificadora_de_riesgo, width=w_ancho)
        entrada10['values'] = [
                              "No Registra",
                              "FIX SCR S.A.",
                              "Moody's Local Calif. Riesgo",
                              "Standard & Poor's International Ratings, Llc. Sucursal Argentina",
                              "Moody's Latin America Calificadora S.A.",
                              "Fitch Argentina Calificadora de Riesgo S.A.",
                              "Professional Rating Services ACR S.A.",
                              "Univ. Nac. de Tres de Febrero",
                              "Evaluadora Latinoamericana S.A. Calificadora de Riesgo"
                               ]
        entrada10['state'] = 'readonly'
        entrada10.grid(row=10, column=1)
        entrada11 = ttk.Combobox(root, textvariable=pais_sede, width=w_ancho)
        entrada11['values'] = [
                              "Argentina",
                              "Brasil",
                              "EE UU"
                               ]
        entrada11['state'] = 'readonly'
        entrada11.grid(row=11, column=1)
        entrada12 = ttk.Combobox(root, textvariable=tipo_de_activo, width=w_ancho)
        entrada12['values'] = [
                              "Fondo Mutuo Abierto",
                              "Fondo Cerrado",
                              "ETF",
                              "Otro"
                             ]
        entrada12['state'] = 'readonly'
        entrada12.grid(row=12, column=1)
        entrada13 = ttk.Combobox(root, textvariable=estado, width=w_ancho)
        entrada13['values'] = [
                              "Activo",
                              "Cancelado",
                              ]
        entrada13['state'] = 'readonly'
        entrada13.grid(row=13, column=1)
        entrada14 = ttk.Combobox(root, textvariable=bolsa, width=w_ancho)
        entrada14['values'] = [
                              "BYMA",
                              "NASDAQ",
                              "NYSE",
                              "AMEX",
                              "BOVESPA",
                              "Otro"
                              ]
        entrada14['state'] = 'readonly'
        entrada14.grid(row=14, column=1)
        entrada15 = Entry(root, textvariable=codigo_cafci, width=w_ancho)
        entrada15.grid(row=15, column=1)
        entrada16 = Entry(root, textvariable=comision_de_ingreso, width=w_ancho)
        entrada16.grid(row=16, column=1)
        entrada17 = Entry(root, textvariable=honorarios_de_administracion, width=w_ancho)
        entrada17.grid(row=17, column=1)
        entrada18 = Entry(root, textvariable=comision_de_egreso, width=w_ancho)
        entrada18.grid(row=18, column=1)
        entrada19 = Entry(root, textvariable=comision_de_transferencia, width=w_ancho)
        entrada19.grid(row=19, column=1)
        entrada20 = Entry(root, textvariable=gastos_ordinarios_de_gestion, width=w_ancho)
        entrada20.grid(row=20, column=1)
        entrada21 = Entry(root, textvariable=cobra_comision_por_desempeno, width=w_ancho)
        entrada21.grid(row=21, column=1)
        entrada22 = Entry(root, textvariable=inversion_minima, width=w_ancho)
        entrada22.grid(row=22, column=1)
        entrada23 = ttk.Combobox(root, textvariable=plazo_de_liquidacion, width=w_ancho)
        entrada23['values'] = [
                              "48hs",
                              "24hs",
                              "72hs",
                              "0hs",
                              "120hs",
                              "96hs",
                              "360hs",
                              "168hs"
                               ]
        entrada23['state'] = 'readonly'
        entrada23.grid(row=23, column=1)
        entrada24 = ttk.Combobox(root, textvariable=id_consulta_especifica, width=w_ancho)
        listado_de_ids = self.mi_modelo.listado_de_ids()
        entrada24['values'] = listado_de_ids
        entrada24['state'] = 'readonly'
        entrada24.grid(row=33, column=1)
        entrada25 = ttk.Combobox(root, textvariable=numero_de_años, width=w_ancho)
        entrada25['values'] = [
                              10,
                              15,
                              20,
                              25,
                              30,
                              35,
                              40,
                              50,
                              100
                             ]
        entrada25['state'] = 'readonly'
        entrada25.grid(row=34, column=1)

        # --------------------------------------------------
        # TREEVIEW
        # --------------------------------------------------

        tree = ttk.Treeview(root)
        tree["columns"] = ("col1", "col2", "col3")
        tree.column("#0", width=90, minwidth=20)
        tree.column("col1", width=200, minwidth=20)
        tree.column("col2", width=200, minwidth=20)
        tree.column("col3", width=200, minwidth=20)
        tree.heading("#0", text="ID")
        tree.heading("col1", text="nombre_del_fondo")
        tree.heading("col2", text="tipo_de_inversion")
        tree.heading("col3", text="codigo_cafci")
        tree.grid(row=25, column=0, columnspan=4, rowspan=4)
        tree2 = ttk.Treeview(root)
        tree2["columns"] = ("col11", "col21", "col31")
        tree2.column("#0", width=250, minwidth=20)
        tree2.column("col11", width=250, minwidth=20)
        tree2.column("col21", width=200, minwidth=20)
        tree2.column("col31", width=200, minwidth=20)
        tree2.heading("#0", text="Campo")
        tree2.heading("col11", text="Variable")
        tree2.heading("col21", text="Rentabilidad")
        tree2.heading("col31", text="Tasa %")
        tree2.grid(row=36, column=0, columnspan=4, rowspan=23)

        def clear_text():
            entrada1.delete(0, 'end')
            entrada2.set('')
            entrada3.set('')
            entrada4.set('')
            entrada5.set('')
            entrada6.set('')
            entrada7.set('')
            entrada8.delete(0, 'end')
            entrada9.delete(0, 'end')
            entrada10.set('')
            entrada11.set('')
            entrada12.set('')
            entrada13.set('')
            entrada14.set('')
            entrada15.delete(0, 'end')
            entrada16.delete(0, 'end')
            entrada17.delete(0, 'end')
            entrada18.delete(0, 'end')
            entrada19.delete(0, 'end')
            entrada20.delete(0, 'end')
            entrada21.delete(0, 'end')
            entrada22.delete(0, 'end')
            entrada23.set('')
  
        def alta_sofisticado(nombre_del_fondo,
                             tipo_de_inversion,
                             horizonte,
                             sociedad_gerente,
                             sociedad_depositaria,
                             region,
                             cotizado_originalmente,
                             calificacion,
                             fecha_de_calificacion,
                             calificadora_de_riesgo,
                             pais_sede,
                             tipo_de_activo,
                             estado,
                             bolsa,
                             codigo_cafci,
                             comision_de_ingreso,
                             honorarios_de_administracion,
                             comision_de_egreso,
                             comision_de_transferencia,
                             gastos_ordinarios_de_gestion,
                             cobra_comision_por_desempeno,
                             inversion_minima,
                             plazo_de_liquidacion, tree):
            mi_base_de_datos.alta(nombre_del_fondo,
                                  tipo_de_inversion,
                                  horizonte,
                                  sociedad_gerente,
                                  sociedad_depositaria,
                                  region,
                                  cotizado_originalmente,
                                  calificacion,
                                  fecha_de_calificacion,
                                  calificadora_de_riesgo,
                                  pais_sede,
                                  tipo_de_activo,
                                  estado,
                                  bolsa,
                                  codigo_cafci,
                                  comision_de_ingreso,
                                  honorarios_de_administracion,
                                  comision_de_egreso,
                                  comision_de_transferencia,
                                  gastos_ordinarios_de_gestion,
                                  cobra_comision_por_desempeno,
                                  inversion_minima,
                                  plazo_de_liquidacion, tree)
            clear_text()

        def modificar_sofisticado(nombre_del_fondo,
                                  tipo_de_inversion,
                                  horizonte,
                                  sociedad_gerente,
                                  sociedad_depositaria,
                                  region,
                                  cotizado_originalmente,
                                  calificacion,
                                  fecha_de_calificacion,
                                  calificadora_de_riesgo,
                                  pais_sede,
                                  tipo_de_activo,
                                  estado,
                                  bolsa,
                                  codigo_cafci,
                                  comision_de_ingreso,
                                  honorarios_de_administracion,
                                  comision_de_egreso,
                                  comision_de_transferencia,
                                  gastos_ordinarios_de_gestion,
                                  cobra_comision_por_desempeno,
                                  inversion_minima,
                                  plazo_de_liquidacion, tree):
            mi_base_de_datos.modificar(nombre_del_fondo,
                                       tipo_de_inversion,
                                       horizonte,
                                       sociedad_gerente,
                                       sociedad_depositaria,
                                       region,
                                       cotizado_originalmente,
                                       calificacion,
                                       fecha_de_calificacion,
                                       calificadora_de_riesgo,
                                       pais_sede,
                                       tipo_de_activo,
                                       estado,
                                       bolsa,
                                       codigo_cafci,
                                       comision_de_ingreso,
                                       honorarios_de_administracion,
                                       comision_de_egreso,
                                       comision_de_transferencia,
                                       gastos_ordinarios_de_gestion,
                                       cobra_comision_por_desempeno,
                                       inversion_minima,
                                       plazo_de_liquidacion, tree)
            clear_text()


        boton_alta = Button(root, text="Alta de registro en ddbb",
                            command=lambda : alta_sofisticado(nombre_del_fondo.get(),
                                                              tipo_de_inversion.get(),
                                                              horizonte.get(),
                                                              sociedad_gerente.get(),
                                                              sociedad_depositaria.get(),
                                                              region.get(),
                                                              cotizado_originalmente.get(),
                                                              calificacion.get(),
                                                              fecha_de_calificacion.get(),
                                                              calificadora_de_riesgo.get(),
                                                              pais_sede.get(),
                                                              tipo_de_activo.get(),
                                                              estado.get(),
                                                              bolsa.get(),
                                                              codigo_cafci.get(),
                                                              comision_de_ingreso.get(),
                                                              honorarios_de_administracion.get(),
                                                              comision_de_egreso.get(),
                                                              comision_de_transferencia.get(),
                                                              gastos_ordinarios_de_gestion.get(),
                                                              cobra_comision_por_desempeno.get(),
                                                              inversion_minima.get(),
                                                              plazo_de_liquidacion.get(), tree))
        boton_alta.grid(row=1, column=2, sticky="ew")
        boton_consulta = Button(root, text="Consulta de la ddbb",
                                command=lambda:mi_base_de_datos.consulta(tree))
        boton_consulta.grid(row=2, column=2, sticky="ew")
        boton_modificar = Button(root, text="Modificar registro en ddbb",
                                command=lambda:modificar_sofisticado(nombre_del_fondo.get(),
                                                                     tipo_de_inversion.get(),
                                                                     horizonte.get(),
                                                                     sociedad_gerente.get(),
                                                                     sociedad_depositaria.get(),
                                                                     region.get(),
                                                                     cotizado_originalmente.get(),
                                                                     calificacion.get(),
                                                                     fecha_de_calificacion.get(),
                                                                     calificadora_de_riesgo.get(),
                                                                     pais_sede.get(),
                                                                     tipo_de_activo.get(),
                                                                     estado.get(),
                                                                     bolsa.get(),
                                                                     codigo_cafci.get(),
                                                                     comision_de_ingreso.get(),
                                                                     honorarios_de_administracion.get(),
                                                                     comision_de_egreso.get(),
                                                                     comision_de_transferencia.get(),
                                                                     gastos_ordinarios_de_gestion.get(),
                                                                     cobra_comision_por_desempeno.get(),
                                                                     inversion_minima.get(),
                                                                     plazo_de_liquidacion.get(), tree))
        boton_modificar.grid(row=3, column=2, sticky="ew")
        boton_borrar = Button(root, text="Baja de registro de la ddbb",
                              command=lambda:mi_base_de_datos.borrar(tree))
        boton_borrar.grid(row=4, column=2, sticky="ew")
        boton_limpiar = Button(root, text="Limpiar tabla",
                              command=lambda:self.mi_modelo.limpiar_treeview(tree))
        boton_limpiar.grid(row=5, column=2, sticky="ew")
        boton_consulta_especifica=Button(root, text="Consulta y Analisis del fondo",
                                        command=lambda:self.mi_modelo.consultar_especifica(id_consulta_especifica.get(),
                                                                                           numero_de_años.get(),
                                                                                           tree2, root))
        boton_consulta_especifica.grid(row=33, column=2, sticky="ew")
