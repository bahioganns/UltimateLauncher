import eel
from back.servicedbfile import ServiceDbFile, DbFile
from back.servicedbicon import ServiceDbIcon
from back.controller import del_file
import os

# !!!!!!!!!!!!!!!!! We are deleting database every time
# !!!!!!!!!!!!!!!!! It will be removed when icons will store there forever
os.remove("memory")

eel.init("front")
# quick testing zone
serv = ServiceDbFile()
icon_serv = ServiceDbIcon()

# remove all elements
serv.remove_all()
icon_serv.remove_all()
print(serv.del_from_db(1))

# add elements
serv.add_to_db(DbFile("exemple\\path\\name"))
serv.add_to_db(DbFile("exemple\\path\\name1"))
serv.add_to_db(DbFile("exemple\\path\\name2"))
# check if there are right amount of elements with right names
assert serv.get_amount() == 3

# check if deletion by id is working
print(serv.del_from_db(1))
assert serv.get_amount() == 2

# check if deletion by id is working
print(del_file(2))
assert serv.get_amount() == 1

# check if deletion by id is working
serv.remove_all()
assert serv.get_amount() == 0
#end of testing zone

# Start the index.html file
eel.start('index.html', mode='chrome')