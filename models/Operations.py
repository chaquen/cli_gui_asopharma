#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.Logs import Logs
from models.Products import Products
from models.Sales import Sales
from models.Outputs import Outputs
from utils.SyncGet import SyncGet
from utils.SyncPost import SyncPost

class Operations():

    def __init__(self):
        self.venta = Sales()
        self.producto  = Products()     
        self.salidas = Outputs()
        self.syncget = SyncGet() 

    def registerSaleBranchOffice(self,typeSale,quantityaSaled,priceSaled,idUser):
        print("registerSaleBranchOffice>> ")
        if self.producto.producto_seleccionado:
            if self.venta.registerSale(typeSale,self.producto.id,quantityaSaled,priceSaled,idUser):
                self.producto.updateQuantitySaled(self.producto.id,typeSale,quantityaSaled)
                self.msn = "Venta registrada"
            else: 
                self.msn = "No se ha registrado la venta"
            return True
        else:
            self.msn = "No se a registrado la venta"
            return False
        

    def sendReportSalesToApi(self):
        '''TODO :: 
        -- Consultar ventas dia
        -- Conectar con api
        -- Enviar datos'''
        pass

    def clearRegisterSale(self):
        '''TODO :: 
        -- Limpiar registro de ventas'''
        pass

    def updateInventoryBranchOfficeFromApi(self):
        '''TODO :: 
        -- Conectar con api
        -- Traer datos de api
        -- Actualziar inventario (cantidad,precio,estado) del producto'''
        pass
    def createInventoryBranchOfficeFromApi(self):
        ''''Funcion para registrar el inventario por primera vez'''
        endpoint="/vistaemfasur"            
        headers = {'user-agent': 'my-app/0.0.1'}
        payload = {'key1': 'value1', 'key2': 'value2'}
        response = self.syncget.gethttp(endpoint,payload=payload,headers=headers)
        self.producto.insertProducts(response['datos'])

