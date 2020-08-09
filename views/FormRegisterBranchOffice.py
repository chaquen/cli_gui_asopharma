#!/usr/bin/env python
# -*- coding: utf-8 
import tkinter as tk    
from utils.SyncGet import SyncGet
from models.Config import Config
import tkinter.messagebox as tm

class FormRegisterBranchOffice():

    def __init__(self,root):
     self.conf = Config()
     self.registerForm = tk.Toplevel(root)   
     self.registerForm.title("Registrar sede")     
     self.registerForm.geometry("400x400")     
     tk.Label(self.registerForm,  
         text ="Selecciona la sede que estara asociada a este equipo").pack() 
     data = self.getBranchesOffice()
     self.id_sede = tk.IntVar()
     for d in data:
          tk.Radiobutton(self.registerForm,text=str(d['nombre_sede']),variable=self.id_sede,value=int(d['id'])).pack()
     
     tk.Button(self.registerForm,text = "Registrar sede",command = self.RegisterBranchOffice).pack()
        
    

    def RegisterBranchOffice(self):
         if self.conf.registerClient(self.id_sede.get()):
              tm.showinfo("OK",self.conf.msn)
         else:
              tm.showerror("ERROR",self.conf.msn) 
              
         
     
    def getBranchesOffice(self):
        endpoint="/sedes"            
        headers = {'user-agent': 'my-app/0.0.1'}
        payload = {'key1': 'value1', 'key2': 'value2'}
        syncget = SyncGet() 
        response = syncget.gethttp(endpoint,payload=payload,headers=headers)
        return response['datos']