import datetime

class Logs:
    def __init__(self):
        self.time = datetime.datetime.now()

    def error(self,msn):
        print("ERROR: "+str(self.time)+" : "+msn)

    def info(self,msn):
        print("INFO: "+str(self.time)+" : "+msn)
        
    def infoini(self,msn):
        print("INFO: INICIANDO METODO  "+str(self.time)+" : "+msn)

    def exception(self,msn):
        print("EXCEPTION: "+str(self.time)+" : "+msn)