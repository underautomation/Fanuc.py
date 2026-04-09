from enum import IntEnum

class CgtpProgramType(IntEnum):
	'''Type of a TP program on the controller.'''
	Tp = 1 # TP program
	Karel = 2 # Karel program
