#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.Operations import Operations
from  db.Database import Database
from db.DropTables import DropTables
from db.CreateTables import CreateTables
from models.Config import *

"""sales = Operations()
code = '7702605107407'
sales.selectProduct(code)"""
"""CONSULTAR SI BASE DE DATOS EXISTE"""
#db =  Database()
#db.connection()

#"""ELIMINAR BASE DE DATOS"""
#db = DropTables()
#db.dropTable()
#
#"""CREAR BASE DE DATOS"""
#db = CreateTables()
#db.createTablesDatabase()
#
#"""CREAR INVENTARIO"""
#op = Operations()
#op.createInventoryBranchOfficeFromApi()

"""BUSCAR PRODUCTO"""
#opprod = Operations()
#opprod.producto.selectProduct("macrogoteo")

"""BUSCAR PRODUCTOS"""
#op = Operations()
#op.producto.selectProducts("7702796811008")

"""BUSCAR TODOS LOS PRODUCTOS"""
#op = Operations()
#op.producto.selectAllProducts()

#"""VENDER PRODUCTO"""
#cod = "7702605107407"
#cantidad = 10
#tipo_venta = 'Unidad'
#usuario = 1
#precio = 10000
#op = Operations()
#
#if op.producto.selectProduct(cod):
#    op.registerSaleBranchOffice(tipo_venta,int(cantidad),precio,usuario)
#else: 
#    print("Debe seleccionar un producto, para registrar la venta")


conf = Config()
conf.validateClient()
