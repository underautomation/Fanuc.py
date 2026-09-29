from enum import IntEnum

class PositionFormat(IntEnum):
	'''Format of the positions of a trajectory'''
	Joint = 0 # Joint positions (up to 9 axes), in degrees (mm for linear axes)
	Cartesian = 1 # Cartesian positions X, Y, Z in mm with an orientation, plus up to 3 external axes
