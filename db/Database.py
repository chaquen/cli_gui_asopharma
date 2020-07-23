#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
from  utils.Logs import Logs
from const import env

class Database:

    namebd = env.DB
    user = ''
    port = ''
    password = ''
    
    def __init__(self):
        self.log = Logs()
        #self.namebd = env.PATH_DB + env.DB
        print(self.namebd)

        
    def connection(self):
        try:
            self.log.info("Iniciando conexión connection "+self.namebd)
            self.conn = sqlite3.connect(self.namebd)    
            self.log.info("Conexión correcta connection")
        except sqlite3.Error as e:
            self.log.exception(e.args[0])
    def closeConnection(self):
        try:
            self.log.info("Cerrando conexión ")
            self.conn.close()
        except sqlite3.Error as e:
            self.log.error(e.args[0])
    
    def executeSelectSQL(self,sql,data=False):    
        try:
            self.log.info("Iniciando executeSelectSQL ")
            c = self.conn.cursor()
            if data == False: 
                c.execute(sql)
            else:
                c.execute(sql,data)      
                
            return c

        except sqlite3.Error as e:
            self.log.error(e.args[0])
            return False
    def executeSQL(self,sql,data=False):    
        try:
            self.log.info("Iniciando executeSQL "+sql)
            c = self.conn.cursor()
            if data == False: 
                c.execute(sql)
            else:
                c.execute(sql,data)      
            
            self.conn.commit()
                
            return c

        except sqlite3.Error as e:
            self.log.error(e.args[0])
            return False

    def executeMany(self,sql,data):
        try:
            self.log.info("Iniciando executeSQL")
            c = self.conn.cursor()
            c.executemany(sql,data)      
            
            self.conn.commit()
                
            return c

        except sqlite3.Error as e:
            self.log.error(e.args[0])
            return False
            



    
