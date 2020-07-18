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
        
    def connection(self):
        try:
            self.log.info("Iniciando conexión connection")
            self.conn = sqlite3.connect(self.namebd)    
            self.log.info("Conexión correcta connection")
        except sqlite3.Error as e:
            self.log.error(e.args[0])
    def closeConnection(self):
        try:
            self.log.info("Cerrando conexión ")
            self.conn.close()
        except sqlite3.Error as e:
            self.log.error(e.args[0])
    
    def executeSelectSQL(self,sql,data=False):    
        try:
            self.log.info("Iniciando executeSelectSQL")
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
            self.log.info("Iniciando executeSQL")
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

    """def getAll(self):
        try:
            self.log.info("Iniciando consulta getAll")
            self.connection()
            c = self.conn.cursor()
            c.execute('SELECT * FROM stocks' )
            data= c.fetchall()
            self.log.info("Consulta realizada "+' '.join(map(str,data)))
            print("-...-")
            print(data)
        except sqlite3.Error as e:
            self.log.error(e.args[0])"""
    """def getOne(self):
        try:
            self.connection()
            c = self.conn.cursor()
            t = ('RHAT',)
            c.execute('SELECT * FROM stocks WHERE symbol=?', t)
            print(c.fetchone())
        except sqlite3.Error as e:
            self.log.error(e.args[0])"""

    """def insert(self):
        try:
            self.connection()
            c = self.conn.cursor()
            c.execute("INSERT INTO stocks VALUES ('2020-07-05','BUY','RHAT',100,35.14)")
            self.conn.commit()
            self.closeConnection()
        except sqlite3.Error as e:
            self.log.error(e.args[0])"""

    """def update(self):
        try:
            self.connection()
            c = self.conn.cursor()
            sql="UPDATE stocks SET symbol_text = ? WHERE  date_text = ?"
            data = ('666','2020-06-05')
            c.execute(sql,data)        
            self.conn.commit()
            self.closeConnection()
        except sqlite3.Error as e:
            self.log.error(e.args[0])"""

    """def delete():
        print('delete')    """

    """def createTable(self):
        try:
            self.connection()
            c = self.conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS stocks
                (date_text, trans_text, symbol_text, qty_real, price_real)''')
            self.conn.commit()
            self.closeConnection()  
        except sqlite3.Error as e:
            self.log.error(e.args[0])"""  

    """def dropTable(self):
        try:
            self.connection()
            c = self.conn.cursor()
            c.execute('''DROP TABLE IF EXISTS stocks''')
            self.conn.commit()
            self.closeConnection()
        except sqlite3.Error as e:
            self.log.error(e.args[0])"""
            



    
