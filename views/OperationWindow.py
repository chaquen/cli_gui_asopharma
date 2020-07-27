
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from views.App import *
from utils.Logs import Logs


class OperationWindow(tk.Frame):

    def __init__(self, parent, controller):
        print("_init_ StartPage")
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.log = Logs()
        self.loadDesign()
        
    
    def menuBar(self,root):
        self.log.infoini("menuBar Operation")
        '''Función para mostrar el menú de la página'''
        self.menubar = tk.Menu(root)
        operationMenu = tk.Menu(self.menubar)
        operationMenu.add_command(label="Ayuda (F1)",command=lambda: self.controller.showFrame("HelpWindow"))
        operationMenu.add_command(label="SALIR (Alt + F4)",command=lambda: root.quit())        
        self.menubar.add_cascade(label="Inicio", menu=operationMenu)
        salesMenu = tk.Menu(self.menubar)
        salesMenu.add_command(label="Vender (F2)")
        salesMenu.add_command(label="BUscar (F3)")       
        self.menubar.add_cascade(label="Operaciones", menu=salesMenu)
        return self.menubar

    def loadDesign(self):
        label = tk.Label(self, text="Escriba el código o nombre del producto", font=self.controller.title_font)
        #label.pack(side="top", fill="x")
        label.grid(row=0,column=3)
        btnSearch = tk.Button(self, text="Buscar",
                            command= self.buscar)
        btnSearch.grid(row=1,column=4)

        searchProduct = tk.Entry(self,width=40)
        searchProduct.grid(row=1,column=3)
        
        
        
    def buscar(self):
        producto = self.searchProduct.get()
        print("Producto a buscar :: "+producto)

    def keyPress(self,event):
        self.log.infoini("key press operation: "+event.keysym)
        if event.keysym == 'F1':
            self.controller.showFrame("HelpWindow")  
        elif event.keysym == 'F2':
            tm.showinfo("Operation","jhh")