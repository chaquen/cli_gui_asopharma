#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  db.Database import Database
import sqlite3
from  utils.Logs import Logs

class DropTable(Datatable):
    def __init()__:
        self.log = Logs()
    
    def dropTable(self):
        try:
            self.log.info("Iniciando DROPTABLE ")
            self.connection()
            c = self.conn.cursor()
            c.execute('''DROP TABLE IF EXISTS stocks''')
            self.conn.commit()
            self.closeConnection()
        except sqlite3.Error as e:
            self.log.error(e.args[0])