#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  db.Database import Database
from  utils.Logs import Logs

class DropTables(Datatable):
    def __init()__:
        self.log = Logs()
    
    def dropTable(self):
        try:
            self.log.info("Iniciando DROPTABLE ")
            self.connection()
            c = self.conn.cursor()
            c.executeSQL('''DROP TABLE IF EXISTS stocks''')
            self.closeConnection()
        except Exception as e:
            self.log.error(e.args[0])
            return False