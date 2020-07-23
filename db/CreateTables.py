#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  db.Database import Database
#import sqlite3
from  utils.Logs import Logs
class CreateTables(Database):
    def __init__(self):
        self.log = Logs()
        print("CREATETABLE "+self.namebd)

    def createTable(self,sql):
        try:
            self.log.info("Iniciando CREATETABLE ")
            self.connection()
            c = self.conn.cursor()
            print(c)
            self.executeSQL(sql)
            self.closeConnection()  
        except Exception as e:
            self.log.error(e.args[0])
            return False