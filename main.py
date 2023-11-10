import kivy
import os
import sqlite3
# #CONFIGURACION GRAFICA
from kivy.config import Config
Config.set("input","mouse","mouse,multitouch_on_demand")
# Config.set("graphics","width","340")
# Config.set("graphics","hight","640")
# #CONFIGURACION GRAFICA

from kivy.app import App
from kivymd.app import MDApp
#from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg 
from kivy.core.audio import SoundLoader
from playsound import playsound
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.clock import Clock
from datetime import date, datetime
from time import strftime
from time import sleep 
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
import sqlite3

##FIN LIBRERIAS*******************************************
#CONFIGURACION TECLADO
Window.keyboard_anim_args={"d":.2,"t":"in_out_expo"}
Window.softinput_mode="below_target"
#CONFIGURACION TECLADO
#*********FECHA Y HORA**********************************
fechain=date.today()
fechafi=date.today()
format_hora="%H:%M:%S"
format_fecha="%Y-%m-%d"
horain=datetime.now().time().strftime(format_hora)
horafi=datetime.now().time().strftime(format_hora)
#*********FECHA Y HORA**********************************

#**********CREA Y CONECTAR BASE DE DATO****************
#******************************************************

#******************************************************
#********INICIO*******SESION MUSCULAR******************
#******************************************************

#**************************PECHO*****************************************
def connect_to_database_pecho(path):
    con = sqlite3.connect(path)
    cursor = con.cursor()
    create_table_pecho(cursor)
    con.commit()
    con.close()
def create_table_pecho(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS PECHO(ID INT PRIMARY KEY NOT NULL, ARTICULAR TEXT NOT NULL, MODO TEXT NOT NULL, ABRV TEXT NOT NULL, EJERCICIO TEXT NOT NULL, RM FLOAT NOT NULL, 
                    PEC FLOAT NULL, ESP FLOAT NULL, ABD FLOAT NULL, HOM FLOAT NULL, BIC FLOAT NULL, TRI FLOAT NULL, ANT FLOAT NULL, CUA FLOAT NULL, ISQ FLOAT NULL, ABDU FLOAT NULL, PAN FLOAT NULL, GLU FLOAT NULL
                )''')
                    
#**************************PECHO*****************************************
#**************************ESPALDA*****************************************
def connect_to_database_espalda(path):
    con = sqlite3.connect(path)
    cursor = con.cursor()
    create_table_espalda(cursor)
    con.commit()
    con.close()
def create_table_espalda(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS ESPALDA(ID INT PRIMARY KEY NOT NULL, ARTICULAR TEXT NOT NULL, MODO TEXT NOT NULL, ABRV TEXT NOT NULL, EJERCICIO TEXT NOT NULL, RM FLOAT NOT NULL,  
                    PEC FLOAT NULL, ESP FLOAT NULL, ABD FLOAT NULL, HOM FLOAT NULL, BIC FLOAT NULL, TRI FLOAT NULL, ANT FLOAT NULL, CUA FLOAT NULL, ISQ FLOAT NULL, ABDU FLOAT NULL, PAN FLOAT NULL, GLU FLOAT NULL
                )''')
#**************************ESPALDA*****************************************
#**************************ABDOMEN*****************************************
def connect_to_database_abdomen(path):
    con = sqlite3.connect(path)
    cursor = con.cursor()
    create_table_abdomen(cursor)
    con.commit()
    con.close()
def create_table_abdomen(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS ABDOMEN(ID INT PRIMARY KEY NOT NULL, ARTICULAR TEXT NOT NULL, MODO TEXT NOT NULL, ABRV TEXT NOT NULL, EJERCICIO TEXT NOT NULL, RM FLOAT NOT NULL,  
                    PEC FLOAT NULL, ESP FLOAT NULL, ABD FLOAT NULL, HOM FLOAT NULL, BIC FLOAT NULL, TRI FLOAT NULL, ANT FLOAT NULL, CUA FLOAT NULL, ISQ FLOAT NULL, ABDU FLOAT NULL, PAN FLOAT NULL, GLU FLOAT NULL
                )''')
#**************************ABDOMEN*****************************************
#**************************HOMBRO*****************************************
def connect_to_database_hombro(path):
    con = sqlite3.connect(path)
    cursor = con.cursor()
    create_table_hombro(cursor)
    con.commit()
    con.close()
def create_table_hombro(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS HOMBRO(ID INT PRIMARY KEY NOT NULL, ARTICULAR TEXT NOT NULL, MODO TEXT NOT NULL, ABRV TEXT NOT NULL, EJERCICIO TEXT NOT NULL, RM FLOAT NOT NULL, 
                    PEC FLOAT NULL, ESP FLOAT NULL, ABD FLOAT NULL, HOM FLOAT NULL, BIC FLOAT NULL, TRI FLOAT NULL, ANT FLOAT NULL, CUA FLOAT NULL, ISQ FLOAT NULL, ABDU FLOAT NULL, PAN FLOAT NULL, GLU FLOAT NULL
                )''')
#**************************HOMBRO*****************************************
#**************************BICEP*****************************************
def connect_to_database_bicep(path):
    con = sqlite3.connect(path)
    cursor = con.cursor()
    create_table_bicep(cursor)
    con.commit()
    con.close()
def create_table_bicep(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS BICEP(ID INT PRIMARY KEY NOT NULL, ARTICULAR TEXT NOT NULL, MODO TEXT NOT NULL, ABRV TEXT NOT NULL, EJERCICIO TEXT NOT NULL, RM FLOAT NOT NULL, 
                    PEC FLOAT NULL, ESP FLOAT NULL, ABD FLOAT NULL, HOM FLOAT NULL, BIC FLOAT NULL, TRI FLOAT NULL, ANT FLOAT NULL, CUA FLOAT NULL, ISQ FLOAT NULL, ABDU FLOAT NULL, PAN FLOAT NULL, GLU FLOAT NULL
                )''')
#**************************BICEP*****************************************
#**************************TRICEP*****************************************
def connect_to_database_tricep(path):
    con = sqlite3.connect(path)
    cursor = con.cursor()
    create_table_tricep(cursor)
    con.commit()
    con.close()
def create_table_tricep(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS TRICEP(ID INT PRIMARY KEY NOT NULL, ARTICULAR TEXT NOT NULL, MODO TEXT NOT NULL, ABRV TEXT NOT NULL, EJERCICIO TEXT NOT NULL, RM FLOAT NOT NULL, 
                    PEC FLOAT NULL, ESP FLOAT NULL, ABD FLOAT NULL, HOM FLOAT NULL, BIC FLOAT NULL, TRI FLOAT NULL, ANT FLOAT NULL, CUA FLOAT NULL, ISQ FLOAT NULL, ABDU FLOAT NULL, PAN FLOAT NULL, GLU FLOAT NULL
                )''')
#**************************TRICEP*****************************************
#**************************ANTEBRAZO*****************************************
def connect_to_database_antebrazo(path):
    con = sqlite3.connect(path)
    cursor = con.cursor()
    create_table_antebrazo(cursor)
    con.commit()
    con.close()
def create_table_antebrazo(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS ANTEBRAZO(ID INT PRIMARY KEY NOT NULL, ARTICULAR TEXT NOT NULL, MODO TEXT NOT NULL, ABRV TEXT NOT NULL, EJERCICIO TEXT NOT NULL, RM FLOAT NOT NULL, 
                    PEC FLOAT NULL, ESP FLOAT NULL, ABD FLOAT NULL, HOM FLOAT NULL, BIC FLOAT NULL, TRI FLOAT NULL, ANT FLOAT NULL, CUA FLOAT NULL, ISQ FLOAT NULL, ABDU FLOAT NULL, PAN FLOAT NULL, GLU FLOAT NULL
                )''')
#**************************ANTEBRAZO*****************************************
#**************************CUADRICEP*****************************************
def connect_to_database_cuadricep(path):
    con = sqlite3.connect(path)
    cursor = con.cursor()
    create_table_cuadricep(cursor)
    con.commit()
    con.close()
def create_table_cuadricep(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS CUADRICEP(ID INT PRIMARY KEY NOT NULL, ARTICULAR TEXT NOT NULL, MODO TEXT NOT NULL, ABRV TEXT NOT NULL, EJERCICIO TEXT NOT NULL, RM FLOAT NOT NULL, 
                    PEC FLOAT NULL, ESP FLOAT NULL, ABD FLOAT NULL, HOM FLOAT NULL, BIC FLOAT NULL, TRI FLOAT NULL, ANT FLOAT NULL, CUA FLOAT NULL, ISQ FLOAT NULL, ABDU FLOAT NULL, PAN FLOAT NULL, GLU FLOAT NULL
                )''')
#**************************CUADRICEP*****************************************
#**************************ISQUIOS*****************************************
def connect_to_database_isquios(path):
    con = sqlite3.connect(path)
    cursor = con.cursor()
    create_table_isquios(cursor)
    con.commit()
    con.close()
def create_table_isquios(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS ISQUIO(ID INT PRIMARY KEY NOT NULL, ARTICULAR TEXT NOT NULL, MODO TEXT NOT NULL, ABRV TEXT NOT NULL, EJERCICIO TEXT NOT NULL, RM FLOAT NOT NULL, 
                    PEC FLOAT NULL, ESP FLOAT NULL, ABD FLOAT NULL, HOM FLOAT NULL, BIC FLOAT NULL, TRI FLOAT NULL, ANT FLOAT NULL, CUA FLOAT NULL, ISQ FLOAT NULL, ABDU FLOAT NULL, PAN FLOAT NULL, GLU FLOAT NULL
                )''')
#**************************ISQUIOS*****************************************
#**************************ABDUCTORES*****************************************
def connect_to_database_abductores(path):
    con = sqlite3.connect(path)
    cursor = con.cursor()
    create_table_abductores(cursor)
    con.commit()
    con.close()    
def create_table_abductores(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS ABDUCTORE(ID INT PRIMARY KEY NOT NULL, ARTICULAR TEXT NOT NULL, MODO TEXT NOT NULL, ABRV TEXT NOT NULL, EJERCICIO TEXT NOT NULL, RM FLOAT NOT NULL, 
                    PEC FLOAT NULL, ESP FLOAT NULL, ABD FLOAT NULL, HOM FLOAT NULL, BIC FLOAT NULL, TRI FLOAT NULL, ANT FLOAT NULL, CUA FLOAT NULL, ISQ FLOAT NULL, ABDU FLOAT NULL, PAN FLOAT NULL, GLU FLOAT NULL
                )''')
#**************************ABDUCTORES*****************************************
#**************************PANTORRILLA*****************************************
def connect_to_database_pantorrilla(path):
    con = sqlite3.connect(path)
    cursor = con.cursor()
    create_table_pantorrilla(cursor)
    con.commit()
    con.close()
def create_table_pantorrilla(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS PANTORRILLA(ID INT PRIMARY KEY NOT NULL, ARTICULAR TEXT NOT NULL, MODO TEXT NOT NULL, ABRV TEXT NOT NULL, EJERCICIO TEXT NOT NULL, RM FLOAT NOT NULL, 
                    PEC FLOAT NULL, ESP FLOAT NULL, ABD FLOAT NULL, HOM FLOAT NULL, BIC FLOAT NULL, TRI FLOAT NULL, ANT FLOAT NULL, CUA FLOAT NULL, ISQ FLOAT NULL, ABDU FLOAT NULL, PAN FLOAT NULL, GLU FLOAT NULL
                )''')
#**************************PANTORRILLA*****************************************
#**************************GLUTEO*****************************************
def connect_to_database_gluteo(path):
    con = sqlite3.connect(path)
    cursor = con.cursor()
    create_table_gluteo(cursor)
    con.commit()
    con.close()
def create_table_gluteo(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS GLUTEO(ID INT PRIMARY KEY NOT NULL, ARTICULAR TEXT NOT NULL, MODO TEXT NOT NULL, ABRV TEXT NOT NULL, EJERCICIO TEXT NOT NULL, RM FLOAT NOT NULL, 
                    PEC FLOAT NULL, ESP FLOAT NULL, ABD FLOAT NULL, HOM FLOAT NULL, BIC FLOAT NULL, TRI FLOAT NULL, ANT FLOAT NULL, CUA FLOAT NULL, ISQ FLOAT NULL, ABDU FLOAT NULL, PAN FLOAT NULL, GLU FLOAT NULL
                )''')
#**************************GLUTEO*****************************************
#**************************SELECCIONE MUSCULO*****************************************
def connect_to_database_seleccione_musculo(path):
    try:
        con = sqlite3.connect(path)
        cursor = con.cursor()
        create_table_seleccione_musculo(cursor)
        con.commit()
        valor=len(cursor.execute("select EJERCICIO from SELECCIONE_MUSCULO").fetchall())
        if valor<=0:
            d1=1
            d2="1"
            d3="1"
            d4="SELECCIONE_EJERCICIO"
            d5="1"
            a=(d1,d2,d3,d4,d5)
            s1 = 'INSERT INTO SELECCIONE_MUSCULO(ID, ARTICULAR, MODO, EJERCICIO, RM)'
            s2 = 'VALUES(%s, "%s", "%s", "%s",%s)' % a
            cursor.execute(s1+' '+s2)
            con.commit()
            con.close()
    except Exception as e:
        print(e)
def create_table_seleccione_musculo(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS SELECCIONE_MUSCULO(ID INT PRIMARY KEY NOT NULL, ARTICULAR TEXT NOT NULL, MODO TEXT NOT NULL, EJERCICIO TEXT NOT NULL, RM TEXT NOT NULL)''')
#**************************SELECCIONE MUSCULO****************************************
#**************************SELECCIONE EJERCICIO*****************************************
def connect_to_database_seleccione_ejercicio(path):
    try:
        con = sqlite3.connect(path)
        cursor = con.cursor()
        create_table_seleccione_ejercicio(cursor)
        con.commit()
        valor=len(cursor.execute("select EJERCICIO from SELECCIONE_EJERCICIO").fetchall())
        if valor<=0:
            d1=1
            d2="1"
            d3="1"
            d4="SELECCIONE_EJERCICIO"
            d5="1"
            a=(d1,d2,d3,d4,d5)
            s1 = 'INSERT INTO SELECCIONE_EJERCICIO(ID, ARTICULAR, MODO, EJERCICIO, RM)'
            s2 = 'VALUES(%s, "%s", "%s", "%s", %s)' % a
            cursor.execute(s1+' '+s2)
            con.commit()
            con.close()
    except Exception as e:
        print(e)
def create_table_seleccione_ejercicio(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS SELECCIONE_EJERCICIO(ID INT PRIMARY KEY NOT NULL, ARTICULAR TEXT NOT NULL, MODO TEXT NOT NULL, EJERCICIO TEXT NOT NULL, RM TEXT NOT NULL)''')
#**************************SELECCIONE EJERCICIO****************************************

#********FIN**********SESION MUSCULAR******************
#******************************************************

#******************************************************
#********INICIO*******SESION EJERCICIO******************
#******************************************************
def connect_to_database_sesion_ejercicio(path):
    con = sqlite3.connect(path)
    cursor = con.cursor()
    create_table_sesion_ejercicio(cursor)
    con.commit()
    con.close()
def create_table_sesion_ejercicio(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS SESION_EJERCICIO(ID INT PRIMARY KEY NOT NULL, FECHA DATE NOT NULL, HORA TIME NOT NULL, FMES TEXT NOT NULL, FSEM TEXT NOT NULL, SESION INT NOT NULL,
                    FSESION TEXT NOT NULL, ANIO INT NOT NULL, SESION_MUSCULAR TEXT NOT NULL, ABRV TEXT NOT NULL, EJERCICIO TEXT NOT NULL, SERIE INT NOT NULL, SERIES INT NOT NULL, PESO FLOAT NOT NULL, 
                    PESOT FLOAT NOT NULL, TT INT NOT NULL, REP INT NOT NULL, REPEFECT INT NOT NULL, RIR INT NOT NULL, RPE INT NOT NULL, DESC INT NOT NULL, TTREP FLOAT NOT NULL, TTSTS FLOAT NOT NULL, 
                    TDES FLOAT NOT NULL, TDUS FLOAT NOT NULL, DSERIE FLOAT NOT NULL, DSESION FLOAT NOT NULL, VOLUMEN INT NOT NULL, RM FLOAT NOT NULL, RM_PORC FLOAT NOT NULL, RMD FLOAT NOT NULL,
                    TON INT NOT NULL, TON_ACUM INT NOT NULL, PROM_PESO FLOAT NOT NULL, MAX_PESO FLOAT NOT NULL, INDE FLOAT NOT NULL, FUER INT NOT NULL, TRAB INT NOT NULL, POT INT NOT NULL          
                )''')
#******************************************************
#**************************SESION EJERCICIO SECUNDARIO********************************
def connect_to_database_sesion_ejercicio_secundario(path):#***************************************************
    con = sqlite3.connect(path)
    cursor = con.cursor()
    create_table_sesion_ejercicio_secundario(cursor)
    con.commit()
    con.close()
def create_table_sesion_ejercicio_secundario(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS SESION_EJERCICIO2(ID INT PRIMARY KEY NOT NULL, FECHA DATE NOT NULL, HORA TIME NOT NULL, FMES TEXT NOT NULL, FSEM TEXT NOT NULL, SESION INT NOT NULL,
                    FSESION TEXT NOT NULL, ANIO INT NOT NULL, SERIE INT NOT NULL, SERIES INT NOT NULL, PEC FLOAT NULL, ESP FLOAT NULL, ABD FLOAT NULL, HOM FLOAT NULL, BIC FLOAT NULL, TRI FLOAT NULL,
                    ANT FLOAT NULL, CUA FLOAT NULL, ISQ FLOAT NULL, ABDU FLOAT NULL, PAN FLOAT NULL, GLU FLOAT NULL
                )''')
#**************************SESION EJERCICIO SECUNDARIO*****************************************
#********FIN*********SESION EJERCICIO******************
#******************************************************
#**********************************************************************
#**********FIN CREA Y CONECTAR  BASE DE DATO***************************
#**********************************************************************
class MessagePopup(Popup):
    pass
#***********************************************************************
#***************************VENTANA PRINCIPAL***************************
#***********************************************************************
class MainWid(ScreenManager):
    def __init__(self,**kwargs):
        super(MainWid,self).__init__()
        self.APP_PATH = os.getcwd()
        self.DB_PATH = self.APP_PATH+'/my_database.db'
        #*****************************************************
        #*****************VENTANA PRINCIPAL******************
        self.StartWid = StartWid(self)
        #*****************************************************
        self.DataBase_SMG = DataBase_SMG(self)
        self.DataBase_SME = DataBase_SME(self)
        self.UpdateData_SMG = MDBoxLayout()
        self.UpdateData_SME = MDBoxLayout()
        self.InsertData_SM = MDBoxLayout()
        #******************************************************
        #******************************************************
        self.DataBase_sesion_ejercicio=DataBase_sesion_ejercicio(self)
        # self.Insert_ejercicio_sesion_muscular= BoxLayout()
        self.Insert_ejercicio_sesion_muscular= Insert_ejercicio_sesion_muscular(self)
        self.UpdateData_sesion_ejercicio_G = MDBoxLayout()
        #******************************************************
        self.Nivel_intensidad=Nivel_intensidad(self)
        self.Nivel_estress=Nivel_estress(self)
        #******************************************************
        self.Popup = MessagePopup()
        #******************************************************
        wid = Screen(name='start')# AGREGA WIDGET (CLASS--StartWid)
        wid.add_widget(self.StartWid)
        self.add_widget(wid)
        #******************************************************
        wid = Screen(name='insertdata_sm')
        wid.add_widget(self.InsertData_SM)
        self.add_widget(wid)
        #*******************************************************
        wid = Screen(name='database_smg')
        wid.add_widget(self.DataBase_SMG)
        self.add_widget(wid)

        wid = Screen(name='database_sme')
        wid.add_widget(self.DataBase_SME)
        self.add_widget(wid)

        wid = Screen(name='updatedata_smg')
        wid.add_widget(self.UpdateData_SMG)
        self.add_widget(wid)

        wid = Screen(name='updatedata_sme')
        wid.add_widget(self.UpdateData_SME)
        self.add_widget(wid)
        
        #******************************************************
        wid = Screen(name='insertdata_sesion_ejercicio')
        wid.add_widget(self.Insert_ejercicio_sesion_muscular)
        self.add_widget(wid)

        wid = Screen(name='database_sesion_ejercicio')
        wid.add_widget(self.DataBase_sesion_ejercicio)
        self.add_widget(wid)

        wid = Screen(name='UpdateData_sesion_ejercicio_g')
        wid.add_widget(self.UpdateData_sesion_ejercicio_G)
        self.add_widget(wid)
        #******************************************************
        wid = Screen(name='nivel_intensidad')#
        wid.add_widget(self.Nivel_intensidad)
        self.add_widget(wid)
        
        wid = Screen(name='nivel_estress')#
        wid.add_widget(self.Nivel_estress)
        self.add_widget(wid)
        
        
    def goto_start(self):
        self.current = 'start'

    #******************************************************
    #*****INICIO******SESION MUSCULAR****INICIO************
    #******************************************************    
    #*****************VISIALIZAR DATABASE*****************
    def goto_database_SMG(self):
        self.DataBase_SMG.check_memory_SMG()
        self.current = 'database_smg'

    def goto_database_SME(self):
        self.DataBase_SME.check_memory_SME()
        self.current = 'database_sme'

    def goto_insertdata_SM(self):
        self.InsertData_SM.clear_widgets()
        wid = InsertData_SM(self)
        self.InsertData_SM.add_widget(wid)
        self.current = 'insertdata_sm'

    def goto_updatedata_SMG(self,data_id):
        self.UpdateData_SMG.clear_widgets()
        wid = UpdateData_SMG(self,data_id)
        self.UpdateData_SMG.add_widget(wid)
        self.current = 'updatedata_smg'

    def goto_updatedata_SME(self,data_id):
        self.UpdateData_SME.clear_widgets()
        wid = UpdateData_SME(self,data_id)
        self.UpdateData_SME.add_widget(wid)
        self.current = 'updatedata_sme'
    #******************************************************
    #******************************************************
    def goto_Insert_ejercicio_sesion_muscular(self):
        self.Insert_ejercicio_sesion_muscular.clear_widgets()
        wid = Insert_ejercicio_sesion_muscular(self)
        self.Insert_ejercicio_sesion_muscular.add_widget(wid)
        self.current = 'insertdata_sesion_ejercicio'

    def goto_database_sesion_ejercicio(self):
        self.DataBase_sesion_ejercicio.check_memory_sesion_ejercicio()
        self.current = 'database_sesion_ejercicio'

    def goto_UpdateData_sesion_ejercicio_G(self,data_id):
        self.UpdateData_sesion_ejercicio_G.clear_widgets()
        wid = UpdateData_sesion_ejercicio_G(self,data_id)
        self.UpdateData_sesion_ejercicio_G.add_widget(wid)
        self.current = 'UpdateData_sesion_ejercicio_g'

    #******************************************************
    def goto_Nivel_intensidad(self):
        self.current = 'nivel_intensidad'
        
    def goto_Nivel_estress(self):
        self.current = 'nivel_estress'
    #******************************************************
        
#**************************************************************************
#************************FIN***VENTANA PRINCIPAL***************************
#**************************************************************************

#**************************************************************************
#*******************PRIMERA VENTANA****MENU PRINCIPAL**********************
#**************************************************************************
class StartWid(MDBoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(StartWid,self).__init__()
        self.mainwid = mainwid

    def create_database_sesion_muscular(self):
        connect_to_database_pecho(self.mainwid.DB_PATH)
        connect_to_database_espalda(self.mainwid.DB_PATH)
        connect_to_database_abdomen(self.mainwid.DB_PATH)
        connect_to_database_hombro(self.mainwid.DB_PATH)
        connect_to_database_bicep(self.mainwid.DB_PATH)
        connect_to_database_tricep(self.mainwid.DB_PATH)
        connect_to_database_antebrazo(self.mainwid.DB_PATH)
        connect_to_database_cuadricep(self.mainwid.DB_PATH)
        connect_to_database_isquios(self.mainwid.DB_PATH)
        connect_to_database_abductores(self.mainwid.DB_PATH)
        connect_to_database_pantorrilla(self.mainwid.DB_PATH)
        connect_to_database_gluteo(self.mainwid.DB_PATH)
        connect_to_database_seleccione_musculo(self.mainwid.DB_PATH)
        connect_to_database_seleccione_ejercicio(self.mainwid.DB_PATH)
        self.mainwid.goto_insertdata_SM() 

    def create_database_sesion_ejercicio(self):
        connect_to_database_sesion_ejercicio(self.mainwid.DB_PATH)
        connect_to_database_sesion_ejercicio_secundario(self.mainwid.DB_PATH)
        self.mainwid.goto_Insert_ejercicio_sesion_muscular()
        
    def nivel_intensidad(self):
        self.mainwid.goto_Nivel_intensidad()
        
    def nivel_estress(self):
        self.mainwid.goto_Nivel_estress()
        
#**************************************************************************
#*******************PRIMERA VENTANA****MENU PRINCIPAL**********************
#**************************************************************************
        
#**************************************************************************
#*******************SEGUNDA VENTANA****DATABASE SESION MUSCULAR************
#**************************************************************************
#************************DATABASE GENERAL********************************************
class DataBase_SMG(MDBoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(DataBase_SMG,self).__init__()
        self.mainwid = mainwid  
        
    def select_sesion_m2(self):
        global sm2
        sm2 = self.ids.sm2.text
        return sm2
    
    def check_memory_SMG(self):
        self.ids.agregar_smg.clear_widgets()#LIMPIAR  WIDGET ScrollView
        self.ids.inicio_smg.clear_widgets()#LIMPIAR WIDGET BoxLayout
        wid = Button_atras_SMG(self.mainwid)#BOTON INICIO
        self.ids.inicio_smg.add_widget(wid)#BOTON INICIO
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor = con.cursor()
        s_muscular=self.select_sesion_m2()
        s1 = f'select ID, EJERCICIO from "{s_muscular}"'
        cursor.execute(s1)
        resultado=cursor.fetchall()
        for i in resultado:
            wid = DataWid_SMG(self.mainwid)
            wid.data_id = str(i[0])
            wid.data = str(i[1])
            self.ids.agregar_smg.add_widget(wid)
        wid = Button_inicio_SMG(self.mainwid)#BOTON AGREGAR
        self.ids.inicio_smg.add_widget(wid)#BOTON AGREGAR
        wid = Button_ver_SMG(self.mainwid)#BOTON VER
        self.ids.inicio_smg.add_widget(wid)#BOTON VER
        
        con.close()
        
class DataWid_SMG(MDBoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(DataWid_SMG,self).__init__()
        self.mainwid = mainwid
    def update_data_SMG(self,data_id):
        self.mainwid.goto_updatedata_SMG(data_id)#MODIFIQUE
        
class Button_ver_SMG(MDRaisedButton):#CREAR BOTON AGREGAR
    def __init__(self,mainwid,**kwargs):
        super(Button_ver_SMG,self).__init__()
        self.mainwid = mainwid
    def visualizar_SMG(self):
        self.mainwid.goto_database_SMG() 

class Button_atras_SMG(MDRaisedButton):#CREAR BOTON AGREGAR
    def __init__(self,mainwid,**kwargs):
        super(Button_atras_SMG,self).__init__()
        self.mainwid = mainwid
    def atras_insertdata_SM(self):
        self.mainwid.goto_insertdata_SM() 

class Button_inicio_SMG(MDRaisedButton):#CREAR BOTON INICIO
    def __init__(self,mainwid,**kwargs):
        super(Button_inicio_SMG,self).__init__()
        self.mainwid = mainwid
    def back_to_StartWid(self):
        self.mainwid.goto_start()
#************************DATABASE GENERAL************************************
#************************DATABASE ESPECIFICO********************************************
class DataBase_SME(MDBoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(DataBase_SME,self).__init__()
        self.mainwid = mainwid  
        
    def check_memory_SME(self):
        self.ids.agregar_sme.clear_widgets()#LIMPIAR  WIDGET ScrollView
        self.ids.inicio_sme.clear_widgets()#LIMPIAR WIDGET BoxLayout
        wid = Button_atras_SME(self.mainwid)#BOTON INICIO
        self.ids.inicio_sme.add_widget(wid)#BOTON INICIO
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor = con.cursor()
        s_muscular=sm1
        s1 = f'select ID, EJERCICIO from "{s_muscular}"'
        cursor.execute(s1)
        resultado=cursor.fetchall()
        for i in resultado:
            wid = DataWid_SME(self.mainwid)
            wid.data_id = str(i[0])
            wid.data = str(i[1])
            self.ids.agregar_sme.add_widget(wid)
        wid = Button_inicio_SME(self.mainwid)#BOTON AGREGAR
        self.ids.inicio_sme.add_widget(wid)#BOTON AGREGAR
        wid = Button_ver_SME(self.mainwid)#BOTON VER
        self.ids.inicio_sme.add_widget(wid)#BOTON VER
        con.close()
        
class DataWid_SME(MDBoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(DataWid_SME,self).__init__()
        self.mainwid = mainwid
    def update_data_SME(self,data_id):
        self.mainwid.goto_updatedata_SME(data_id)#MODIFIQUE

class Button_ver_SME(MDRaisedButton):#CREAR BOTON AGREGAR
    def __init__(self,mainwid,**kwargs):
        super(Button_ver_SME,self).__init__()
        self.mainwid = mainwid
    def visualizar_SME(self):
        self.mainwid.goto_database_SME() 
        
class Button_atras_SME(MDRaisedButton):#CREAR BOTON AGREGAR
    def __init__(self,mainwid,**kwargs):
        super(Button_atras_SME,self).__init__()
        self.mainwid = mainwid
    def atras_insertdata_SM(self):
        self.mainwid.goto_insertdata_SM() 

class Button_inicio_SME(MDRaisedButton):#CREAR BOTON INICIO
    def __init__(self,mainwid,**kwargs):
        super(Button_inicio_SME,self).__init__()
        self.mainwid = mainwid
    def back_to_StartWid(self):
        self.mainwid.goto_start()
#************************DATABASE ESPECIFICO************************************

#**************************************************************************
#*************FIN***SEGUNDA VENTANA****DATABASE SESION MUSCULAR************
#**************************************************************************

#**************************************************************************
#*******************TERCERA VENTANA****INSERTAR SESION MUSCULAR************
#**************************************************************************
class InsertData_SM(MDBoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(InsertData_SM,self).__init__()
        self.mainwid = mainwid
    
    #*************************AGREGAR DATOS***********************
    def calcular_RM(self):
        peso1=self.ids.ti_peso1.text
        nrep1=self.ids.ti_no_rep.text
        peso=float(peso1)
        nrep=float(nrep1)
        rm1 = round(peso/(1.0278-(0.0278*nrep)),2) 
        rm=str(rm1)
        self.ids.ti_1rm.text=rm
    #************AGREGAR EJERCICIOS*******************************************
    def select_abrv(self):
        d1 = self.ids.ti_abrv.text
        return d1 
    def select_articular(self):
        d2 = self.ids.ti_articulacion.text
        return d2
    def select_modo(self):
        d3 = self.ids.ti_modo.text
        return d3
    def select_ejercicio(self):
        d4 = self.ids.ti_ejercicio.text
        return d4 
    def select_1rm(self):
        d5 = self.ids.ti_1rm.text
        return d5 
    def select_sesion_m(self):
        global sm1
        sm1 = self.ids.sm1.text
        return sm1 

    def insert_data_SM(self):
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor = con.cursor()
        cursor_consulta = con.cursor()
        s_muscular=self.select_sesion_m()
        s1 = f'select ID from "{s_muscular}" ORDER BY ID ASC'
        cursor_consulta.execute(s1)
        resultado1=cursor_consulta.fetchall()#resultado = lista original base de dato
        cant_reg=len(resultado1)
        #*************SECUENCIA ID**************
        if cant_reg>=1:
            sec=cant_reg
            while sec<=cant_reg:
                sec += 1
            sec=sec
        else:
            sec=1
        sec1=sec
        #***********SECUENCIA ID*****************
        #***************CONDICIONAL DATOS VACIOS******
        dt1 = self.ids.ti_pec.text
        dt2 = self.ids.ti_esp.text
        dt3 = self.ids.ti_abd.text
        dt4 = self.ids.ti_hom.text
        dt5 = self.ids.ti_bic.text
        dt6 = self.ids.ti_tri.text
        dt7 = self.ids.ti_ant.text
        dt8 = self.ids.ti_cua.text
        dt9 = self.ids.ti_isq.text
        dt10 = self.ids.ti_abdu.text
        dt11 = self.ids.ti_pan.text
        dt12 = self.ids.ti_glu.text
        if dt1!="":
            a=dt1
        else:
            a=0
        b1=a
        if dt2!="":
            a=dt2
        else:
            a=0
        b2=a
        if dt3!="":
            a=dt3
        else:
            a=0
        b3=a
        if dt4!="":
            a=dt4
        else:
            a=0
        b4=a
        if dt5!="":
            a=dt5
        else:
            a=0
        b5=a
        if dt6!="":
            a=dt6
        else:
            a=0
        b6=a
        if dt7!="":
            a=dt7
        else:
            a=0
        b7=a
        if dt8!="":
            a=dt8
        else:
            a=0
        b8=a
        if dt9!="":
            a=dt9
        else:
            a=0
        b9=a
        if dt10!="":
            a=dt10
        else:
            a=0
        b10=a
        if dt11!="":
            a=dt11
        else:
            a=0
        b11=a
        if dt12!="":
            a=dt12
        else:
            a=0
        b12=a
        #***********************************************
        d1 = sec1
        d2 = self.select_articular()
        d3 = self.select_modo()
        d4 = self.select_abrv()
        d5 = self.select_ejercicio()
        d6 = self.select_1rm()
        d7 = b1
        d8 = b2
        d9 = b3
        d10 = b4
        d11 = b5
        d12 = b6
        d13 = b7
        d14 = b8
        d15 = b9
        d16 = b10
        d17 = b11
        d18 = b12
        a1=(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18)
        s1 = f'INSERT INTO "{s_muscular}"(ID, ARTICULAR, MODO, ABRV, EJERCICIO, RM, PEC, ESP, ABD, HOM, BIC, TRI, ANT, CUA, ISQ, ABDU, PAN, GLU)'
        s2 = 'VALUES(%s, "%s", "%s", "%s", "%s", %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)' % a1
        #*******************************************************************
        if d2=="ARTICULACION" or d3=="MODO" or d4=="" or d5==""  or d6=="":
            message = self.mainwid.Popup.ids.message
            self.mainwid.Popup.open()
            self.mainwid.Popup.title = "Data base error"
            message.text = 'Uno o más campos están vacíos'
        else:
            con = sqlite3.connect(self.mainwid.DB_PATH)  #mode: "rectangle"
            cursor = con.cursor()
            cursor.execute(s1+' '+s2)
            con.commit()
            con.close()
            self.mainwid.goto_database_SME()

    def ir_to_dbw_SMG(self):
        self.mainwid.goto_database_SMG()
    
    def ir_to_dbw_SME(self):
        self.mainwid.goto_database_SME()
    #************PECHO*******************************************
    def back_to_StartWid(self):
        self.mainwid.goto_start()
    
#**************************************************************************
#************FIN****TERCERA VENTANA****INSERTAR SESION MUSCULAR************
#**************************************************************************
#s_muscular=="SELECCIONE_SESION_MUSCULAR" 
#**************************************************************************
#**********CUARTA VENTANA****MODIFICAR Y ELIMINAR SESION MUSCULAR**********
#**************************************************************************
#********************UPDATEDATA GENERAL******************************************
class UpdateData_SMG(MDBoxLayout):
    def __init__(self,mainwid,data_id,**kwargs):
        super(UpdateData_SMG,self).__init__()
        self.mainwid = mainwid
        self.data_id = data_id
        self.check_memory_update_SMG()

    def check_memory_update_SMG(self):
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor = con.cursor()
        s_muscular3=sm2
        s=f"select ARTICULAR, MODO, ABRV, EJERCICIO, RM, PEC, ESP, ABD, HOM, BIC, TRI, ANT, CUA, ISQ, ABDU, PAN, GLU from '{s_muscular3}' WHERE ID =" 
        cursor.execute(s+self.data_id)
        for i in cursor:
            self.ids.ti_articulacion.text = i[0]
            self.ids.ti_modo.text = i[1]
            self.ids.ti_abrv.text = i[2]
            self.ids.ti_ejercicio.text = i[3]
            self.ids.ti_1rm.text = str(i[4])
            self.ids.ti_pec.text = str(i[5])
            self.ids.ti_esp.text = str(i[6])
            self.ids.ti_abd.text = str(i[7])
            self.ids.ti_hom.text = str(i[8])
            self.ids.ti_bic.text = str(i[9])
            self.ids.ti_tri.text = str(i[10])
            self.ids.ti_ant.text = str(i[11])
            self.ids.ti_cua.text = str(i[12])
            self.ids.ti_isq.text = str(i[13])
            self.ids.ti_abdu.text = str(i[14])
            self.ids.ti_pan.text = str(i[15])
            self.ids.ti_glu.text = str(i[16])
        con.close()

    def update_data_SMG(self):
        con = sqlite3.connect(self.mainwid.DB_PATH)  #readonly:True
        cursor = con.cursor()
        d1 = self.ids.ti_articulacion.text
        d2 = self.ids.ti_modo.text
        d3 = self.ids.ti_abrv.text
        d4 = self.ids.ti_ejercicio.text
        d5 = self.ids.ti_1rm.text
        d6 = self.ids.ti_pec.text 
        d7 = self.ids.ti_esp.text
        d8 = self.ids.ti_abd.text 
        d9 = self.ids.ti_hom.text 
        d10 = self.ids.ti_bic.text 
        d11 = self.ids.ti_tri.text 
        d12 = self.ids.ti_ant.text 
        d13 = self.ids.ti_cua.text 
        d14 = self.ids.ti_isq.text 
        d15 = self.ids.ti_abdu.text 
        d16 = self.ids.ti_pan.text 
        d17 = self.ids.ti_glu.text 
        a1 = (d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17)
        s_muscular3=sm2
        s1 = f"UPDATE '{s_muscular3}' SET"
        s2 = 'ARTICULAR="%s",MODO="%s", ABRV="%s", EJERCICIO="%s", RM="%s", PEC=%s, ESP=%s, ABD=%s, HOM=%s, BIC=%s, TRI=%s, ANT=%s, CUA=%s, ISQ=%s, ABDU=%s, PAN=%s, GLU=%s' % a1
        s3 = 'WHERE ID=%s' % self.data_id
        try:
            cursor.execute(s1+' '+s2+' '+s3)
            con.commit()
            con.close()
            self.mainwid.goto_database_SMG()
        except Exception as e:
            message = self.mainwid.Popup.ids.message
            self.mainwid.Popup.open()
            self.mainwid.Popup.title = "Data base error"
            if '' in a1:
                message.text = 'Uno o más campos están vacíos'
            else: 
                message.text = str(e)
            con.close()

    def delete_data_SMG(self):
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor = con.cursor()
        s_muscular3=sm2
        s = f"delete from '{s_muscular3}' where ID="+self.data_id
        cursor.execute(s)
        con.commit()
        con.close()
        self.mainwid.goto_database_SMG()    
    
    def back_to_StartWid(self):
        self.mainwid.goto_start()
    
    def back_to_dbw_SMG(self):
        self.mainwid.goto_database_SMG()    
#********************UPDATEDATA GENERAL*****************************************
#********************UPDATEDATA ESPECIFICO******************************************
class UpdateData_SME(MDBoxLayout):
    def __init__(self,mainwid,data_id,**kwargs):
        super(UpdateData_SME,self).__init__()
        self.mainwid = mainwid
        self.data_id = data_id
        self.check_memory_update_SME()

    def check_memory_update_SME(self):
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor = con.cursor()
        s_muscular3=sm1
        s=f"select ARTICULAR, MODO, ABRV, EJERCICIO, RM, PEC, ESP, ABD, HOM, BIC, TRI, ANT, CUA, ISQ, ABDU, PAN, GLU from '{s_muscular3}' WHERE ID =" 
        cursor.execute(s+self.data_id)
        for i in cursor:
            self.ids.ti_articulacion.text = i[0]
            self.ids.ti_modo.text = i[1]
            self.ids.ti_abrv.text = i[2]
            self.ids.ti_ejercicio.text = i[3]
            self.ids.ti_1rm.text = str(i[4])
            self.ids.ti_pec.text = str(i[5])
            self.ids.ti_esp.text = str(i[6])
            self.ids.ti_abd.text = str(i[7])
            self.ids.ti_hom.text = str(i[8])
            self.ids.ti_bic.text = str(i[9])
            self.ids.ti_tri.text = str(i[10])
            self.ids.ti_ant.text = str(i[11])
            self.ids.ti_cua.text = str(i[12])
            self.ids.ti_isq.text = str(i[13])
            self.ids.ti_abdu.text = str(i[14])
            self.ids.ti_pan.text = str(i[15])
            self.ids.ti_glu.text = str(i[16])
        con.close()

    def update_data_SME(self):
        con = sqlite3.connect(self.mainwid.DB_PATH)  #readonly:True
        cursor = con.cursor()
        d1 = self.ids.ti_articulacion.text
        d2 = self.ids.ti_modo.text
        d3 = self.ids.ti_abrv.text
        d4 = self.ids.ti_ejercicio.text
        d5 = self.ids.ti_1rm.text
        d6 = self.ids.ti_pec.text 
        d7 = self.ids.ti_esp.text
        d8 = self.ids.ti_abd.text 
        d9 = self.ids.ti_hom.text 
        d10 = self.ids.ti_bic.text 
        d11 = self.ids.ti_tri.text 
        d12 = self.ids.ti_ant.text 
        d13 = self.ids.ti_cua.text 
        d14 = self.ids.ti_isq.text 
        d15 = self.ids.ti_abdu.text 
        d16 = self.ids.ti_pan.text 
        d17 = self.ids.ti_glu.text  
        a1 = (d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17)
        s_muscular3=sm1
        s1 = f"UPDATE '{s_muscular3}' SET"
        s2 = 'ARTICULAR="%s",MODO="%s", ABRV="%s", EJERCICIO="%s", RM=%s, PEC=%s, ESP=%s, ABD=%s, HOM=%s, BIC=%s, TRI=%s, ANT=%s, CUA=%s, ISQ=%s, ABDU=%s, PAN=%s, GLU=%s' % a1
        s3 = 'WHERE ID=%s' % self.data_id
        try:
            cursor.execute(s1+' '+s2+' '+s3)
            con.commit()
            con.close()
            self.mainwid.goto_database_SME()
        except Exception as e:
            message = self.mainwid.Popup.ids.message
            self.mainwid.Popup.open()
            self.mainwid.Popup.title = "Data base error"
            if '' in a1:
                message.text = 'Uno o más campos están vacíos'
            else: 
                message.text = str(e)
            con.close()

    def delete_data_SME(self):
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor = con.cursor()
        s_muscular3=sm1
        s = f"delete from '{s_muscular3}' where ID="+self.data_id
        cursor.execute(s)
        con.commit()
        con.close()
        self.mainwid.goto_database_SME()    
    
    def back_to_StartWid(self):
        self.mainwid.goto_start()
    
    def back_to_dbw_SME(self):
        self.mainwid.goto_database_SME()    
#********************UPDATEDATA ESPECIFICO*****************************************

#**************************************************************************
#***FIN****CUARTA VENTANA****MODIFICAR Y ELIMINAR SESION MUSCULAR**********
#**************************************************************************

# #******************************************************************************
# #*********QUINTA VENTANA**INGRESAR SESION EJERCICIO****************************
# #******************************************************************************    

class Insert_ejercicio_sesion_muscular(MDBoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(Insert_ejercicio_sesion_muscular,self).__init__()
        self.mainwid = mainwid
        self.agregar_spinner()
        self.on_start()
        #time.sleep(1)
        self.datos_historico()
    #INICIO****************************************AGREGAR LISTA DE EJERCICIOS Y SESION MUSCULAR*****************************
    
    def agregar_spinner(self):
        # try:
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor_consulta = con.cursor()
        dato=(self.ids.sesion_muscular1.text)
        s2=f"select EJERCICIO from '{dato}'"
        cursor_consulta.execute(s2)
        resultado1=cursor_consulta.fetchall()#resultado = lista original base de dato
        resul=[]
        for i in resultado1:
            y= i[-1]
            resul.append(y)
        lista1=resul
        #CREAR SPINNER EJERCICIO Y AGREGAR A VENTANA
        self.ids.spiner_ejercicio_sesion.clear_widgets()#LIMPIAR  WIDGET ScrollView
        wid=self.SpinnerObject=Spinner(text='SELECCIONE_EJERCICIOS', values=lista1,sync_height= True)
        self.SpinnerObject.bind(text=self.on_spinner_select_sesion_ejercicio)
        self.ids.spiner_ejercicio_sesion.add_widget(wid)#AGREGAR BOTON A LA VENTANA 
            #CREAR SPINNER EJERCICIO Y AGREGAR A VENTANA
        # except Exception as e:
        #     print(type(e).__name__,"-" "  No hay registro en la tabla spiner")
        
    def on_spinner_select_sesion_ejercicio(self,spinner,dato2): 
        global sesion_ejercicio
        sesion_ejercicio=dato2
    #INICIO****************************************AGREGAR LISTA DE EJERCICIOS Y SESION MUSCULAR*****************************
    #*************************PESO**************************
    cont_peso =1# tomardato()
    peso = StringProperty('1')
    def aumentar_boton_peso(self):
        self.cont_peso=int(self.ids.ti_peso1.text )   
        self.cont_peso = self.cont_peso + 1
        self.peso= str(self.cont_peso)
    def disminuir_boton_peso(self):
        self.cont_peso = self.cont_peso - 1
        valor=self.cont_peso
        if valor>=0:
            self.peso= str(self.cont_peso)
    #*************************PESO**************************   
    #************TIEMPO DE TENSION**************************
    cont_tt =1# tomardato()
    tt = StringProperty('1')
    def aumentar_boton_tt(self):
        self.cont_tt=int(self.ids.ti_ttrep.text )   
        self.cont_tt = self.cont_tt + 1
        valor=self.cont_tt
        if valor<=10:
            self.tt= str(self.cont_tt)
    def disminuir_boton_tt(self):
        self.cont_tt = self.cont_tt - 1
        valor=self.cont_tt
        if valor>=0:
            self.tt= str(self.cont_tt)
    #************TIEMPO DE TENSION**************************  
    #************NO REPETICION**************************
    cont_nrep =1# tomardato()
    nrep = StringProperty('1')
    def aumentar_boton_nrep(self):
        self.cont_nrep=int(self.ids.ti_repeticion.text )   
        self.cont_nrep = self.cont_nrep + 1
        self.nrep= str(self.cont_nrep)
    def disminuir_boton_nrep(self):
        self.cont_nrep = self.cont_nrep - 1
        valor=self.cont_nrep
        if valor>=0:    
            self.nrep= str(self.cont_nrep)
    #************NO REPETICION**************************  
    #***********RIR-REPETICION EN RESERVA*********************************
    cont_rir =1# tomardato()
    rir = StringProperty('-1')
    rpe = StringProperty('10')
    def aumentar_boton_rir(self):
        self.cont_rir=int(self.ids.ti_rir.text )   
        self.cont_rir = self.cont_rir + 1
        valor=self.cont_rir
        if valor<=4:
            self.rir= str(self.cont_rir)
        #*****************************************
        self.cont_rpe=int(self.ids.ti_rpe.text )   
        self.cont_rpe = self.cont_rpe - 1
        valor=self.cont_rpe
        if valor<=10 and valor>=5:
            self.rpe= str(self.cont_rpe)
    def disminuir_boton_rir(self):
        self.cont_rir = self.cont_rir - 1
        valor=self.cont_rir
        if valor>=-1:
            self.rir= str(self.cont_rir)
        #*****************************************
        self.cont_rpe = self.cont_rpe + 1
        valor=self.cont_rpe
        if valor>=5 and valor<=10:
            self.rpe= str(self.cont_rpe)
    #***********RIR-REPETICION EN RESERVA********************************* 

    #*********CRONOMETRO*****************************************************
    sw_seconds = 0
    sw_started = False
    def on_start(self):
        Clock.schedule_interval(self.update, 0)

    def update(self, nap):
        try:
            td=int(self.ids.ti_descanso.text)   
            td1=td*60
            if self.sw_started:
                if self.sw_seconds<=td1:
                    self.sw_seconds += nap
            m, s = divmod(self.sw_seconds, 60)
            # a=self.ids.stopwatch.text = ('DESCANSO: '+'%02d:%02d:%02d' % (int(m), int(s), int(s * 100 % 100)))
            a=self.ids.stopwatch.text = ('%02d:%02d:%02d' % (int(m), int(s), int(s * 100 % 100)))
            if a==f"0{td}:00:00":
                self.sound=SoundLoader.load("sound3.wav")
                self.sound.play()
        except Exception as e:
            print(type(e).__name__,"-" "  No hay registro en la celda descanso")
            
    def start_stop(self):
        self.ids.start_stop.text = 'Start' if self.sw_started else 'Stop'
        self.sw_started = not self.sw_started
        
    def reset(self):
        if self.sw_started:
            self.ids.start_stop.text = 'Start'
            self.sw_started = False
            self.sw_seconds = 0
    # def start_stop(self):
    #     self.sw_started = not self.sw_started
    #     if self.sw_started == True:
    #         self.ids.start_stop.text = 'Start'
    #     else:   
    #         self.sw_started = False
    #         self.sw_seconds = 0
    
    #*********CRONOMETRO******************************************************
    #******************CARGAR DATOS HISTORICOS********************************
    def datos_historico(self):
        try:
            con = sqlite3.connect(self.mainwid.DB_PATH)
            sql1=f"select MAX_PESO, REP, SESION, RM_PORC from SESION_EJERCICIO WHERE EJERCICIO ='{sesion_ejercicio}'" 
            df1= pd.read_sql_query(sql1,con)   #.fillna("0",inplace=True) se aplica cuando hay valores null en columnas o
            inde=df1["MAX_PESO"].max()
            cond=df1["MAX_PESO"]==inde
            cond1=df1[cond]
            #****************************
            inde2=df1["SESION"].max()
            cond2=df1["SESION"]==inde2
            cond3=df1[cond2]
            #*****************************
            ult_serie=cond3["SESION"].count()
            peso_max=cond1["MAX_PESO"].max()
            rep_max=cond1["REP"].max()
            rm_actual=cond1["RM_PORC"].max()
            #******************************************
            self.ids.max_peso.text=str(peso_max)
            self.ids.no_rep.text=str(rep_max)
            self.ids.rmp.text=str(rm_actual)
            self.ids.no_serie.text=str(ult_serie)
        except Exception as e:
            print(type(e).__name__,"-" "  No hay registro en la tabla spiner")
        
        
    #******************CARGAR DATOS HISTORICOS********************************
    
    def insertdata_sesion_muscular(self):
        try:
            con = sqlite3.connect(self.mainwid.DB_PATH)
            cursor_consulta = con.cursor()
            cursor_consulta.execute('select ID from SESION_EJERCICIO ORDER BY ID ASC')
            resultado1=cursor_consulta.fetchall()#resultado = lista original base de dato sesion_ejercicio
            cant_reg=len(resultado1)
            global sesion_muscular2
            sesion_muscular2=self.ids.sesion_muscular1.text
            #********************************************************************************
            con = sqlite3.connect(self.mainwid.DB_PATH)
            cursor_consul = con.cursor()
            se1 = f"select SERIES, EJERCICIO from SESION_EJERCICIO WHERE EJERCICIO ='{sesion_ejercicio}'" 
            cursor_consul.execute(se1)
            sec_ejer1=cursor_consul.fetchall()#resultado = lista original base de dato
            cant_ejer=len(sec_ejer1)
            
            #*********************************************************************************
            #*******************CONSULTAR FECHA Y SESION****************************************************
            nrep3=int(self.ids.ti_repeticion.text)
            peso3=float(self.ids.ti_peso1.text)# peso actual
            tdes1 =float(self.ids.ti_descanso.text)
            ttrep1=float(self.ids.ti_ttrep.text)
            if cant_reg>=1:#*********cant_reg>=1************CONDICIONAL SI ES MAYOR A UN REGISTRO*****
                cursor_consulta2 = con.cursor()
                cursor_consulta2.execute('select FECHA, SESION, SERIE, EJERCICIO, PESOT, VOLUMEN, PESO, TTSTS, TDES from SESION_EJERCICIO ORDER BY ID DESC')
                fecha_ant1=cursor_consulta2.fetchall()#resultado = lista original base de dato
                cursor_consulta2.close()
                tdes2=float(fecha_ant1[0][8])
                ttsts2=float(fecha_ant1[0][7])
                peso_ant=float(fecha_ant1[0][6])
                vol2=int(fecha_ant1[0][5])
                pesot2=float(fecha_ant1[0][4])
                ejercicio=fecha_ant1[0][3]
                serie=int(fecha_ant1[0][2])
                sesion=fecha_ant1[0][1]
                fecha_ants=fecha_ant1[0][0]
                fechains=date.today().strftime(format_fecha)
                fecha_ant=datetime.strptime(fecha_ants, format_fecha)
                fechain1=datetime.strptime(fechains, format_fecha)
                
                #***********************TT ************************
                ttrep=(ttrep1*nrep3)/60
                #******************************************
                #*******SECUENCIA SERIE_DIA, VOLUMEN, PESO_TOTAL, TONELAJE_ACUM, PROMEDIO_PESO, MAXIMO_PESO, - TTSTS - TDES- TDUS- DSERIE- DSESION*********
                if fecha_ant<fechain1:
                    secf_1 = sesion + 1
                    tdes_1 = tdes1
                    ttsts_1 = ttrep
                    maxp_1 = peso3
                    promp_1 = peso3
                    ton_acum_1 = nrep3*peso3
                    pesot_1 = peso3
                    vol_1 = nrep3
                    sece_1 = 1 
                elif fecha_ant==fechain1:
                    #********CONDICIONAL SESION EJERCICIO*************
                    if ejercicio==sesion_ejercicio:
                        secf_1 = sesion 
                        tdes_1 = tdes2 + tdes1
                        ttsts_1 = ttsts2 + ttrep
                        sece_1 = serie+1 
                        vol_1= vol2 + nrep3
                        pesot_1 = pesot2+peso3
                        ton_acum_1 = pesot_1 * vol_1
                        promp_1 = pesot_1 / sece_1
                        if peso_ant>=peso3:
                            maxp_2 = peso_ant
                        else:
                            maxp_2 = peso3
                        maxp_1 = maxp_2
                    else:
                        secf_1 = sesion 
                        tdes_1 = tdes1
                        ttsts_1 = ttrep
                        sece_1 = 1
                        vol_1 = nrep3
                        pesot_1 = peso3
                        ton_acum_1 = nrep3*peso3
                        promp_1 = peso3
                        maxp_1 = peso3
                secf = secf_1
                tdes = tdes_1
                ttsts = ttsts_1
                sece = sece_1
                vol = vol_1
                pesot = pesot_1
                ton_acum = ton_acum_1
                promp = promp_1
                maxp = maxp_1
            #     #********CONDICIONAL SESION EJERCICIO*************
            #     #*******SECUENCIA SERIE_DIA, VOLUMEN, PESO_TOTAL, TONELAJE_ACUM, PROMEDIO_PESO, MAXIMO_PESO*********
            else: #*********cant_reg>=1************CONDICIONAL SI ES MAYOR A UN REGISTRO*****
                tdes = tdes1
                ttsts = (ttrep1*nrep3)/60
                sece=1
                secf=1
                vol=nrep3
                pesot=peso3
                ton_acum=nrep3*peso3
                promp=peso3
                maxp=peso3
            #*******************CONSULTAR FECHA Y SESION*********************************************
            # duracion total de la sesion
            tdus = tdes + ttsts
            # densidad serie
            ttrep=(ttrep1*nrep3)/60
            dserie = (ttrep / tdes1) * 100
            # densidad sesion
            dsesion = (ttsts / tdus) * 100
            #*************SECUENCIA ID**************
            if cant_reg>=1:
                sec=cant_reg
                while sec<=cant_reg:
                    sec += 1
                sec=sec
            else:
                sec=1
            sec1=sec
            #***********SECUENCIA ID*****************
            #*************SECUENCIA EJERCICIO**************
            if cant_ejer>=1:
                ejercicio1=sec_ejer1[0][1]
                if ejercicio1==sesion_ejercicio:
                    secea1=cant_ejer
                    while secea1<=cant_ejer:
                        secea1 += 1
                    secea1=secea1
                secea1=secea1
            else:
                secea1=1
            secea=secea1
            #***********SECUENCIA EJERCICIO*****************
            #***********CALCULAR 1RM*************
            global rm
            con = sqlite3.connect(self.mainwid.DB_PATH)
            cursor_consulta3 = con.cursor()
            s_m=sesion_muscular2
            sr = f"select EJERCICIO, RM, ARTICULAR, ABRV from '{s_m}' WHERE EJERCICIO ='{sesion_ejercicio}'" 
            cursor_consulta3.execute(sr)
            rm1=cursor_consulta3.fetchall()#resultado = lista original base de dato
            cursor_consulta3.close()
            abrv1=rm1[0][3]#1RM INICIAL
            articular=rm1[0][2]#1RM INICIAL
            rm=float(rm1[0][1])#1RM INICIAL
            peso2=float(self.ids.ti_peso1.text)# peso actual
            nrep2=float(self.ids.ti_repeticion.text)
            rm_porc=float((peso2/rm)*100)
            rmd=peso2/(1.0278-(0.0278*nrep2))
            #***********CALCULAR 1RM*************
            #***********CONDICIONAL ACTUALIZAR 1RM*************
            if peso2>=rm:
                cursor_consulta4 = con.cursor()
                rm_actual=str(round(peso2/(1.0278-(0.0278*nrep2)),2)) 
                su = f"UPDATE '{s_m}' SET RM='{rm_actual}' WHERE EJERCICIO='{sesion_ejercicio}'"
                cursor_consulta4.execute(su)
                con.commit()
                cursor_consulta4.close()
            #***********CONDICIONAL ACTUALIZAR 1RM*************
            #********REPETICIONES EFECTIVAS******
            refect1=int(self.ids.ti_rir.text)
            if rm_porc>=70 :
                if nrep3>=6:
                    if refect1==-1:
                        repe=6
                    elif refect1==0:
                        repe=5
                    elif refect1==1:
                        repe=4
                    elif refect1==2:
                        repe=3
                    elif refect1==3:
                        repe=2
                    elif refect1==4:
                        repe=1
                    repe1=repe
                else:
                    repe1=nrep3
            else:
                repe1=0
            refect=repe1
            #********REPETICIONES EFECTIVAS******
            #***********************TONELAJE************************
            ton=nrep3*peso3
            #*************************NIVEL DE ESTRESS*************
            rir=int(self.ids.ti_rir.text)
            rirf=1.8
            rir0=1.6
            rir1=1.2
            rir2=1
            rir3=0.8
            rir4=0.6
            multi=1.25
            mono=1
            if articular=="MULTI":
                if rir==-1:
                    ind_estress1=rirf*multi 
                if rir==0:
                    ind_estress1=rir0*multi 
                if rir==1:
                    ind_estress1=rir1*multi 
                if rir==2:
                    ind_estress1=rir2*multi
                if rir==3:
                    ind_estress1=rir3*multi
                if rir==4:
                    ind_estress1=rir4*multi   
                ind_estress2=ind_estress1
            if articular=="MONO":
                if rir==-1:
                    ind_estress1=rirf*mono 
                if rir==0:
                    ind_estress1=rir0*mono 
                if rir==1:
                    ind_estress1=rir1*mono 
                if rir==2:
                    ind_estress1=rir2*mono
                if rir==3:
                    ind_estress1=rir3*mono
                if rir==4:
                    ind_estress1=rir4*mono
                ind_estress2=ind_estress1
            ind_estress=ind_estress2
            
            #FUERZA TRABAJO POTENCIA
            fuer = peso3*9.8  #expresados Newton
            trab = fuer * 0.4 #expresados joules
            pot = trab / ttrep1#tiempo de tension #expresados watss
            #FECHA_MES  FECHA_SEMANA FECHA_SESION
            
            
            semana2=fechain.isocalendar()
            mes2=fechain.month
            anio2=fechain.year
            fecha_mes=str(anio2) +"-"+str(mes2)
            fecha_sem=str(semana2[0])+"-"+str(semana2[1])
            fecha_sesion=fecha_sem+"-"+str(secf)
            
            #******************************************************************************************
            d1 = sec1 #codigo ID
            d2 = fechain
            d3 = horain
            d4 = fecha_mes#FECHA MES
            d5 = fecha_sem#FECHA SEMANA
            d6 = secf# NUMERO DE SESION --*********************************** EDITAR SESION OK REVISION
            d7 = fecha_sesion#FSESION
            d8 = anio2
            d9 = (self.ids.sesion_muscular1.text) #SESION MUSCULAR
            d10 = abrv1#abreviatura
            d11 = sesion_ejercicio
            d12 = sece#"numero de series por ejercicio"
            d13 = secea#"numero de series totales" **********************************EDITAR
            d14 = self.ids.ti_peso1.text
            d15 =pesot#PESO TOTAL
            d16 = self.ids.ti_ttrep.text
            d17 = self.ids.ti_repeticion.text
            d18 = refect#repeticiones efectivas
            d19 = self.ids.ti_rir.text
            d20 = self.ids.ti_rpe.text
            d21 = self.ids.ti_descanso.text
            d22 = round(ttrep,1)#tiempo total por repeticion
            d23 = round(ttsts,1)#total tiempo toda las series sesion en minuto
            d24 = round(tdes,1) #total descanso sesion en minuto
            d25 = round(tdus,1) # total duracion sesion
            d26 = round(dserie,1) #densidad por serie 
            d27 = round(dsesion,1) #densidad por sesion
            d28 = vol#VOLUMEN  
            d29 = round(rm,1) 
            d30 = round(rmd,1)#1RM DINAMICA                       
            d31 = round(rm_porc,1)#1RM_PORC
            d32 = int(ton)#TONELAJE
            d33 = int(ton_acum)#TONELAJE ACUMULADO
            d34 = round(promp,1)#PROM_PESO
            d35 = maxp#MAX_PESO
            d36 = round(ind_estress,1)#INDICE DE ESTRESS
            d37 = int(fuer)#FUERZA
            d38 = int(trab) #TRABAJO
            d39 = int(pot) #POTENCIA
            a1=(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25,d26,d27,d28,d29,d30,d31,d32,d33,d34,d35,d36,d37,d38,d39)
            s1 = 'INSERT INTO SESION_EJERCICIO(ID, FECHA, HORA, FMES, FSEM, SESION, FSESION, ANIO, SESION_MUSCULAR, ABRV, EJERCICIO, SERIE, SERIES,  PESO, PESOT, TT, REP, REPEFECT, RIR, RPE, DESC, TTREP, TTSTS, TDES, TDUS, DSERIE, DSESION, VOLUMEN, RM, RMD, RM_PORC, TON, TON_ACUM, PROM_PESO, MAX_PESO, INDE, FUER, TRAB, POT)'
            s2 = 'VALUES(%s, "%s","%s","%s","%s", %s,"%s", %s, "%s", "%s","%s", %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)' % a1
            cursor = con.cursor()
            cursor.execute(s1+' '+s2)
            con.commit()
            con.close()
            #**********************************************insertdata_ejercicio_secundario**********************************
            con = sqlite3.connect(self.mainwid.DB_PATH)
            cursor_consulta5 = con.cursor()
            s_m=sesion_muscular2
            sr = f"select * from '{s_m}' WHERE EJERCICIO ='{sesion_ejercicio}'" 
            cursor_consulta5.execute(sr)
            resul=cursor_consulta5.fetchall()#resultado = lista original base de dato
            
            dt1 = resul[0][5] #pecho
            dt2 = resul[0][6] #espalda
            dt3 = resul[0][7] #abdomen
            dt4 = resul[0][8] #hombro
            dt5 = resul[0][9] #bicep
            dt6 = resul[0][10] #tricep
            dt7 = resul[0][11] #antebrazo
            dt8 = resul[0][12] #cuadricep
            dt9 = resul[0][13] #isquios
            dt10 = resul[0][14] #abductores
            dt11 = resul[0][15] #pantorrilla
            dt12 = resul[0][16] #gluteo
            cursor_consulta5.close()
            if dt1!=0:
                a=round((dt1* sece)/100,1)
            else:
                a=0
            b1=a
            if dt2!=0:
                a=round((dt2* sece)/100,1)
            else:
                a=0
            b2=a
            if dt3!=0:
                a=round((dt3* sece)/100,1)
            else:
                a=0
            b3=a
            if dt4!=0:
                a=round((dt4* sece)/100,1)
            else:
                a=0
            b4=a
            if dt5!=0:
                a=round((dt5* sece)/100,1)
            else:
                a=0
            b5=a
            if dt6!=0:
                a=round((dt6* sece)/100,1)
            else:
                a=0
            b6=a
            if dt7!=0:
                a=round((dt7* sece)/100,1)
            else:
                a=0
            b7=a
            if dt8!=0:
                a=round((dt8* sece)/100,1)
            else:
                a=0
            b8=a
            if dt9!=0:
                a=round((dt9* sece)/100,1)
            else:
                a=0
            b9=a
            if dt10!=0:
                a=round((dt10* sece)/100,1)
            else:
                a=0
            b10=a
            if dt11!=0:
                a=round((dt11* sece)/100,1)
            else:
                a=0
            b11=a
            if dt12!=0:
                a=round((dt12* sece)/100,1)
            else:
                a=0
            b12=a
            a1=(sec1, fechain, horain, fecha_mes, fecha_sem, secf, fecha_sesion, anio2, sece, secea, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12)
            s1 = f'INSERT INTO "SESION_EJERCICIO2"(ID, FECHA, HORA, FMES, FSEM, SESION, FSESION, ANIO, SERIE, SERIES, PEC, ESP, ABD, HOM, BIC, TRI, ANT, CUA, ISQ, ABDU, PAN, GLU)'
            s2 = 'VALUES( %s, "%s", "%s", "%s", "%s", %s, "%s", %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)' % a1
            cursor = con.cursor()
            cursor.execute(s1+' '+s2)
            con.commit()
            con.close()
            
            #********************insertdata_ejercicio_secundario**********************************
            self.mainwid.goto_database_sesion_ejercicio()
        except Exception as e:
                message = self.mainwid.Popup.ids.message
                self.mainwid.Popup.open()
                self.mainwid.Popup.title = "Data base error"
                message.text = 'Uno o más campos están vacíos'
                print(e)

    def database_ejercicio(self):
        self.mainwid.goto_database_sesion_ejercicio()
    #BOTON DE INICIO Y ATRAS
    def back_to_StartWid(self):
        self.mainwid.goto_start()
        
    
        
# #******************************************************************************
# #*FIN************QUINTA VENTANA**INGRESAR SESION EJERCICIO*********************
# #******************************************************************************

# #******************************************************************************
# #*********SEXTA VENTANA**MODIFICAR SESION EJERCICIO****************************
# #****************************************************************************** 
#********************DATEDATA SESION EJERCICIO GENERAL***************************
class DataBase_sesion_ejercicio(MDBoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(DataBase_sesion_ejercicio,self).__init__()
        self.mainwid = mainwid

    def check_memory_sesion_ejercicio(self):
        self.ids.agregar_ejercicio.clear_widgets()#LIMPIAR  WIDGET ScrollView
        self.ids.inicio_ejercicio.clear_widgets()#LIMPIAR WIDGET BoxLayout
        wid = Button_atras_sesion_ejercicio(self.mainwid)#BOTON INICIO
        self.ids.inicio_ejercicio.add_widget(wid)#BOTON INICIO
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor = con.cursor()
        fechain1=str(date.today())
        s2=f"select FECHA, ID, EJERCICIO, SERIE, PESO, TT, REP, REPEFECT, RIR, RPE, DESC, RM, RM_PORC, RMD, VOLUMEN, TON, TON_ACUM, PESOT, PROM_PESO, MAX_PESO from SESION_EJERCICIO WHERE FECHA ='{fechain1}'" 
        cursor.execute(s2)
        resultado=cursor.fetchall()
        for i in resultado:
            wid = DataWid_sesion_ejercicio(self.mainwid)
            r1 = str(i[2])+'\n'
            r2 = 'SERIE: '+str(i[3])+'     '+'PESO: '+str(i[4])+'  KG'+'     '+'TT: '+str(i[5])+'\n'
            r3 = 'RMD: '+str(i[13])+' KG'+'\n'
            r4 = 'REP: '+str(i[6])+'     '+'REPEFECT: '+str(i[7])+'\n'
            r5 = 'RIR: '+str(i[8])+'     '+'RPE: '+str(i[9])+'     '+'DESC: '+str(i[10])+' MIN'+'\n'
            r6 = 'RM: '+str(i[11])+' KG'+'    '+'RM_% : '+str(i[12])+' %''\n'
            r7 = 'TON: '+str(i[15])+'     '+'TON_ACUM: '+str(i[16])+'\n'
            r8 = 'VOL: '+str(i[14])+'     '+'PESOT: '+str(i[17])+'\n'
            r9 ='PROM_P: '+str(i[18])+'     '+'MAX_P: '+str(i[19])
            wid.data_id = str(i[1])
            wid.data = r1+r2+r3+r4+r5+r6+r7+r8+r9
            self.ids.agregar_ejercicio.add_widget(wid)
        wid = Button_inicio_sesion_ejercicio(self.mainwid)#BOTON AGREGAR
        self.ids.inicio_ejercicio.add_widget(wid)#BOTON AGREGAR
        con.close()

class DataWid_sesion_ejercicio(MDBoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(DataWid_sesion_ejercicio,self).__init__()
        self.mainwid = mainwid

    def update_data(self,data_id):
        self.mainwid.goto_UpdateData_sesion_ejercicio_G(data_id)
    
class Button_atras_sesion_ejercicio(MDRaisedButton):#CREAR BOTON AGREGAR
    def __init__(self,mainwid,**kwargs):
        super(Button_atras_sesion_ejercicio,self).__init__()
        self.mainwid = mainwid

    def back_to_insert_sesion_ejercicio(self):
        self.mainwid.goto_Insert_ejercicio_sesion_muscular() 

class Button_inicio_sesion_ejercicio(MDRaisedButton):#CREAR BOTON INICIO
    def __init__(self,mainwid,**kwargs):
        super(Button_inicio_sesion_ejercicio,self).__init__()
        self.mainwid = mainwid

    def back_to_StartWid(self):
        self.mainwid.goto_start()
#********************DATEDATA SESION EJERCICIO GENERAL***************************
# #******************************************************************************
# #**FIN*******SEXTA VENTANA**MODIFICAR SESION EJERCICIO*************************
# #******************************************************************************

# # *****************************************************************************
# #****INICIO*****SEPTIMA VENTANA**MODIFICAR SESION EJERCICIO********************
# #******************************************************************************
#********************UPDATEDATA SESION EEJERCICIO GENERAL*****************************************
class UpdateData_sesion_ejercicio_G(MDBoxLayout):
    def __init__(self,mainwid,data_id,**kwargs):
        super(UpdateData_sesion_ejercicio_G,self).__init__()
        self.mainwid = mainwid
        self.data_id = data_id
        self.check_memory_sesion_ejercicio_G()

    def check_memory_sesion_ejercicio_G(self):
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor = con.cursor()
        #s_muscular4=sm2
        #s = f"select EJERCICIO, FECHA, PESO, TT, REP, RIR, RPE, DESC from '{s_muscular4}' WHERE ID ="
        s = 'select EJERCICIO, FECHA, PESO, TT, REP, RIR, RPE, DESC from SESION_EJERCICIO where ID='
        cursor.execute(s+self.data_id)
        for i in cursor:
            self.ids.ti_ejercicio.text = i[0]
            self.ids.ti_fecha.text = i[1]
            self.ids.ti_peso.text = str(i[2])
            self.ids.ti_ttrep.text = str(i[3])
            self.ids.ti_repeticion.text = str(i[4])
            self.ids.ti_rir.text = str(i[5])
            self.ids.ti_rpe.text = str(i[6])
            self.ids.ti_descanso.text = str(i[7])   
        con.close()

    def update_data_sesion_ejercicio_G(self):
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor = con.cursor()
        d1 = self.ids.ti_ejercicio.text
        d2 = self.ids.ti_fecha.text
        d3 = self.ids.ti_peso.text
        d4 = self.ids.ti_ttrep.text
        d5 = self.ids.ti_repeticion.text
        d6 = self.ids.ti_rir.text
        d7 = self.ids.ti_rpe.text 
        d8 = self.ids.ti_descanso.text
        a1 = (d1,d2,d3,d4,d5,d6,d7,d8)
        s1 = 'UPDATE SESION_EJERCICIO SET'
        s2 = 'EJERCICIO="%s",FECHA="%s",PESO=%s,TT=%s,REP=%s,RIR=%s,RPE=%s,DESC=%s' % a1
        s3 = 'WHERE ID=%s' % self.data_id
        try:
            cursor.execute(s1+' '+s2+' '+s3)
            con.commit()
            con.close()
            self.mainwid.goto_database_sesion_ejercicio()
        except Exception as e:
            message = self.mainwid.Popup.ids.message
            self.mainwid.Popup.open()
            self.mainwid.Popup.title = "Data base error"
            if '' in a1:
                message.text = 'Uno o más campos están vacíos'
            else: 
                message.text = str(e)
            con.close()

    def delete_data_sesion_ejercicio_G(self):
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor = con.cursor()
        s = 'delete from SESION_EJERCICIO where ID='+self.data_id
        s1 = 'delete from SESION_EJERCICIO2 where ID='+self.data_id
        cursor.execute(s)
        cursor.execute(s1)
        con.commit()
        con.close()
        self.mainwid.goto_database_sesion_ejercicio()    
    
    def back_to_StartWid(self):
        self.mainwid.goto_start()
    def back_to_dbw(self):
        self.mainwid.goto_database_sesion_ejercicio() 
#********************UPDATEDATA GENERAL*****************************************
# # # ***************************************************************************
# #****FIN*****SEPTIMA VENTANA**MODIFICAR SESION EJERCICIO***********************
# #******************************************************************************  

# # *****************************************************************************
# #****INICIO*****OCTAVA VENTANA**MODIFICAR SESION EJERCICIO********************
# #******************************************************************************
#********************UPDATEDATA SESION EEJERCICIO GENERAL*****************************************
class Nivel_intensidad(MDBoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(Nivel_intensidad,self).__init__()
        self.mainwid = mainwid
        self.agregar_spinner2()
        self.grafica()
        
    cont_graf1 =1# tomardato()
    cont1 = StringProperty('1')
    def disminuir_boton_grafica1(self):
        self.cont_graf1=int(self.ids.cont_graf1.text )   
        self.cont_graf1 = self.cont_graf1 + 1
        valor=self.cont_graf1
        if valor<=creg1:
            self.cont1= str(self.cont_graf1)
            
    def aumentar_boton_grafica1(self):
        self.cont_graf1 = self.cont_graf1 - 1
        valor=self.cont_graf1
        if valor>=1:
            self.cont1= str(self.cont_graf1)
        
    def agregar_spinner2(self):
        try:
            global sm3
            con = sqlite3.connect(self.mainwid.DB_PATH)
            cursor_consulta_2 = con.cursor()
            sm3=(self.ids.indicador_musculo.text)
            si2=f"select EJERCICIO from '{sm3}'"
            cursor_consulta_2.execute(si2)
            resultado2=cursor_consulta_2.fetchall()#resultado = lista original base de dato
            resul2=[]
            for i in resultado2:
                y= i[-1]
                resul2.append(y)
            lista2=resul2
            
            self.ids.indicador_ejercicio.clear_widgets()#LIMPIAR  WIDGET ScrollView
            wid=self.SpinnerObject=Spinner(text='SELECCIONE_EJERCICIOS', values=lista2,sync_height= True)
            self.SpinnerObject.bind(text=self.on_spinner_select_sesion_ejercicio2)
            self.ids.indicador_ejercicio.add_widget(wid)#AGREGAR BOTON A LA VENTANA 
        except Exception as e:
            print(type(e).__name__,"-" "  No hay registro en la tabla spiner")
            
    def on_spinner_select_sesion_ejercicio2(self,spinner,dato3): 
        global sesion_ejercicio_ind
        sesion_ejercicio_ind=dato3

    def grafica(self):
        try:
            #*************DATA BASE CONFIGURACION*********************************************************
            con = sqlite3.connect(self.mainwid.DB_PATH)
            ind_ejercicio=sesion_ejercicio_ind
            sql1=f"select * from SESION_EJERCICIO WHERE EJERCICIO ='{ind_ejercicio}'" 
            df1= pd.read_sql_query(sql1,con)
            dfp=df1
            
            cant_serie=df1[["SERIES"]]
            global creg1
            lserie=list(cant_serie['SERIES'])
            creg1=len(lserie)
            if creg1>=5:
                a=int(self.ids.cont_graf1.text )
                rmin= creg1 - (a + 3) 
                rmax= rmin + 4
            else:
                rmin= 1
                rmax= creg1
                
            cond1=df1["SERIES"]>=rmin
            df1=df1[cond1]
            cond2=df1["SERIES"]<=rmax
            df1=df1[cond2]
            
            rm_porc=list(df1['RM_PORC'])
            rm=list(df1['RM']) 
            peso1=list(df1['PESO'])
            rep=list(df1['REP'])
            repefect=list(df1['REPEFECT'])
            desc=list(df1['DESC'])
            ttrep=list(df1['TTREP'])
            ton=list(df1['TON'])
            fuer=list(df1['FUER'])
            trab=list(df1['TRAB'])
            pot=list(df1['POT'])
            
            cant_seried=df1[["SERIES"]]
            seried=list(cant_seried['SERIES'])
            ult_reg=max(seried)
            #*************DATA BASE CONFIGURACION*********************************************************
            # #GRAFICA1**********************************************************************************  
            self.fig , self.ax = plt.subplots(1,dpi=90,figsize=(5,4), sharey=False,facecolor='white' )
            self.ax.grid(alpha=0.5)
            self.ax.spines['right'].set_visible(False)
            self.ax.spines['top'].set_visible(False)
            self.ax.spines['bottom'].set_color("blue")
            self.ax.spines['left'].set_color("blue")
            self.ax.tick_params(color="blue", labelcolor="blue", direction="out",length=1, width=1)
            plt.xlim(seried[0],max(seried))
            plt.ylim(min(rm_porc)-5,(max(rm_porc)+5))
            plt.xlim(right=max(seried)+0.5)
            plt.xlim(left=min(seried)-0.5)
            plt.xticks(range(seried[0],ult_reg+1,1)) #secuencia uno a uno
            plt.plot(seried,rm_porc, marker=".",color="green")
            for i,j in zip(seried,rm_porc):
                self.ax.annotate(j, xy=(i -0.3, j +0.2), color="blue")
            plt.legend(['RM%'],bbox_to_anchor=(0, 1., 1.10, .102), loc='upper center', ncol=1, borderaxespad=0.,fontsize=8, columnspacing=0)
            plt.rcParams.update({'figure.max_open_warning': 0})
            plt.tight_layout()
            self.ids.box1.clear_widgets()#LIMPIAR  WIDGET ScrollView
            wid2=(FigureCanvasKivyAgg(plt.gcf()))
            self.ids.box1.add_widget(wid2)#AGREGAR BOTON A LA VENTANA 
            
            # #GRAFICA2**********************************************************************************  
            self.fig , self.ax = plt.subplots(1,dpi=90,figsize=(5,4), sharey=False,facecolor='white' )
            self.ax.grid(alpha=0.5)
            self.ax.spines['right'].set_visible(False)
            self.ax.spines['top'].set_visible(False)
            self.ax.spines['bottom'].set_color("blue")
            self.ax.spines['left'].set_color("blue")
            self.ax.tick_params(color="blue", labelcolor="blue", direction="out",length=1, width=1)
            
            plt.xlim(seried[0],max(seried))
            plt.ylim(min(peso1)-5,(max(rm)+10))
            plt.xlim(right=max(seried)+0.5)
            plt.xlim(left=min(seried)-0.5)
            plt.xticks(range(seried[0],ult_reg+1,1)) #secuencia uno a uno
            plt.plot(seried,peso1, marker=".",color="green")
            plt.plot(seried,rm, marker=".",color="orange")
            plt.legend(['PESO','RM'],bbox_to_anchor=(0, 1.0, .9, .102), loc='upper center', ncol=2, mode="expand", borderaxespad=0.,fontsize=8, columnspacing=0)
            plt.rcParams.update({'figure.max_open_warning': 0})
            #plt.tight_layout()
            for i,j in zip(seried,peso1):
                self.ax.annotate(j, xy=(i -0.3, j +0.2), color="blue")
            for i,j in zip(seried,rm):
                self.ax.annotate(j, xy=(i -0.3, j +0.2), color="blue")
            self.ids.box2.clear_widgets()#LIMPIAR  WIDGET ScrollView
            wid=(FigureCanvasKivyAgg(plt.gcf()))
            self.ids.box2.add_widget(wid)#AGREGAR BOTON A LA VENTANA   
            
            # #GRAFICA3**********REPETICIONES EFECTIVA*******************************************************
            self.fig2 , self.ax = plt.subplots(1,dpi=90,figsize=(5,4), sharey=False,facecolor='white' )
            self.ax.spines['right'].set_visible(False)
            self.ax.spines['top'].set_visible(False)
            self.ax.spines['bottom'].set_color("blue")
            self.ax.spines['left'].set_visible(False)
            self.ax.tick_params(color="blue", labelcolor="blue", direction="out",length=0, width=0)
            plt.xlim(seried[0],max(seried))
            plt.ylim(0,(max(rep)+2))
            plt.xlim(right=max(seried)+0.5)
            plt.xlim(left=min(seried)-0.5)
            plt.yticks(fontsize=1)
            plt.xticks(range(seried[0],ult_reg+1,1)) #secuencia uno a uno
            bar_width =.30
            c1=int(seried[0])
            c2=int(ult_reg)+1
            co=np.arange(c1,c2)
            plt.bar(co - bar_width/2,rep, bar_width, color="green")
            plt.bar(co +bar_width/2,repefect, bar_width,color="orange")
            for i,j in zip(co,rep):
                self.ax.annotate(j, xy=(i -0.3, j +0.2),color="blue")
            for i,j in zip(co,repefect):
                self.ax.annotate(j, xy=(i +0.1, j +0.2),color="blue")
            plt.legend(['REP','REPEFECT'],bbox_to_anchor=(0, 1., .9, .102), loc='upper center', ncol=2, mode="expand", borderaxespad=0.,fontsize=8, columnspacing=0)
            plt.rcParams.update({'figure.max_open_warning': 0})
            plt.tight_layout()
            self.ids.box3.clear_widgets()#LIMPIAR  WIDGET ScrollView
            wid2=(FigureCanvasKivyAgg(plt.gcf()))
            self.ids.box3.add_widget(wid2)#AGREGAR BOTON A LA VENTANA 
            
            # #GRAFICA4**********************************************************************************  
            self.fig2 , self.ax = plt.subplots(1,dpi=90,figsize=(5,4), sharey=False,facecolor='white' )
            self.ax.spines['right'].set_visible(False)
            self.ax.spines['top'].set_visible(False)
            self.ax.spines['bottom'].set_color("blue")
            self.ax.spines['left'].set_visible(False)
            self.ax.tick_params(color="blue", labelcolor="blue", direction="out",length=0, width=0)
            plt.xlim(seried[0],max(seried))
            plt.ylim(min(ton)-50,(max(ton)+50))
            plt.xlim(right=max(seried)+0.5)
            plt.xlim(left=min(seried)-0.5)
            plt.yticks(fontsize=1)
            plt.xticks(range(seried[0],ult_reg+1,1)) #secuencia uno a uno
            bar_width =.30
            c1=int(seried[0])
            c2=int(ult_reg)+1
            co=np.arange(c1,c2)
            plt.bar(co - bar_width/2,ton, bar_width, color="green")
            for i,j in zip(co,ton):
                self.ax.annotate(j, xy=(i -0.3, j +0.2),color="blue")
            plt.legend(['TON'],bbox_to_anchor=(0, 1., 1.10, .102), loc='upper center', ncol=1, borderaxespad=0.,fontsize=8, columnspacing=0)
            plt.rcParams.update({'figure.max_open_warning': 0})
            plt.tight_layout()
            self.ids.box4.clear_widgets()#LIMPIAR  WIDGET ScrollView
            wid2=(FigureCanvasKivyAgg(plt.gcf()))
            self.ids.box4.add_widget(wid2)#AGREGAR BOTON A LA VENTANA 
            
            # #GRAFICA5**********************************************************************************  
            self.fig2 , self.ax = plt.subplots(1,dpi=90,figsize=(5,4), sharey=False,facecolor='white' )
            self.ax.spines['right'].set_visible(False)
            self.ax.spines['top'].set_visible(False)
            self.ax.spines['bottom'].set_color("blue")
            self.ax.spines['left'].set_visible(False)
            self.ax.tick_params(color="blue", labelcolor="blue", direction="out",length=0, width=0)
            plt.xlim(seried[0],max(seried))
            plt.ylim(0,(max(desc)+2))
            plt.xlim(right=max(seried)+0.5)
            plt.xlim(left=min(seried)-0.5)
            plt.yticks(fontsize=1)
            plt.xticks(range(seried[0],ult_reg+1,1)) #secuencia uno a uno
            bar_width =.30
            c1=int(seried[0])
            c2=int(ult_reg)+1
            co=np.arange(c1,c2)
            plt.bar(co - bar_width/2,desc, bar_width, color="green")
            plt.bar(co +bar_width/2,ttrep, bar_width,color="orange")
            for i,j in zip(co,desc):
                self.ax.annotate(j, xy=(i -0.3, j +0.2),color="blue")
            for i,j in zip(co,ttrep):
                self.ax.annotate(j, xy=(i +0.1, j +0.2),color="blue")
            plt.legend(['DESC','TTREP'],bbox_to_anchor=(0, 1., .9, .102), loc='upper center', ncol=2, mode="expand", borderaxespad=0.,fontsize=8, columnspacing=0)
            plt.rcParams.update({'figure.max_open_warning': 0})    
            plt.tight_layout()
            self.ids.box5.clear_widgets()#LIMPIAR  WIDGET ScrollView
            wid2=(FigureCanvasKivyAgg(plt.gcf()))
            self.ids.box5.add_widget(wid2)#AGREGAR BOTON A LA VENTANA 
            
            # #GRAFICA6**********************************************************************************  
            self.fig2 , self.ax = plt.subplots(1,dpi=90,figsize=(5,4), sharey=False,facecolor='white' )
            self.ax.spines['right'].set_visible(False)
            self.ax.spines['top'].set_visible(False)
            self.ax.spines['bottom'].set_color("blue")
            self.ax.spines['left'].set_visible(False)
            self.ax.tick_params(color="blue", labelcolor="blue", direction="out",length=0, width=0)
            plt.xlim(seried[0],max(seried))
            plt.ylim(min(pot)/2,(max(fuer)+200))
            plt.xlim(right=max(seried)+0.5)
            plt.xlim(left=min(seried)-0.5)
            plt.yticks(fontsize=1)
            plt.xticks(range(seried[0],ult_reg+1,1)) #secuencia uno a uno
            bar_width =.30
            c1=int(seried[0])
            c2=int(ult_reg)+1
            co=np.arange(c1,c2)
            plt.bar(co - bar_width/2,fuer, bar_width, color="green")
            plt.bar(co +bar_width/2,trab, bar_width,color="orange")
            plt.bar(co +.45,pot, .30,color="blue")
            for i,j in zip(co,fuer):
                self.ax.annotate(j, xy=(i -0.3, j +0.2),color="blue")
            for i,j in zip(co,trab):
                self.ax.annotate(j, xy=(i +0.1, j +0.2),color="blue")
            for i,j in zip(co,pot):
                self.ax.annotate(j, xy=(i +0.3, j +0.2),color="blue")
            plt.legend(['FUER','TRAB','POT'],bbox_to_anchor=(0, 1., .9, .102), loc='upper center', ncol=3, mode="expand", borderaxespad=0.,fontsize=8, columnspacing=0)
            plt.rcParams.update({'figure.max_open_warning': 0})    
            plt.tight_layout()
            self.ids.box6.clear_widgets()#LIMPIAR  WIDGET ScrollView
            wid2=(FigureCanvasKivyAgg(plt.gcf()))
            self.ids.box6.add_widget(wid2)#AGREGAR BOTON A LA VENTANA 
            
            
            # #GRAFICA7**********************************************************************************  
            self.fig2 , self.ax = plt.subplots(1,dpi=90,figsize=(5,4), sharey=False,facecolor='white' )
            data_resul=dfp.groupby(["SESION_MUSCULAR"])[["DESC"]].mean().unstack()
            data_resul1=dfp.groupby(["SESION_MUSCULAR"])[["TTREP"]].mean().unstack().round(1)
            desc1=list(data_resul['DESC']) 
            ttrep1=list(data_resul1['TTREP'])
            nombres=["DESCANSO","TTREP"]
            tamaño=[desc1,ttrep1]
            if len(nombres)==1:
                explotar=[0.05]
            elif len(nombres)==2:
                explotar=[0.05,0.05]
            elif len(nombres)==3:
                explotar=[0.05,0.05,0.05]
            plt.pie(tamaño, explode=explotar,colors=['green','orange'],
            autopct = '%1.0f%%', pctdistance = 0.4,
            shadow=True, startangle=90, radius=0.8,
            labeldistance=0.6), plt.tight_layout()
            plt.axis('equal')
            plt.legend(['DESC','TTREP'],bbox_to_anchor=(0, 1., .9, .102), loc='upper center', ncol=2,mode="expand", borderaxespad=0.,fontsize=8, columnspacing=0)
            plt.rcParams.update({'figure.max_open_warning': 0})    
            plt.tight_layout()
            self.ids.box7.clear_widgets()#LIMPIAR  WIDGET ScrollView
            wid2=(FigureCanvasKivyAgg(plt.gcf()))
            self.ids.box7.add_widget(wid2)#AGREGAR BOTON A LA VENTANA 
            
            
        except Exception as e:
            print(type(e).__name__,"-" "  No hay registro en la tabla de la base de dato grafica porcentaje intensidad")
    #*****************************************************************************************************************
    
    def back_to_StartWid(self):
        self.mainwid.goto_start()
# # *****************************************************************************
# #****INICIO*****OCTAVA VENTANA**MODIFICAR SESION EJERCICIO********************
# #******************************************************************************  

# # *****************************************************************************
# #****INICIO*****NOVENA VENTANA**MODIFICAR SESION EJERCICIO********************
# #******************************************************************************
#********************UPDATEDATA SESION EEJERCICIO GENERAL*****************************************

class Nivel_estress(MDBoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(Nivel_estress,self).__init__()
        self.mainwid = mainwid
        self.actualizar()
        
    def actualizar(self):
        self.grafica_sesion_musculo()
        self.grafica_sesion_ejercicio()
        self.grafica_series()
        self.grafica_duracion()
        
    def time(self):
        time.sleep(0.5)
    cont_graf =1# tomardato()
    cont = StringProperty('1')
    def disminuir_boton_grafica(self):
        self.cont_graf=int(self.ids.cont_graf.text )   
        self.cont_graf = self.cont_graf + 1
        valor=self.cont_graf
        if valor<=creg:
            self.cont= str(self.cont_graf)

    def aumentar_boton_grafica(self):
        self.cont_graf = self.cont_graf - 1
        valor=self.cont_graf
        if valor>=1:
            self.cont= str(self.cont_graf)

    def grafica_sesion_musculo(self):
        try:
            tiempo=self.ids.tiempo.text
            if tiempo=="SESION":
                ftiempo="FSESION"
                subt="SESION"
            elif tiempo=="SEMANA":
                ftiempo="FSEM"
                subt="SEMANA"
            elif tiempo=="MES":
                ftiempo="FMES"
                subt="MES"
            elif tiempo=="AÑO":
                ftiempo="ANIO"
                subt="AÑO"
            #DATA BASE ORIGINAL
            con = sqlite3.connect(self.mainwid.DB_PATH)
            sql1=f"select SESION, {ftiempo}, SESION_MUSCULAR, INDE from SESION_EJERCICIO" 
            df1= pd.read_sql_query(sql1,con)   #.fillna("0",inplace=True) se aplica cuando hay valores null en columnas o filas
            #CANTIDAD DE REGISTRO SESION
            cant_sesion=df1[["SESION"]].drop_duplicates(["SESION"],keep="first")
            global creg
            l1=list(cant_sesion['SESION'])
            creg=len(l1)
            a=int(self.ids.cont_graf.text ) 
            
            if "FSESION"==f"{ftiempo}":
                rmin=creg-a
                rmax=rmin+1
            elif "FSEM"==f"{ftiempo}":
                rmin=creg-a-2
                rmax=rmin+3
            elif "FMES"==f"{ftiempo}":
                rmin=creg-a-2
                rmax=rmin+3
            elif "ANIO"==f"{ftiempo}":
                rmin=creg/creg
                rmax=creg
            rmin1=rmin
            rmax1=rmax    

            cond1=df1["SESION"]>=rmin1 
            df1=df1[cond1]
            cond2=df1["SESION"]<=rmax1
            df1=df1[cond2]
            #******************************************************************************************************
            #GRAFICA
            graf1=df1.groupby([f"{ftiempo}","SESION_MUSCULAR"])[["INDE"]].sum().unstack()
            # ORGANIZA TOTAL SESION MUSCULO E INDE
            sum_inde=df1[[f"{ftiempo}","SESION_MUSCULAR","INDE"]].groupby([f"{ftiempo}","SESION_MUSCULAR"])[["INDE"]].transform("sum").round()
            df_se=df1[["SESION_MUSCULAR"]]
            #CONCATENAR NUEVA TABLA
            dfe1=pd.concat([df_se,sum_inde],axis=1)
            dfe2=dfe1[["SESION_MUSCULAR","INDE"]].drop_duplicates(["SESION_MUSCULAR"],keep="first")
            l3=list(dfe2['INDE'])
            cant_sesiond=df1[["SESION"]].drop_duplicates(["SESION"],keep="first")
            ld=list(cant_sesiond['SESION'])

            self.fig3 , self.ax =  plt.subplots(1,dpi=90,figsize=(5,4), sharey=False,facecolor='white')
            self.fig3=graf1.plot(kind="bar")
            self.fig3.set_xticklabels(ld,rotation=90)
            self.fig3.spines['right'].set_visible(False)
            self.fig3.spines['top'].set_visible(False)
            self.fig3.spines['bottom'].set_color("blue")
            self.fig3.spines['left'].set_visible(False)
            #plt.xlim(l1[0]-1,max(l1)+1)
            plt.ylim(min(l1)/2,max(l3)+10)
            plt.grid(alpha=0.5, axis="y")
            plt.xlabel("",fontdict=None)
            plt.tick_params(color="blue", labelcolor="blue", direction="out",length=0, width=0,)
            plt.legend(bbox_to_anchor=(-0.2, .85, 1.32, .102), loc='lower center', ncol=2, mode="expand", borderaxespad=0.,fontsize=8, columnspacing=0)
            plt.rcParams.update({'figure.max_open_warning': 0})
            self.ids.box1.clear_widgets()#LIMPIAR  WIDGET ScrollView
            wid2=(FigureCanvasKivyAgg(plt.gcf()))
            self.ids.box1.add_widget(wid2)#AGREGAR BOTON A LA VENTANA 
            
            
        except Exception as e:
            print(type(e).__name__,"-" "  No hay registro en la tabla de la base de dato grafica sesion musculo_sesion") 
            print(e)
    #***************************FIN SESION MUSCULO******************************************************************
    def grafica_sesion_ejercicio(self):
        try:
            tiempo=self.ids.tiempo.text
            if tiempo=="SESION":
                ftiempo="FSESION"
                subt="SESION"
            elif tiempo=="SEMANA":
                ftiempo="FSEM"
                subt="SEMANA"
            elif tiempo=="MES":
                ftiempo="FMES"
                subt="MES"
            elif tiempo=="AÑO":
                ftiempo="ANIO"
                subt="AÑO"
            #DATA BASE ORIGINAL
            con = sqlite3.connect(self.mainwid.DB_PATH)
            sm3 = self.ids.nivel_estres_sm.text
            sql1=f"select SESION, {ftiempo}, ABRV, INDE from SESION_EJERCICIO WHERE SESION_MUSCULAR ='{sm3}'" #{sm3}
            df1= pd.read_sql_query(sql1,con)   #.fillna("0",inplace=True) se aplica cuando hay valores null en columnas o filas
            #CANTIDAD DE REGISTRO SESION
            cant_sesion=df1[["SESION"]].drop_duplicates(["SESION"],keep="first")
            l1=list(cant_sesion['SESION'])
            a=int(self.ids.cont_graf.text )  
            
            if "FSESION"==f"{ftiempo}":
                rmin=creg-a
                rmax=rmin+1
            elif "FSEM"==f"{ftiempo}":
                rmin=creg-a-2
                rmax=rmin+3
            elif "FMES"==f"{ftiempo}":
                rmin=creg-a-2
                rmax=rmin+3
            elif "ANIO"==f"{ftiempo}":
                rmin=creg/creg
                rmax=creg
            rmin1=rmin
            rmax1=rmax 
            cond1=df1["SESION"]>=rmin1 
            df1=df1[cond1]
            cond2=df1["SESION"]<=rmax1
            df1=df1[cond2]
            #****************************************************************************************************************
            #GRAFICA
            #graf1=df1.groupby([f"{ftiempo}","ABRV"])[["INDE"]].sum().unstack()
            graf2=pd.pivot_table(df1, index=[f"{ftiempo}"], values=["INDE"], columns=["ABRV"],fill_value=0, aggfunc="sum")
            # ORGANIZA TOTAL SESION MUSCULO E INDE
            sum_inde=df1[[f"{ftiempo}","ABRV","INDE"]].groupby([f"{ftiempo}","ABRV"])[["INDE"]].transform("sum").round()
            df_se=df1[["ABRV"]]
            #CONCATENAR NUEVA TABLA
            dfe1=pd.concat([df_se,sum_inde],axis=1)
            dfe2=dfe1[["ABRV","INDE"]].drop_duplicates(["ABRV"],keep="first")
            cant_sesiond=df1[["SESION"]].drop_duplicates(["SESION"],keep="first")
            ld=list(cant_sesiond['SESION'])
            l3=list(dfe2['INDE'])
            self.fig3 , self.ax =  plt.subplots(1,dpi=90,figsize=(5,4), sharey=False,facecolor='white')
            self.fig3=graf2.plot(kind="bar")
            self.fig3.set_xticklabels(ld,rotation=90)
            self.fig3.spines['right'].set_visible(False)
            self.fig3.spines['top'].set_visible(False)
            self.fig3.spines['bottom'].set_color("blue")
            self.fig3.spines['left'].set_visible(False)
            plt.ylim(min(l1)/2,max(l3)+1)
            plt.grid(alpha=0.5, axis="y")
            plt.xlabel("",fontdict=None)
            plt.tick_params(color="blue", labelcolor="blue", direction="out",length=0, width=0,)
            plt.suptitle(f"{sm3} NIVEL DE ESTRES x {subt}",size=10, color="green")
            plt.legend(bbox_to_anchor=(-0.2, -0.16, 1.32, .102), loc='lower center', ncol=2, mode="expand", borderaxespad=0.,fontsize=8, columnspacing=0.5)
            plt.rcParams.update({'figure.max_open_warning': 0})
            self.ids.box2.clear_widgets()#LIMPIAR  WIDGET ScrollView
            wid2=(FigureCanvasKivyAgg(plt.gcf()))
            self.ids.box2.add_widget(wid2)#AGREGAR BOTON A LA VENTANA 
        except Exception as e:
            print(type(e).__name__,"-" "  No hay registro en la tabla de la base de dato grafica sesion musculo_ejercicio") 
            print(e)
            
    def grafica_series(self):
        try:
            tiempo=self.ids.tiempo.text
            if tiempo=="SESION":
                ftiempo="FSESION"
                subt="SESION"
            elif tiempo=="SEMANA":
                ftiempo="FSEM"
                subt="SEMANA"
            elif tiempo=="MES":
                ftiempo="FMES"
                subt="MES"
            elif tiempo=="AÑO":
                ftiempo="ANIO"
                subt="AÑO"
            #DATA BASE ORIGINAL
            con = sqlite3.connect(self.mainwid.DB_PATH)
            sm3 = self.ids.nivel_estres_sm.text
            sql1=f"select SESION, {ftiempo}, ABRV, SERIES from SESION_EJERCICIO WHERE SESION_MUSCULAR ='{sm3}'" #{sm3}
            df1= pd.read_sql_query(sql1,con)   #.fillna("0",inplace=True) se aplica cuando hay valores null en columnas o filas
            #CANTIDAD DE REGISTRO SESION
            cant_sesion=df1[["SESION"]].drop_duplicates(["SESION"],keep="first")
            a=int(self.ids.cont_graf.text )  
            
            if "FSESION"==f"{ftiempo}":
                rmin=creg-a
                rmax=rmin+1
            elif "FSEM"==f"{ftiempo}":
                rmin=creg-a-2
                rmax=rmin+3
            elif "FMES"==f"{ftiempo}":
                rmin=creg-a-2
                rmax=rmin+3
            elif "ANIO"==f"{ftiempo}":
                rmin=creg/creg
                rmax=creg
            rmin1=rmin
            rmax1=rmax 
            cond1=df1["SESION"]>=rmin1 
            df1=df1[cond1]
            cond2=df1["SESION"]<=rmax1
            df1=df1[cond2]
            #****************************************************************************************************************
            #GRAFICA
            #graf1=df1.groupby([f"{ftiempo}","ABRV"])[["INDE"]].sum().unstack()
            graf2=pd.pivot_table(df1, index=[f"{ftiempo}"], values=["SESION"], columns=["ABRV"],fill_value=0, aggfunc="max")
            # ORGANIZA TOTAL SESION MUSCULO E INDE
            sum_inde=df1[[f"{ftiempo}","ABRV","SESION"]].groupby([f"{ftiempo}","ABRV"])[["SESION"]].transform("max").round()
            df_se=df1[["ABRV"]]
            #CONCATENAR NUEVA TABLA
            dfe1=pd.concat([df_se,sum_inde],axis=1)
            dfe2=dfe1[["ABRV","SESION"]].drop_duplicates(["ABRV"],keep="first")
            cant_sesiond=df1[["SESION"]].drop_duplicates(["SESION"],keep="first")
            ld=list(cant_sesiond['SESION'])
            l3=list(dfe2['SESION'])
            self.fig3 , self.ax =  plt.subplots(1,dpi=90,figsize=(5,4), sharey=False,facecolor='white')
            self.fig3=graf2.plot(kind="bar")
            self.fig3.set_xticklabels(ld,rotation=90)
            self.fig3.spines['right'].set_visible(False)
            self.fig3.spines['top'].set_visible(False)
            self.fig3.spines['bottom'].set_color("blue")
            self.fig3.spines['left'].set_visible(False)
            plt.ylim(0, max(l3)+1)
            plt.grid(alpha=0.5, axis="y")
            plt.xlabel("",fontdict=None)
            plt.tick_params(color="blue", labelcolor="blue", direction="out",length=0, width=0,)
            plt.suptitle(f"{sm3} SERIES x {subt}",size=10, color="green")
            plt.legend(bbox_to_anchor=(-0.2, -0.16, 1.32, .102), loc='lower center', ncol=2, mode="expand", borderaxespad=0.,fontsize=8, columnspacing=0.5)
            plt.rcParams.update({'figure.max_open_warning': 0})
            self.ids.box3.clear_widgets()#LIMPIAR  WIDGET ScrollView
            wid2=(FigureCanvasKivyAgg(plt.gcf()))
            self.ids.box3.add_widget(wid2)#AGREGAR BOTON A LA VENTANA 
        except Exception as e:
            print(type(e).__name__,"-" "  No hay registro en la tabla de la base de dato grafica series") 
            print(e)
            
    def grafica_duracion(self):
        try:
            tiempo=self.ids.tiempo.text
            if tiempo=="SESION":
                ftiempo="FSESION"
                subt="SESION"
            elif tiempo=="SEMANA":
                ftiempo="FSEM"
                subt="SEMANA"
            elif tiempo=="MES":
                ftiempo="FMES"
                subt="MES"
            elif tiempo=="AÑO":
                ftiempo="ANIO"
                subt="AÑO"
            #DATA BASE ORIGINAL
            con = sqlite3.connect(self.mainwid.DB_PATH)
            sm3 = self.ids.nivel_estres_sm.text
            sql1=f"select SESION, {ftiempo}, SESION_MUSCULAR, DESC, TTREP from SESION_EJERCICIO WHERE SESION_MUSCULAR ='{sm3}'" #{sm3}
            df1= pd.read_sql_query(sql1,con)   #.fillna("0",inplace=True) se aplica cuando hay valores null en columnas o filas
            #CANTIDAD DE REGISTRO SESION
            cant_sesion=df1[["SESION"]].drop_duplicates(["SESION"],keep="first")
            a=int(self.ids.cont_graf.text )  
            
            if "FSESION"==f"{ftiempo}":
                rmin=creg-a
                rmax=rmin+1
            elif "FSEM"==f"{ftiempo}":
                rmin=creg-a-2
                rmax=rmin+3
            elif "FMES"==f"{ftiempo}":
                rmin=creg-a-2
                rmax=rmin+3
            elif "ANIO"==f"{ftiempo}":
                rmin=creg/creg
                rmax=creg
            rmin1=rmin
            rmax1=rmax 
            cond1=df1["SESION"]>=rmin1 
            df1=df1[cond1]
            cond2=df1["SESION"]<=rmax1
            df1=df1[cond2]
            #****************************************************************************************************************
            #GRAFICA
            #graf1=df1.groupby([f"{ftiempo}","ABRV"])[["INDE"]].sum().unstack()
            graf2=pd.pivot_table(df1, index=[f"{ftiempo}"], values=["DESC","TTREP"], columns=["SESION_MUSCULAR"],fill_value=0, aggfunc="sum")
            # ORGANIZA TOTAL SESION MUSCULO E INDE
            sum_inde=df1[[f"{ftiempo}","SESION_MUSCULAR","DESC","TTREP"]].groupby([f"{ftiempo}","SESION_MUSCULAR"])[["DESC","TTREP"]].transform("sum").round()
            df_se=df1[["SESION_MUSCULAR"]]
            #CONCATENAR NUEVA TABLA
            dfe1=pd.concat([df_se,sum_inde],axis=1)
            dfe2=dfe1[["SESION_MUSCULAR","DESC"]].drop_duplicates(["SESION_MUSCULAR"],keep="first")
            cant_sesiond=df1[["SESION"]].drop_duplicates(["SESION"],keep="first")
            ld=list(cant_sesiond['SESION'])
            l3=list(dfe2['DESC'])
            self.fig3 , self.ax =  plt.subplots(1,dpi=90,figsize=(5,4), sharey=False,facecolor='white')
            self.fig3=graf2.plot(kind="bar")
            self.fig3.set_xticklabels(ld,rotation=90)
            self.fig3.spines['right'].set_visible(False)
            self.fig3.spines['top'].set_visible(False)
            self.fig3.spines['bottom'].set_color("blue")
            self.fig3.spines['left'].set_visible(False)
            plt.ylim(0, max(l3)+1)
            plt.grid(alpha=0.5, axis="y")
            plt.xlabel("",fontdict=None)
            plt.tick_params(color="blue", labelcolor="blue", direction="out",length=0, width=0,)
            plt.suptitle(f"{sm3} DURACION x {subt}",size=10, color="green")
            plt.legend(bbox_to_anchor=(-0.2, -0.16, 1.32, .102), loc='lower center', ncol=2, mode="expand", borderaxespad=0.,fontsize=8, columnspacing=0.5)
            plt.rcParams.update({'figure.max_open_warning': 0})
            self.ids.box4.clear_widgets()#LIMPIAR  WIDGET ScrollView
            wid2=(FigureCanvasKivyAgg(plt.gcf()))
            self.ids.box4.add_widget(wid2)#AGREGAR BOTON A LA VENTANA 
        except Exception as e:
            print(type(e).__name__,"-" "  No hay registro en la tabla de la base de dato grafica duracion") 
            print(e)
            
    def back_to_StartWid(self):
        self.mainwid.goto_start()
# # *****************************************************************************
# #****INICIO*****NOVENA VENTANA**MODIFICAR SESION EJERCICIO********************
# #******************************************************************************


#******************************************************
#**********APLICACION DE INICIALIZACION***************************
#******************************************************
class mainApp(MDApp):
    title="AOR_GYM"
    # def open_settings(self, *args):
    #     pass
    def build(self):
        self.theme_cls.primary_palette = 'Teal'
        return MainWid()
#*****************************************APLICACION PRINCIPAL

    
if __name__== '__main__':
    mainApp().run()