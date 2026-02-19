from enum import IntEnum

class DataStyle(IntEnum):
	'''Data style for motion commands'''
	Cartesian = 0 # Cartesian coordinate system (X, Y, Z, W, P, R)
	Joint = 1 # Joint coordinate system (J1-J9)
