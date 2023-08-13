import eel
from back.servicedb import Servicedb, Dbfile
from back.controller import get_files_json, execute_file, open_file, add_new_file

eel.init("front")

print(get_files_json())

# Start the index.html file
eel.start('index.html', mode='default')