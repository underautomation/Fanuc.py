from enum import IntEnum

class IOType(IntEnum):
	'''I/O types supported by Stream Motion protocol'''
	DI = 1 # Digital Input
	DO = 2 # Digital Output
	RI = 8 # Robot Input
	RO = 9 # Robot Output
	SI = 11 # System Input
	SO = 12 # System Output
	WI = 16 # Weld Input
	WO = 17 # Weld Output
	UI = 20 # User Input
	UO = 21 # User Output
	WSI = 26 # Weld System Input
	WSO = 27 # Weld System Output
	F = 35 # Flag
	M = 36 # Marker
