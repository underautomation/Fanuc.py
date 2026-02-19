from enum import IntEnum

class DigitalPorts(IntEnum):
	'''Fanuc digital port types'''
	DIN = 0 # Digital input
	DOUT = 1 # Digital outputs
	UI = 2 # User inputs
	UO = 3 # User outputs
	SI = 4 # SI
	SO = 5 # SO
	RI = 6 # Robot inputs
	RO = 7 # Robot outputs
	FLG = 8 # Flags
