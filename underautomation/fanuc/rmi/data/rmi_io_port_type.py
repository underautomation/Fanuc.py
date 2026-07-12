from enum import IntEnum

class RmiIoPortType(IntEnum):
	'''IO port type for generic read/write operations.'''
	DI = 0 # Digital Input.
	DO = 1 # Digital Output.
	AI = 2 # Analog Input.
	AO = 3 # Analog Output.
	GO = 4 # Group Output.
	RO = 5 # Robot Output.
	FLAG = 6 # Internal flag register.
	RI = 7 # Robot Input.
	UI = 8 # User Interface Input.
	UO = 9 # User Interface Output.
