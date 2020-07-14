#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  db.GetAll import GetAll
from  db.GetOne import GetOne
from  db.Insert import Insert
from  db.Update import Update
from  db.Delete import Delete
from  utils.Logs import Logs

class Inventory():

    def __init__(self):
        self.getall =GetAll()

    def getAll(self): 
        sql = 'SELECT * FROM stocks'
        self.getall.getAll(sql)

