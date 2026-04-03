from enum import IntEnum

class CgtpCommentType(IntEnum):
	'''Type of element whose comment can be read or written via CGTP.'''
	NumericRegister = 1 # Numeric register (R[]).
	PositionRegister = 3 # Position register (PR[]).
	UserAlarm = 4 # User alarm.
	RI = 6 # Robot input.
	RO = 7 # Robot output.
	DI = 8 # Digital input.
	DO = 9 # Digital output.
	GI = 10 # Group input.
	GO = 11 # Group output.
	AI = 12 # Analog input.
	AO = 13 # Analog output.
	StringRegister = 14 # String register (SR[]).
	Flag = 19 # Flag (F[]).
