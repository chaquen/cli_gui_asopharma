#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  db.Database import Database
import sqlite3
from  utils.Logs import Logs

class Insert(Database):

    def __init__(self):
        self.log = Logs()

    def insert(self,table,data):
        try:
            self.log.info("Iniciando INSERT "+table+" "+data )
            self.connection()
            self.executeSQL("INSERT INTO "+table+" VALUES ("+data+")")
            self.conn.commit()
            self.closeConnection()
        except Exception as e:
            self.log.error(e.args[0])
