#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  db.Database import Database
import sqlite3
from  utils.Logs import Logs

class Insert(Database):

    def __init__(self):
        self.log = Logs()
        print("INSERT "+self.namebd)

    def insertOne(self,table,data):
        try:
            self.log.info("Iniciando INSERT "+table+" "+data )
            self.connection()
            self.executeSQL("INSERT INTO "+table+" VALUES ("+data+")")
            self.conn.commit()
            self.closeConnection()
            return True
        except Exception as e:
            self.log.error(e.args[0])
            return False
    
    def insertMany(self,table,fields,values,data):
        try:
            self.log.info("Iniciando INSERT "+table+" ("+fields+") " )
            self.connection()
            sql = "INSERT INTO "+table+" ("+fields+") VALUES ("+values+")"
            return self.executeMany(sql,data) 
            
        except Exception as e:
            self.log.error(e.args[0])
