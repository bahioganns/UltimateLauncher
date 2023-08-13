import eel
from back.Controllers.controller import Controller, Session, engine, Base, Dbfile
# from back.methods import get_files_list
# from middle.mid_methods import get_files_json

eel.init("front")

cont1 = Controller("C:\\Users\\bahio\\Downloads\\temp.txt")
cont1.add_to_db()
cont2 = Controller("C:\\Users\\bahio\\Downloads\\temp1.txt")
cont2.add_to_db()

# Start the index.html file
eel.start('index.html', mode='default')