from  db.Database import Database
#from  db.GetAll import GetAll
#from  db.GetOne import GetOne
from  db.Insert import Insert
#from  db.Update import Update
#from  db.Delete import Delete
from db.CreateTables import CreateTables
from utils.SyncGet import SyncGet
from utils.SyncPost import SyncPost
from utils.Logs import Logs
from models.Products import Products
import datetime
import json



#db = Database()
#getall = GetAll()
#2getone = GetOne()
#insert = Insert()
#update = Update()
#delete = Delete()

#db.dropTable()
#db.createTable()
#insert.insert('stocks',"'2020-07-13','BUY','555',100,35.14")
#getall.getAll('SELECT * FROM stocks')
#t = ('55',)
#d=getone.getOne('SELECT * FROM stocks WHERE symbol_text=?', t)
#print(d)
#data = ('55','2020-06-05')
#update.update('stocks','symbol_text = ?','date_text = ?',data)
#t = ('555',)
#delete.delete('stocks','symbol_text = ?',t)

#from models.Inventory import Inventory

#inventory = Inventory()
#inventory.getAll()



### API TEST

#log = Logs()
#log.info("INICIO")
#ini = int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
endpoint="/vistaemfasur"
sy = SyncGet()
headers = {'user-agent': 'my-app/0.0.1'}
payload = {'key1': 'value1', 'key2': 'value2'}
response = sy.gethttp(endpoint,payload=payload,headers=headers)
print(response)
print(response['datos'])
#for x in response:
#  print("KEY: "+x+str(type(response[x])))
#  if x == "datos":
#        print(response[x])
          
            #for ll in l:
             #   print("'"+ll+" ===> "+l[ll]+"'")
              #  validar(l[ll])


#log.info("FIN")
#fin = int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
#print("DIFERENCIA TIEMPO "+str(fin - ini))
#endpoint = '/reporte_inventario'
#sy = SyncPost()
#print(sy.posthttp(endpoint))

cr = CreateTables()
fic = open("create.sql", "r")
lines = []
for line in fic:
    cr.createTable(line)
sy = SyncGet()

#response = sy.gethttp(endpoint)
#insert = Insert()
#for x in response:
#  print("KEY: "+x+str(type(response[x])))
#  if x == "datos":
#      for l in response[x]:
#            for ll in l:
#                print("'"+ll+" ===> "+l[ll]+"'")
#                insert.insert('stocks',"id,codigo_producto,codigo_distribuidor,nombre_producto,tipo_venta_producto,tipo_presentacion,cantidad_existencias,cantidad_existencias_blister,cantidad_existencias_unidades")


prd = Products()
#prd.insertProduct(response['datos'])
p = prd.selectProduct("codigo_producto",value="7707228367085")
print(p)
print(prd.codigo_distribuidor)
print(prd.selectAllProducts())