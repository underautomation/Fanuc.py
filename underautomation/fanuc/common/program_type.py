from enum import IntEnum

class ProgramType(IntEnum):
	'''Represents the type of a program.'''
	Unknown = 0 # The program type is unknown.
	Karel = 1 # The program is a Karel program, also known as PC (Programmable Control).
	TP = 2 # The program is a TP (Teach Pendant) program.
