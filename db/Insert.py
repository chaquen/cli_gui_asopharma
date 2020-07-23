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
        except Exception as e:
            self.log.error(e.args[0])
    
    def insertMany(self,table,fields,values,data):
        try:
            self.log.info("Iniciando INSERT "+table+" ("+fields+") " )
            self.connection()
            
            sql = "INSERT INTO "+table+" ("+fields+") VALUES ("+values+")"
            print(data)
            self.executeMany(sql,data)
            self.conn.commit()
            self.closeConnection()
        except Exception as e:
            self.log.error(e.args[0])
