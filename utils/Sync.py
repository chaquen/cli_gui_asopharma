#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  utils.Logs import Logs
import requests
import json as json
import inspect
class Sync():
    _codes =  {
        200 : 'Connect ok',
        204 : 'No Content',
        301 : 'Moved Permanently',
        400 : 'Bad Request',
        401 : 'Unauthorized',
        403 : 'Forbidden',
        404 : 'Not Found',
        500 : 'Internal Server Error',
        0   : 'Type corrrect endpoint fail "/"'

    }
    _url = 'https://api.asopharma.com'
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
    
    def gethttp(self,endpoint=" ",headers=False,payload=False):
        try:
            self.log.info("INICIANDO METODO  "+inspect.stack()[0][3])
            if endpoint[0] != "/":
                self.log.error(str(0)+" :: "+self._codes[0]+" endpoint: "+endpoint)
                return False
            
            if headers != False and payload != False:
                self.log.info(" ENDPOINT: "+self._url+endpoint+" HEADERS:"+json.dumps(headers)+" PARAMS:"+json.dumps(payload))
                response = requests.get(self._url+endpoint,headers=headers,params=payload)
            elif headers != False and payload == False:
                self.log.info(" ENDPOINT: "+self._url+endpoint+" HEADERS:"+json.dumps(headers))
                response = requests.get(self._url+endpoint,headers=headers)
            elif headers == False and payload != False:
                self.log.info(" ENDPOINT: "+self._url+endpoint+" PARAMS:"+json.dumps(payload))
                response = requests.get(self._url+endpoint,params=payload)
            else:
                self.log.info(" ENDPOINT:"+self._url+endpoint)
                response = requests.get(self._url+endpoint)
            response.raise_for_status()
            return response.json()
            """if response.status_code == requests.codes.ok :            
                self.log.info(str(response.status_code)+" :: "+self._codes[response.status_code]+" :: "+inspect.stack()[0][3])
                return response.json()
            else: 
                self.log.error(str(response.status_code)+" :: "+self._codes[response.status_code]+" :: "+inspect.stack()[0][3]+" :: "+response.url)
                return False"""
        except requests.exceptions.HTTPError as e:
            self.log.exception("HTTPError "+inspect.stack()[0][3]+" "+str(e.args[0]))
            return False
        except requests.exceptions.Timeout as e:
            self.log.exception("Timeout "+inspect.stack()[0][3]+" "+str(e.args[0]))
            return False
        except requests.exceptions.TooManyRedirects as e:
            self.log.exception("TooManyRedirects "+inspect.stack()[0][3]+" "+e.args[0])
            return False
        except Exception as e:
            self.log.exception(" Exception "+inspect.stack()[0][3]+" "+e.args[0])
            return False
            
    def posthttp(self):
        pass
    def puthttp(self):
        pass
    def headhttp(self):
        pass
    def optionshttp(self):
        pass
    __name__
