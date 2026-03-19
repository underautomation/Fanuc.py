from enum import IntEnum

class SimulationType(IntEnum):
	'''Identifies the type of I/O for which simulation status can be read or written.'''
	DI = 0 # Digital Input.
	DO = 1 # Digital Output.
	RI = 2 # Remote Input.
	RO = 3 # Remote Output.
	WI = 4 # Weld Input.
	WO = 5 # Weld Output.
	WSI = 6 # Wire Stick Input.
	WSO = 7 # Wire Stick Output.
	GI = 8 # Group Input.
	GO = 9 # Group Output.
	AI = 10 # Analog Input.
	AO = 11 # Analog Output.
