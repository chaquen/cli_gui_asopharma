#!/usr/bin/env python
# -*- coding: utf-8 -*-
from views.MainWindow import * 
from const import env

if __name__ == "__main__":
    '''
        SI EXISTE UN INICIO DE SESION ACTIVO
        EJECUTAR LA CLASE DE OperationWindow
    '''
    app = LoginWindows(title=env.APPNAME,size=env.SIZE)
    app.loadDesign()
    app.mainloop()
