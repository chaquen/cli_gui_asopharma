
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from views.App import *
from utils.Logs import Logs
from models.Config import Config
from db.DropTables import DropTables
from db.CreateTables import CreateTables
from views.FormRegisterBranchOffice import FormRegisterBranchOffice
import tkinter.messagebox as tm
from datetime import datetime


class ConfigureWindow(tk.Frame):

    def __init__(self, parent, controller):
        print("_init_ StartPage")
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config = Config()
        self.log = Logs()
        self.loadDesing()
        
    def menuBar(self,root):
        '''Función para mostrar el menú de la página'''
        self.log.infoini("menuBar Configure")
        self.menubar = tk.Menu(root)
        ConfigureMenu = tk.Menu(self.menubar)
        ConfigureMenu.add_command(label="Ayuda (F1)",command=lambda: self.controller.showFrame("ConfigureWindow"))
        ConfigureMenu.add_command(label="SALIR (Alt + F1)",command=lambda: root.quit())        
        self.menubar.add_cascade(label="Inicio", menu=ConfigureMenu)

        return self.menubar    

    def loadDesing(self):
        '''Función para cargar diseño'''
        label = tk.Label(self, text="Ventana de configuración", font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        self.button1 = tk.Button(self, text="Ir a inicio de sesión",
                            command=lambda: self.controller.showFrame("LoginWindow"))
        self.button1.pack()
        self.button2 = tk.Button(self, text="Crear base de datos",
                            command= self.createDataBase)
        self.button2.pack()
        self.button3 = tk.Button(self, text="Eliminar base de datos",
                            command= self.deleteDataBase)
        
        
        self.button4 = tk.Button(self, text="Sincronizar equipo",
                            command= self.syncComputer)

        self.button4.pack()
        if self.config.validateClient() is not None:            
            self.button3.pack()
            self.button2['state'] = "disable"
            self.button3['state'] = "normal"
            self.button4['state'] = "normal"
        else:
            self.button2['state'] = "normal"
            self.button3['state'] = "disable"
            self.button4['state'] = "disable"

    def viewFormRegisterBranchOffice(self):
        formRegisterBranchOffice = FormRegisterBranchOffice(self)



    def createDataBase(self):
        if self.config.createDatabase() == True:
            tm.showinfo("Crear base de datos",self.config.msn)
            self.button2['state'] = "disable"
            self.button4['state'] = "normal"
        else:
            tm.showerror("Crear base de datos",self.config.msn)        

    def deleteDataBase(self):
        if self.config.deleteDatabase() == True:
            tm.showinfo("Eliminar base de datos",self.config.msn)
        else:
            tm.showerror("Eliminar base de datos",self.config.msn)
            
    def syncComputer(self):
        self.viewFormRegisterBranchOffice()

    def keyPress(self,event):
        '''Funcion para capturar eventos dpresionados en el frame'''
        self.log.infoini("key press Configure: "+event.keysym)
        if event.keysym == 'F1':
            self.controller.showFrame("ConfigureWindow")  
        else:
            pass