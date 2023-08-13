import eel
from back.servicedb import Servicedb, Dbfile
from back.controller import get_files_json

eel.init("front")

dbf0 = Dbfile("C:\\Users\\bahio\\Downloads\\temp.txt")
cont1 = Servicedb()
cont1.add_to_db(dbf0)
dbf1 = Dbfile("C:\\Users\\bahio\\Downloads\\temp1.txt")
cont1.add_to_db(dbf1)

print(get_files_json())

# Start the index.html file
eel.start('index.html', mode='default')