from enum import IntEnum

class IoPortType(IntEnum):
	'''Type of I/O port on the controller.'''
	DI = 1
	DO = 2
	AI = 3
	AO = 4
	RI = 8
	RO = 9
	GI = 18
	GO = 19
	Flag = 35
