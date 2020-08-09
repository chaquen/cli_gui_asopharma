
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from views.App import *
from utils.Logs import Logs

class HelpWindow(tk.Frame):

    def __init__(self, parent, controller):
        print("_init_ StartPage")
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.log = Logs()
        self.loadDesing()
        
    def menuBar(self,root):
        '''Función para mostrar el menú de la página'''
        self.log.infoini("menuBar Help")
        self.menubar = tk.Menu(root)
        helpMenu = tk.Menu(self.menubar)
        helpMenu.add_command(label="Ayuda (F1)",command=lambda: self.controller.showFrame("HelpWindow"))
        helpMenu.add_command(label="SALIR (Alt + F1)",command=lambda: root.quit())        
        self.menubar.add_cascade(label="Inicio", menu=helpMenu)

        return self.menubar    

    def loadDesing(self):
        '''Función para cargar diseño'''
        label = tk.Label(self, text="This is the HelpWindow", font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Ir a inicio de sesión",
                            command=lambda: self.controller.showFrame("LoginWindow"))
        button1.pack()

    def keyPress(self,event):
        '''Funcion para capturar eventos dpresionados en el frame'''
        self.log.infoini("key press Help: "+event.keysym)
        if event.keysym == 'F1':
            self.controller.showFrame("HelpWindow")  
        else:
            pass