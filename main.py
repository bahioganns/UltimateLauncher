import eel
from middle.mid_convert import random_python

eel.init("front")

random_python()

# Start the index.html file
eel.start('index.html', mode='default')