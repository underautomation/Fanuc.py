from enum import IntEnum

class ProgramSubType(IntEnum):
	'''Sub-type of a TP program on the controller.'''
	Job = 1 # Job program.
	Process = 2 # Process program.
	Macro = 3 # Macro program.
	Condition = 4 # Condition handler program.
