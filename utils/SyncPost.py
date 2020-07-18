#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  utils.Logs import Logs
from utils.Sync import Sync
import requests
import json as json
import inspect

class SyncPost(Sync):
    def __init__(self):
        self.log = Logs() 

    def posthttp(self,endpoint,headers=False,payload=False):
        try:
            self.log.infoini(inspect.stack()[0][3])

            self.endpoint  = self.validateUrl(endpoint)
            
            if self.endpoint == False:
                return False
            
            response = self.sendRequest(headers,payload)
            
            #response.raise_for_status()

            #return response.json()
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
    
    def sendRequest(self,headers,payload):
        self.log.infoini(inspect.stack()[0][3])

        if headers != False and payload != False:
                self.log.info(" ENDPOINT: "+self.endpoint+" HEADERS:"+json.dumps(headers)+" PARAMS:"+json.dumps(payload))
                response = requests.post(self.endpoint,headers=headers,data=payload)
        elif headers != False and payload == False:
                self.log.info(" ENDPOINT: "+self._url+endpoint+" HEADERS:"+json.dumps(headers))
                response = requests.post(self.endpoint,headers=headers)
        elif headers == False and payload != False:
                self.log.info(" ENDPOINT: "+self.endpoint+" PARAMS:"+json.dumps(payload))
                response = requests.post(self.endpoint,data=payload)
        else:
                self.log.info(" ENDPOINT:"+self.endpoint)
                response = requests.post(self.endpoint)
        
        return response
            