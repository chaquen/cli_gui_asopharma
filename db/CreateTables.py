#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  db.Database import Database
import sqlite3
from  utils.Logs import Logs

class CreateTables(Datatables):

    def __init__(self):
        self.log = Logs()

    def createTable(self):
        try:
            self.log.info("Iniciando CREATETABLE ")
            self.connection()
            c = self.conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS stocks
                (date_text, trans_text, symbol_text, qty_real, price_real)''')
            self.conn.commit()
            self.closeConnection()  
        except sqlite3.Error as e:
            self.log.error(e.args[0])
            return False