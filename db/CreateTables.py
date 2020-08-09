#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  db.Database import Database
from  utils.Logs import Logs
class CreateTables(Database):
    def __init__(self):
        self.log = Logs()
        self.sqlfile = "./sql/create.sql"
        self.msn = ""
        

    def createTable(self,sql):
        try:
            self.log.info("Iniciando CREATETABLE ")
            self.connection()
            c = self.conn.cursor()
            self.executeSQL(sql)
            self.closeConnection()  
            self.msn = "Tablas creadas"
            return True
        except Exception as e:
            self.log.error(e.args[0])
            self.msn = e.args[0]
            return False
    
    def createTablesDatabase(self):
        contentFile = open(self.sqlfile, "r")
        lines = []
        for line in contentFile:
            self.createTable(line)