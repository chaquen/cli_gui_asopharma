#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  utils.Logs  import Logs
from  db.Insert   import Insert
from  db.GetAll   import GetAll
from  db.GetOne   import GetOne
from  collections import defaultdict
import datetime
class Sales():
    

    def __init__(self):
        self.log = Logs()
        self.table = 'sales'
        self.dateSale = datetime.datetime.now()
        self.fields = [
            'fk_id_producto',
            'tipo_venta',
            'cantidad_vendida',
            'fecha_venta',
            'precio_venta',
            'cajero'
        ]
       
    def registerSale(self,typeSale,idProducto,quantity,priceSaled,idUser):
        fieldsstr = ",".join(self.fields)                
        self.log.info("Iniciando registerSale "+self.table+" ("+fieldsstr+") " )
        ins = Insert()        
        data_list=[]
        data_list.append([idProducto,typeSale,quantity,self.dateSale,priceSaled,idUser])
        print(type(data_list))
        values = '?,'*len(self.fields)
        values = values[:-1]
        self.log.infoini("SENTENCIA  INSERT "+self.table+" ("+fieldsstr+") "+values )
        return ins.insertMany(self.table,fieldsstr,values,data_list)
        
    def findSale(self):
        pass


    
