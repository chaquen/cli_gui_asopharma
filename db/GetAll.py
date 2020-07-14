#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  db.Database import Database
from  utils.Logs import Logs

class GetAll(Database):
    
    def __init__(self):
         self.log = Logs()


    def getAll(self,sql):
        try:
            self.log.info("Iniciando consulta getAll")
            self.connection()
            c = self.executeSelectSQL(sql)
            data= c.fetchall()
            self.log.info("Consulta realizada getAll "+' '.join(map(str,data)))
            self.closeConnection()
            return data
        except Exception as e:
            self.log.error(e.args[0])
            return False