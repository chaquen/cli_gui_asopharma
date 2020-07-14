#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  db.Database import Database
import sqlite3
from  utils.Logs import Logs

class Delete(Database):

    def __init__(self):
        self.log = Logs()

    def delete(self,table,where,data):
        try:
            self.log.info("Iniciando DELETE "+table+"  WHERE "+where )
            self.connection()
            self.executeSQL("DELETE FROM  "+ table +" WHERE  "+ where,data)
            """c = self.conn.cursor()
            sql="DELETE FROM  "+ table +" WHERE  "+ where
            c.execute(sql,data)        
            self.conn.commit()"""
            self.closeConnection()
        except Exception as e:
            self.log.error(e.args[0])
