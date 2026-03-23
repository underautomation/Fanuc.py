from enum import IntEnum

class CommentType(IntEnum):
	'''Identifies the type of data for which a comment can be read or written.'''
	Register = 0 # Numeric register R[].
	PositionRegister = 1 # Position register PR[].
	StringRegister = 2 # String register SR[].
	DI = 3 # Digital Input.
	DO = 4 # Digital Output.
	RI = 5 # Remote Input.
	RO = 6 # Remote Output.
	UI = 7 # User Input.
	UO = 8 # User Output.
	SI = 9 # System Input.
	SO = 10 # System Output.
	WI = 11 # Weld Input.
	WO = 12 # Weld Output.
	WSI = 13 # Wire Stick Input.
	WSO = 14 # Wire Stick Output.
	GI = 15 # Group Input.
	GO = 16 # Group Output.
	AI = 17 # Analog Input.
	AO = 18 # Analog Output.
	Flag = 19 # Flag
