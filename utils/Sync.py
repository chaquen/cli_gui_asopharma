#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  utils.Logs import Logs
from const import constant
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
    _url = constant.URL
    def __init__(self):
        self.log = Logs() 
        
    def validateUrl(self,endpoint):
        self.log.infoini(inspect.stack()[0][3])

        if len(endpoint) == 0 :
            return  False
        else:
            return self._url+endpoint