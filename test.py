#from  db.Database import Database
from  db.GetAll import GetAll
from  db.GetOne import GetOne
#from  db.Insert import Insert
#from  db.Update import Update
#from  db.Delete import Delete



#db = Database()
getall = GetAll()
getone = GetOne()
#insert = Insert()
#update = Update()
#delete = Delete()

#db.dropTable()
#db.createTable()
#insert.insert('stocks',"'2020-07-13','BUY','555',100,35.14")
getall.getAll('SELECT * FROM stocks')
t = ('55',)
d=getone.getOne('SELECT * FROM stocks WHERE symbol_text=?', t)
#print(d)
#data = ('55','2020-06-05')
#update.update('stocks','symbol_text = ?','date_text = ?',data)
#t = ('555',)
#delete.delete('stocks','symbol_text = ?',t)

#from models.Inventory import Inventory

#inventory = Inventory()
#inventory.getAll()