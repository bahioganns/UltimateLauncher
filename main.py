import eel
from middle.mid_convert import random_python


from back.Controllers.controller import Controller, Session, engine, Base, Dbfile

eel.init("front")

cont = Controller("C:\\Users\\bahio\\Downloads\\temp.txt")
cont.add_to_db("C:\\Users\\bahio\\Downloads\\temp.txt")

session = Session()

files = session.query(Dbfile).all()

print("all files:")

for file in files:
    print(file.id, " ", file.path)

# Start the index.html file
#eel.start('index.html', mode='default')