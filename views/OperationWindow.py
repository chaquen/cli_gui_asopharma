
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from views.App import *
from utils.Logs import Logs
from models.Products import Products
from models.Sales import Sales
from models.Operations import Operations
import tkinter.messagebox as tm

class OperationWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.log = Logs()
        #self.producto = Products()
        self.operaciones = Operations()
        #self.productSelect = True
        #self.ventas = Sales()
        self.controller = controller
        self.loadDesign()
            
    def menuBar(self,root):
        '''Función para mostrar el menú de la página'''
        self.log.infoini("menuBar Operation")
        self.menubar = tk.Menu(root)
        operationMenu = tk.Menu(self.menubar)
        operationMenu.add_command(label="Ayuda (F1)",command=lambda: self.controller.showFrame("HelpWindow"))
        operationMenu.add_command(label="SALIR (Alt + F4)",command=lambda: root.quit())        
        self.menubar.add_cascade(label="Inicio", menu=operationMenu)
        salesMenu = tk.Menu(self.menubar)
        salesMenu.add_command(label="Buscar (F2)")
        salesMenu.add_command(label="Vender Unidad (F3)")       
        salesMenu.add_command(label="Vender Blister (F4)")    
        salesMenu.add_command(label="Vender Caja (F5)")    
        self.menubar.add_cascade(label="Operaciones", menu=salesMenu)
        return self.menubar

    def loadDesign(self):
        '''Funcion para acrgar el diseño de este Frame'''
        label = tk.Label(self, text="Escriba el código o nombre del producto", font=self.controller.title_font)
        label.grid(row=0,column=3)
        
        self.searchProduct = tk.Entry(self,width=40)
        self.searchProduct.grid(row=1,column=3)

        btnSearch = tk.Button(self, text="Buscar",
                            command = self.search)
        btnSearch.grid(row=1,column=4)
        self.labelMsn = tk.Label(self, text="", font=self.controller.title_font)
        self.labelMsn.grid(row=2,column=5)
        
    def search(self):
        '''Funcion para buscar los productos'''
        self.log.infoini("search")
        productSearched = self.searchProduct.get()
        pr = self.operaciones.producto.selectProduct(productSearched)
        if pr == False:
            self.labelMsn['text'] = self.operaciones.producto.msn
        else: 
            self.labelMsn['text'] = ""
            self.searchProduct.delete(0, 'end')
            self.viewInfoProduct(pr)            
        return pr

    def viewInfoProduct(self,pr):
        '''Aqui va la función para mostrar la información del producto encontrado'''
        self.log.infoini("viewInfoProduct")
        lblCodeProduct = tk.Label(self,text=self.operaciones.producto.codigo_producto)
        lblNameProduct = tk.Label(self,text=self.operaciones.producto.nombre_producto)
        lblTypeProduct = tk.Label(self,text=self.operaciones.producto.tipo_venta_producto)
        self.lblPriceProduct = tk.Label(self,text=self.operaciones.producto.precio_mayoreo_sede)
        validation = self.register(self.onlyNumbers)
        self.entQuantity = tk.Entry(self,validate="key",validatecommand=(validation, '%S'))
        self.entQuantity.focus()
        btnSale = tk.Button(self,text="Vender",command = lambda : self.salesProduct(self.operaciones.producto.tipo_venta_producto,self.entQuantity.get(),self.operaciones.producto.precio_mayoreo_sede,1))
        lblCodeProduct.grid(row=3,column=0,padx=30,pady=50)
        lblNameProduct.grid(row=3,column=1,padx=30,pady=50)
        lblTypeProduct.grid(row=3,column=2,padx=30,pady=50)
        self.lblPriceProduct.grid(row=3,column=3,padx=30,pady=50)
        self.entQuantity.grid(row=3,column=4,padx=30,pady=50)
        btnSale.grid(row=3,column=5,padx=30,pady=50)

        '''scrollbar = tk.Scrollbar(self)
        scrollbar.grid(row=6,column=0)
        mylist = tk.Listbox(self, yscrollcommand = scrollbar.set,width=400 )
        
        for line in range(1000):
            mylist.insert(line, "This || is line || number " + str(line)+" || ")
            mylist.grid(row=6,column=0)

        scrollbar.config( command = mylist.yview )'''

        
    def salesProduct(self,tipo,cantidad,precio,usr):
        '''aqui debo validar si el tipo enviado es valido para el producto, en caso contrario mostrar mensaje al usuario'''
        self.log.infoini("salesProduct "+tipo)
        print(self.operaciones.producto.producto_seleccionado)
        if tipo != "":
            if self.operaciones.producto.producto_seleccionado == True:
               if self.operaciones.registerSaleBranchOffice(tipo,int(cantidad),precio,usr) == True:
                   tm.showinfo("Operaciones",self.operaciones.msn)
               else:
                   tm.showerror("Error Operaciones",self.operaciones.msn)
            else: 
                print("Debe seleccionar un producto, para registrar la venta")
                self.clearControls()
        else:
            tm.showerror("Error Operaciones","Debes seleccionar un tipo de venta permitido para el producto "
                        +self.producto.msn)
    
    def validateTypeSale(self,tipo,producto):
        '''Funcion para validar el tipo de venta permitido para el producto'''
        return True

    def updateInventory(self):
        '''aqui va la funcion para  modificar las existencias'''
        pass

    def clearControls(self):
        '''aqui va la funcion para limpiar los textos '''
        self.entQuantity.delete(0, 'end')
        self.productSelect = False
    
    def viewSalesHistory(self):
        '''Funcion para registrar el historico de ventas del dia'''
        pass
    
    def keyPress(self,event):
        '''Aqui va la funcion para leer las teclas presionadas y agregar los eventos relacionados'''
        self.log.infoini("key press operation: "+event.keysym)
        if event.keysym == 'F1':
            self.controller.showFrame("HelpWindow")  
        elif (event.keysym == 'Return' or event.keysym == 'KP_Enter' or event.keysym == 'F2') and self.searchProduct.get() != "" and self.operaciones.producto.producto_seleccionado:
            '''aqui se debe validar si el enter presionado tiene una cantidad y un producto seleccionado para maracr una venta'''
            if self.productSelect:
                self.salesProduct(self.producto.tipo_venta_producto)
            else:
                self.search()
        elif event.keysym == 'F3':
            self.salesProduct('Unidad',self.entQuantity.get(),self.operaciones.producto.precio_mayoreo_sede,1)
        elif event.keysym == 'F4':
            self.salesProduct('Blister',self.entQuantity.get(),self.operaciones.producto.precio_venta_blister_sede,1)
        elif event.keysym == 'F5':
            self.salesProduct('Caja',self.entQuantity.get(),self.operaciones.producto.precio_venta_sede,1)

    def onlyNumbers(self,char):
        '''Funcion para valdiar si el digito ingresado es numero'''
        return char.isdigit()