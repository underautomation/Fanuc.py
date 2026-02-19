from enum import IntEnum

class SegmentName(IntEnum):
	'''Identifies the type of I/O segment.'''
	SDI = 0 # Safety Digital Input.
	SDO = 1 # Safety Digital Output.
	RDI = 2 # Remote Digital Input.
	RDO = 3 # Remote Digital Output.
	UI = 4 # User Input.
	UO = 5 # User Output.
	SI = 6 # System Input.
	SO = 7 # System Output.
	WI = 8 # Weld Input.
	WO = 9 # Weld Output.
	WSI = 10 # Wire Stick Input.
	PMC_K = 11 # PMC Keep Relay.
	PMC_R = 12 # PMC Internal Relay.
	AI = 13 # Analog Input.
	AO = 14 # Analog Output.
	GI = 15 # Group Input.
	GO = 16 # Group Output.
	PMC_D = 17 # PMC Data Table.
