#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  db.Database import Database
from  utils.Logs import Logs

class DropTables(Database):
    def __init__(self):
        self.log    = Logs()
        self.msn    = ""
        self.tables = [
            'inventory',
            'products',
            'sales',
            'users',
            'config',
            'config_details'
        ]
    
    def executeDropTable(self,table):
        try:
            self.log.info("Iniciando DROPTABLE ")
            self.connection()
            c = self.conn.cursor()
            sql= 'DROP TABLE IF EXISTS '+table
            c.execute(sql)
            self.closeConnection()
            self.msn += table+", eliminada; "
            return True
        except Exception as e:
            self.log.error(e.args[0])
            self.msn += e.args[0]
            return False

    def dropTable(self):
        for t in self.tables:
            if t != "":
                drop = self.executeDropTable(t)
                if  drop == False:
                   break
        return  drop    