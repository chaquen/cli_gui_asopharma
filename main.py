#!/usr/bin/env python
# -*- coding: utf-8 -*-
from views.App import * 
from const import env


	


if __name__ == "__main__":
    '''
        SI EXISTE UN INICIO DE SESION ACTIVO
        EJECUTAR LA CLASE DE OperationWindow
    '''
    app = App(title=env.APPNAME,size=env.SIZE)
    app.mainloop()
