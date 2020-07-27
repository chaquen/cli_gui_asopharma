#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk                
from tkinter import font  as tkfont 
from views.LoginWindow import * 
from views.HelpWindow import * 
from views.OperationWindow import * 
from utils.Logs import Logs


class App(tk.Tk):

    def __init__(self,title,size, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.log = Logs()
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry(size)
        
        self.title(title)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        #container.grid_rowconfigure(0, weight=1)
        #container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginWindow, OperationWindow, HelpWindow):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")       

        self.showFrame("LoginWindow")
     
    
    def showFrame(self, page_name):
        '''Show a frame for the given page name'''
        self.log.infoini("show_frame "+page_name)
        frame = self.frames[page_name]
        frame.tkraise()
        menubar = frame.menuBar(self)
        self.configure(menu=menubar)
        frame.bind_all('<Key>',frame.keyPress)
    
    
    
        

