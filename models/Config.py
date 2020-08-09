#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.Logs import Logs
from  db.Insert import Insert
from  db.GetAll import GetAll
from  db.GetOne import GetOne
from db.Update import Update
from db.DropTables import DropTables
from db.CreateTables import CreateTables
from getmac import get_mac_address as gma
from datetime import datetime


class Config():
    def __init__(self):
        self.log   = Logs()
        self.tabla = "config"
        self.msn   = ""
    def inicializateClient(self):
        '''Funcion para iniciar configuracion del cliente'''
        self.createDatabase()
       
    def validateClient(self):
        '''Funcion para validar si el ciente ya etsa configurado'''
        #Validar que base de datos exista
        go = GetOne()
        
        return go.getOne("SELECT * FROM config")
       
    def reconfigClient(self):
        '''Funcion para reconfigurar el cliente'''
       
    def createDatabase(self):
        """CREAR BASE DE DATOS"""
        db = CreateTables()
        respuesta = db.createTablesDatabase()
        self.msn = db.msn
        return respuesta


    def deleteDatabase(self):
        db = DropTables()
        respuesta = db.dropTable()
        self.msn = db.msn
        return respuesta

    def getMac(self):
        return gma()
    
    def registerClient(self,sede):
        ins = Insert()
        fecha = str(datetime.now().day)+"/"+str(datetime.now().month)+"/"+str(datetime.now().year)
        respuesta = ins.insertOne("config",fecha+","+str(sede)+","+str(self.getMac()))
        if  respuesta == True:
            self.msn ="Registro exitoso"
            
        else:
            self.msn ="Ha ocurrido un error al registrar" 
        
        return respuesta


    