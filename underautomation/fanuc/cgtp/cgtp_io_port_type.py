from enum import IntEnum

class CgtpIoPortType(IntEnum):
	'''Type of I/O port on the controller.'''
	DI = 1 # Digital input.
	DO = 2 # Digital output.
	AI = 3 # Analog input.
	AO = 4 # Analog output.
	RI = 8 # Robot input.
	RO = 9 # Robot output.
	GI = 18 # Group input.
	GO = 19 # Group output.
	Flag = 35 # Flag.
