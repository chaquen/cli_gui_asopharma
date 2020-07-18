#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  utils.Logs import Logs
from const import constant
from utils.Sync import Sync
import requests
import json as json
import inspect

class SyncValidate(Sync):
    def __init__(self):
        self.log = Logs()
        
    def validadeStatus(self,endpoint=" "):
        try:
            self.log.info("INICIANDO METODO  "+inspect.stack()[0][3])
            if endpoint[0] != "/":
                self.log.error(str(0)+" :: "+self._codes[0]+" endpoint: "+endpoint)
                return False
            response = requests.get(self._url)
            print(response.status_code)
            if response.status_code == 200 :            
                self.log.info(self._codes[response.status_code])
                return response
            else: 
                self.log.error(response.status_code+" :: "+self._codes[response.status_code])
                return False
        except requests.exceptions.RequestException as e:
            self.log.exception("RequestException "+inspect.stack()[0][3]+" "+e.args[0])
            return False
        except requests.exceptions.Timeout as e:
            self.log.exception("Timeout "+inspect.stack()[0][3]+" "+e.args[0])
            return False
        except requests.exceptions.TooManyRedirects as e:
            self.log.exception("TooManyRedirects "+inspect.stack()[0][3]+" "+e.args[0])
            return False
        except Exception as e:
            self.log.exception(" validadeStatus() "+e.args[0])
            return False    