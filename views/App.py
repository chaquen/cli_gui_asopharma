#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk                
from tkinter import font  as tkfont 
from views.LoginWindow import * 
from views.HelpWindow import * 
from views.ConfigureWIndow import * 
from views.OperationWindow import * 
from utils.Logs import Logs
from models.Config import Config

class App(tk.Tk):

    def __init__(self,title,size="1200x1200", *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.log = Logs()
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        #self.geometry(str(self.winfo_screenmmwidth()*6)+"x"+str(self.winfo_screenmmheight()*2))
        self.geometry(size)
        self.title(title)
        conf = Config()        
        if conf.validateClient() is None:
            self.firstWindow = "ConfigureWindow"
        else:
            self.firstWindow = "LoginWindow"  

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.windows = (LoginWindow, OperationWindow, HelpWindow, ConfigureWindow)
       
        self.frames = {}
        for F in self.windows:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")       

        self.showFrame(self.firstWindow)
     
    
    def showFrame(self, page_name):
        '''Mostrar el frame seleccionado'''
        self.log.infoini("show_frame "+page_name)
        frame = self.frames[page_name]
        frame.tkraise()
        menubar = frame.menuBar(self)
        self.configure(menu=menubar)
        frame.bind_all('<Key>',frame.keyPress)
    
    
    
        

