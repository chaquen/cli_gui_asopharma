#!/usr/bin/env python
# -*- coding: utf-8 -*-
from views.App import *
from models.Users import Users
from datetime import datetime
import getpass
from const import env
from utils.Logs import Logs
import tkinter.messagebox as tm

class LoginWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.log = Logs()
        self.user = Users()
        self.controller = controller
        self.msnWelcome()
        self.loadDesign()
        
    def loadDesign(self):
        '''Función para cargar el formulario de login'''
        self.labelUser = tk.Label(self,text="Usuario")
        self.labelUser.grid(row=6,column=5,pady=10,padx=250)
        self.entryUser = tk.Entry(self)
        self.entryUser.grid(row=7,column=5,pady=10,padx=250)
        self.labelUser = tk.Label(self,text="Contraseña")
        self.labelUser.grid(row=8,column=5,pady=10,padx=250)
        self.entryPass = tk.Entry(self,show="*")
        self.entryPass.grid(row=9,column=5,pady=10,padx=250)
        
        loginBotton = tk.Button(self,text="Ingresar",
                            background="#93988F",
                            command= self.loginWin
                            )
        loginBotton.grid(row=10,column=5,pady=10,padx=250)
        
    def msnWelcome(self):
        '''Función para mostrar el mensaje de la página'''
        texto = "Bienvenido {name} a {appname} .\n Hoy es {fecha}:\t".format(
                name = getpass.getuser(),appname = env.APPNAME,
                fecha = str(datetime.now().day)+"/"+str(datetime.now().month)+"/"+str(datetime.now().year))
        self.labelTitle = tk.Label(self, text=texto)
        self.labelTitle.grid(row=5,column=10,pady=10,padx=100)

    def menuBar(self,root):
        '''Función para mostrar el menú de la página'''
        self.log.infoini("menuBar login")
        self.menubar = tk.Menu(root)
        loginMenu = tk.Menu(self.menubar)
        loginMenu.add_command(label="Ayuda (F1)",command=lambda: self.controller.showFrame("HelpWindow"))
        loginMenu.add_command(label="Config (F12)",command=lambda: self.controller.showFrame("ConfigureWindow"))
        loginMenu.add_command(label="SALIR (Alt + F4)",command=lambda: root.quit())        
        self.menubar.add_cascade(label="Inicio", menu=loginMenu)

        return self.menubar

    def loginWin(self):
        '''Función para la logica de la página'''
        self.log.infoini("loginwin")
        user = self.entryUser.get()
        password = self.entryPass.get()
        
        if user == "":
           tm.showerror("Login Error","Debes ingresar un usuario")
           return False
        elif password == "": 
            tm.showerror("Login Error","Debes ingresar una contraseña")
            return False
        validated = self.user.login(user,password)
        if validated:
            tm.showinfo("Login Info",self.user.msn)
            self.log.infoini("login: "+user+"::"+password)
            self.controller.showFrame("OperationWindow")
        else:
            tm.showerror("Login Error",self.user.msn)          

    def keyPress(self,event):
        self.log.infoini("key press Login: "+event.keysym)
        if event.keysym == 'F1':
            self.controller.showFrame("HelpWindow")  
        elif event.keysym == 'F12':
            self.controller.showFrame("ConfigureWindow")  
        else:
            pass
