#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  utils.Logs import Logs
from  db.Insert import Insert
from  db.GetAll import GetAll
from  db.GetOne import GetOne
from collections import defaultdict
class Products():
    
    table = "products"
    fields = ['codigo_producto',
              'codigo_distribuidor',
              'nombre_producto',
              'tipo_venta_producto',
              'tipo_presentacion',
              'cantidad_existencias',
              'cantidad_existencias_blister',
              'cantidad_existencias_caja']

    def __init__(self):
        self.log = Logs()
        self.codigo_producto = ""
        self.codigo_distribuidor = ""
        self.nombre_producto = ""
        self.tipo_venta_producto = ""
        self.tipo_presentacion = ""
        self.cantidad_existencias = 0
        self.cantidad_existencias_blister = 0
        self.cantidad_existencias_caja = 0

    def insertProducts(self,data):
        
        ins = Insert()
        fieldsstr = ",".join(self.fields)
        #self.log.infoini(" INSERT "+self.table+" ("+fields+") "+values )
        print(data[0][self.fields[0]])
        data_list=[]
        for d in data:
        #    print(d.values())
            data_list.append([*d.values()])
        print(type(data_list))
        values = '?,'*len(self.fields)
        values = values[:-1]
        ins.insertMany(self.table,fieldsstr,values,data_list)
    
    def selectProduct(self,field,value):
        go = GetOne()
        fieldsstr = ",".join(self.fields)
        data = go.getOne("SELECT "+fieldsstr+" FROM "+self.table+" WHERE "+field+" = ? ",(value,))

        self.codigo_producto = data[0]
        self.codigo_distribuidor = data[1]
        self.nombre_producto = data[2]
        self.tipo_venta_producto = data[3]
        self.tipo_presentacion = data[4]
        self.cantidad_existencias = data[5]
        self.cantidad_existencias_blister = data[6]
        self.cantidad_existencias_caja = data[7]

        return data

    def selectAllProducts(self):
        ga = GetAll()
        data = ga.getAll("SELECT * FROM "+self.table)
        data_dict = defaultdict(dict)
        print(len(data_dict))
        
        for d in data:
            i = len(data_dict) 
            data_dict[i][self.fields[0]] = d[0]
            data_dict[i][self.fields[1]] = d[1]
            data_dict[i][self.fields[2]] = d[2]
            data_dict[i][self.fields[3]] = d[3]
            data_dict[i][self.fields[4]] = d[4]
            data_dict[i][self.fields[5]] = d[5]
            data_dict[i][self.fields[6]] = d[6]
            data_dict[i][self.fields[7]] = d[7]
            

        return data_dict
        