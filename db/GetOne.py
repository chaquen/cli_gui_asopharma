#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  db.Database import Database
#import sqlite3
from  utils.Logs import Logs

class GetOne(Database):
    
    def __init__(self):
         self.log = Logs()


    def getOne(self,sql,data):
        try:
            self.log.info("Iniciando consulta getOne "+sql)
            print(data)
            self.connection()
            c = self.executeSelectSQL(sql,data)
            if c != False:
                data_query = c.fetchone()
                if data_query == None:
                       self.log.info("No se encontraron datos")
                       return False 
                self.log.info("Consulta realizada getOne "+' '.join(map(str,data_query)))
                self.closeConnection()                   
                return data_query
            else: 
                self.closeConnection()   
                self.log.info("No ha se han encontrado datos")                
            
                     
        except Exception as e:
            self.log.error(e.args[0])
            return False