#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  utils.Logs import Logs
import tkinter as tk  
from tkinter import *
from tkinter import font  as tkfont 
import tkinter.messagebox as tm
import getpass
from getmac import get_mac_address as gma
from datetime import date
from datetime import datetime

class MainWindow(tk.Tk):
    def __init__(self,title,size="300x300",*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.log = Logs()
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.window_title = title
        self.title(self.window_title)
        self.minsize(300,300)
        self.geometry(size)
        self.root = tk.Frame(self)
        self.root.pack(side="top", fill="both", expand=True)
        #self.root.grid_rowconfigure(0, weight=1)
        #self.root.grid_columnconfigure(0, weight=1)
        
class LoginWindows(MainWindow):
     
      
    def loadDesign(self):
        self.log.infoini("loadDesign")
        texto = "Bienvenido {name} a {appname} \n accediendo desde {mac}, hoy es {fecha}:\t".format(name = getpass.getuser(),appname = self.window_title,mac = gma(),fecha = str(datetime.now().day)+"/"+str(datetime.now().month)+"/"+str(datetime.now().year))
        self.mylabelmsn = Label(self.root,text=texto)
        self.mylabelmsn.grid(row=0,column=1,padx=50,pady=100)

        self.label_username = Label(self.root, text="Usuario")
        self.label_username.grid(row=1,column=1,pady=2)

        self.entry_username = Entry(self.root)
        self.entry_username.grid(row=2,column=1,padx=10,pady=10)
        
        self.label_password = Label(self.root, text="Contraseña")
        self.label_password.grid(row=3,column=1,padx=10,pady=10)       
        
        self.entry_password = Entry(self.root, show="*")
        self.entry_password.grid(row=4,column=1,padx=10,pady=10)

        self.btn_login = Button(self.root,text="Ingresar",background="#93988f",command=self.validateLogin)
        self.btn_login.grid(row=5,column=1)
        
    def validateLogin(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        print(username, password)

        if username == "john" and password == "password":
            tm.showinfo("Login info", "Welcome John")
        else:
            tm.showerror("Login error", "Incorrect username")

    
class OperationWindow(MainWindow):
    def loadDesign(self):
        pass

