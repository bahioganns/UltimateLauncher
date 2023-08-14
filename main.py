import eel
from back.servicedb import Servicedb, Dbfile
from back.controller import get_files_json, open_file, add_new_file, del_file

eel.init("front")
serv = Servicedb()

# remove all elements
serv.remove_all()

# add elements
serv.add_to_db(Dbfile("exemple\\path\\name"))
serv.add_to_db(Dbfile("exemple\\path\\name1"))
serv.add_to_db(Dbfile("exemple\\path\\name2"))
# check if there are right amount of elements with right names
assert serv.get_amount() == 3

# check if deletion by id is working
serv.del_from_db(1)
assert serv.get_amount() == 2

# check if deletion by id is working
del_file(2)
assert serv.get_amount() == 1

# check if deletion by id is working
serv.remove_all()
assert serv.get_amount() == 0

add_new_file()

# serv.add_to_db(Dbfile("E:\\discord_backup_codes.txt"))
# open_file(1)

#print empty
print(get_files_json())

# Start the index.html file
eel.start('index.html', mode='default')