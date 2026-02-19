from enum import IntEnum

class Languages(IntEnum):
	'''Languages supported by the Fanuc robots'''
	English = 0 # For robots set to English language
	Japanese = 1 # For robots set to Japanese language
	Chinese = 2 # For robots set to Chinese language
