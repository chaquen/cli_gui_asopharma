#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  utils.Logs import Logs

class Users():
    def __init__(self):
        self.msn = ""
        self.log = Logs()
        

    def login(self,username,password):
        self.log.infoini("LOGIN :"+username+"::"+password)
        self.msn = "IMPLEMENTE LA FUNCIONALIDAD MY DOGGIE"
        return True