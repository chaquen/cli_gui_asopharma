#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  utils.Logs import Logs
from  db.Insert import Insert
from  db.GetAll import GetAll
from  db.GetOne import GetOne
from collections import defaultdict
from db.Update import Update
class Products():
    
    table = "products"
    fields = [  
              'id',
              'codigo_producto',
              'codigo_distribuidor',
              'nombre_producto',
              'tipo_venta_producto',
              'tipo_presentacion',
              'unidades_por_caja',
              'unidades_por_blister',
              'precio_venta_sede',
              'precio_venta_blister_sede',
              'precio_mayoreo_sede',
              'cantidad_existencias_caja',
              'cantidad_existencias_blister',
              'cantidad_existencias_unidades',
              'cantidad_existencias_totales',
              'minimo_inventario_sede',
              'categoria',
              'proveedor']

    def __init__(self):
        self.log                           = Logs()
        self.id                            = ""
        self.codigo_producto               = ""
        self.codigo_distribuidor           = ""
        self.nombre_producto               = ""
        self.tipo_venta_producto           = ""
        self.tipo_presentacion             = ""
        self.unidades_por_caja             = ""
        self.unidades_por_blister          = ""
        self.precio_venta_sede             = ""
        self.precio_venta_blister_sede     = ""
        self.precio_mayoreo_sede           = ""
        self.cantidad_existencias_caja     = ""
        self.cantidad_existencias_blister  = ""
        self.cantidad_existencias_unidades = ""
        self.cantidad_existencias_totales = ""
        self.minimo_inventario_sede        = ""
        self.categoria                     = ""
        self.proveedor                     = ""
        self.producto_seleccionado         = False
        self.msn                           = ""
         #PorUnidad = unidad
        #Caja = caja/unidad
        #CajaBlister = caja/unidad/blister 
        self.UNIDAD  = "Unidad"
        self.BLISTER = "Blister"
        self.CAJA    = "Caja"

    def insertProducts(self,data):
        
        ins = Insert()
        fieldsstr = ",".join(self.fields)        
        
        data_list=[]
        for d in data:
            data_list.append([*d.values()])
        print(type(data_list))
        values = '?,'*len(self.fields)
        values = values[:-1]
        self.log.infoini(" INSERT "+self.table+" ("+','.join(self.fields)+") "+values )
        ins.insertMany(self.table,fieldsstr,values,data_list)
    
    def selectProduct(self,value):

        go        = GetOne()
        fieldsstr = ",".join(self.fields)
        sql       = "SELECT "+fieldsstr+" FROM "+self.table+" WHERE codigo_producto = ? OR  codigo_distribuidor = ? OR nombre_producto = ?"
        data      = go.getOne(sql,(value,value,value,))
        print(data)
        if data != False:
            self.id                             = data[0]
            self.codigo_producto                = data[1]
            self.codigo_distribuidor            = data[2]
            self.nombre_producto                = data[3]
            self.tipo_venta_producto            = data[4]
            self.tipo_presentacion              = data[5]
            self.unidades_por_caja              = int(data[6])
            self.unidades_por_blister           = int(data[7])
            self.precio_venta_sede              = float(data[8])
            self.precio_venta_blister_sede      = float(data[9])
            self.precio_mayoreo_sede            = float(data[10])
            self.cantidad_existencias_caja      = int(data[11])
            self.cantidad_existencias_blister   = int(data[12])
            self.cantidad_existencias_unidades  = int(data[13])
            self.cantidad_existencias_totales  = int(data[14])
            self.minimo_inventario_sede         = int(data[15])
            self.categoria                      = data[16]
            self.proveedor                      = data[17] 
            self.producto_seleccionado          = True
            self.msn                            = "Producto encontrado"

            return True
        else:
            self.producto_seleccionado = False
            self.msn                   = "Producto no encontrado"

            return False

        return data
    def selectProducts(self,value):
        ga = GetAll()
        fieldsstr = ",".join(self.fields)
        sql = "SELECT "+fieldsstr+" FROM "+self.table+" WHERE codigo_producto = ? OR  codigo_distribuidor = ? OR nombre_producto LIKE ? "
        ga.getAll(sql,data=(value,value,value,))
        data_dict = defaultdict(dict)
        for d in data_dict:
            i = len(data_dict) 
            data_dict[i][self.fields[0]]  = d[0]
            data_dict[i][self.fields[1]]  = d[1]
            data_dict[i][self.fields[2]]  = d[2]
            data_dict[i][self.fields[3]]  = d[3]
            data_dict[i][self.fields[4]]  = d[4]
            data_dict[i][self.fields[5]]  = d[5]
            data_dict[i][self.fields[6]]  = d[6]
            data_dict[i][self.fields[7]]  = d[7]
            data_dict[i][self.fields[8]]  = d[8]
            data_dict[i][self.fields[9]]  = d[9]
            data_dict[i][self.fields[10]] = d[10]
            data_dict[i][self.fields[11]] = d[11]
            data_dict[i][self.fields[12]] = d[12]
            data_dict[i][self.fields[13]] = d[13]
            data_dict[i][self.fields[14]] = d[14]
            data_dict[i][self.fields[15]] = d[15]
            data_dict[i][self.fields[16]] = d[16]
            
            
        self.msn = "Productos encontrados"

        return data_dict

    def selectAllProducts(self):
        ga = GetAll()
        data = ga.getAll("SELECT * FROM "+self.table,False)
        data_dict = defaultdict(dict)
        
        for d in data_dict:
            i = len(data_dict) 
            data_dict[i][self.fields[0]]  = d[0]
            data_dict[i][self.fields[1]]  = d[1]
            data_dict[i][self.fields[2]]  = d[2]
            data_dict[i][self.fields[3]]  = d[3]
            data_dict[i][self.fields[4]]  = d[4]
            data_dict[i][self.fields[5]]  = d[5]
            data_dict[i][self.fields[6]]  = d[6]
            data_dict[i][self.fields[7]]  = d[7]
            data_dict[i][self.fields[8]]  = d[8]
            data_dict[i][self.fields[9]]  = d[9]
            data_dict[i][self.fields[10]] = d[10]
            data_dict[i][self.fields[11]] = d[11]
            data_dict[i][self.fields[12]] = d[12]
            data_dict[i][self.fields[13]] = d[13]
            data_dict[i][self.fields[14]] = d[14]
            data_dict[i][self.fields[15]] = d[15]
            data_dict[i][self.fields[16]] = d[16]
            
        self.msn = "Productos encontrados"

        return data_dict

    def updateQuantitySaled(self,idProduct,typeProductSaled,quantitySaled):
        
        update = Update()
        if typeProductSaled == self.UNIDAD:             
            #data          = (quantitySaled,quantitySaled,quantitySaled,idProduct)
            data = self.calcQuanty(int(quantitySaled))
        elif typeProductSaled == self.BLISTER:
            data = self.calcQuanty(int(quantitySaled)*self.unidades_por_blister)            
        elif typeProductSaled == self.CAJA:
            data = self.calcQuanty((int(quantitySaled)*self.unidades_por_blister)*self.unidades_por_caja)            
        else: 
            self.msn = "Debe seleccioanr un tipo de venta permitido"
            return False

        return update.update(self.table,setupdate = 'cantidad_existencias_unidades = ?, cantidad_existencias_blister = ?, cantidad_existencias_unidades = ?, cantidad_existencias_totales= ? ' , where = 'id = ?',data = data)


    def calcQuanty(self,quantitySaled):        
        #1000 // 25 = 40 tengo 1000 unidades las divido por las unidades por blister25
        #40 // 2  = 20 eso me da los blister ahora los divido en unidades por caja
        #20 // es me da las cajas 
       
        self.cantidad_existencias_totales  = int(self.cantidad_existencias_totales) -  int(quantitySaled)
        cantidad_de_blister                = self.cantidad_existencias_totales // self.unidades_por_blister
        cantidad_de_cajas                  = cantidad_de_blister // self.unidades_por_caja
        self.cantidad_existencias_blister  = cantidad_de_blister % self.unidades_por_caja
        self.cantidad_existencias_caja     = self.cantidad_existencias_unidades % self.unidades_por_blister
        return (quantitySaled,self.cantidad_existencias_blister,self.cantidad_existencias_caja,self.cantidad_existencias_totales,self.id)
        #para determinar la cantidad de unidade de nuevo 
        # es numero de cajas * numero de unidades por caja + (blister sobrante * unidades por blister) + unidades sueltas
    
    def updateInventoryBranchOffice(self,idProduct,Quantity,State,Price):
        pass
    

