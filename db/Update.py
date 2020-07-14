#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  db.Database import Database
#import sqlite3
from  utils.Logs import Logs

class Update(Database):

    def __init__(self):
        self.log = Logs()

    def update(self,table,setupdate,where,data):
        try:
            self.log.info("Iniciando UPDATE "+table+" SET "+setupdate + " WHERE "+where+" DATA "+' '.join(map(str,data)) )
            self.connection()
            self.executeSQL("UPDATE "+ table +" SET "+ setupdate +" WHERE  "+ where,data)
            """c = self.conn.cursor()
            sql="UPDATE "+ table +" SET "+ setupdate +" WHERE  "+ where
            c.execute(sql,data)        
            self.conn.commit()"""
            self.closeConnection()
        except Exception as e:
            self.log.error(e.args[0])
