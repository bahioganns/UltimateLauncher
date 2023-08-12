from back.convert import get_random_number
import eel

@eel.expose	
def random_python():
	return get_random_number()