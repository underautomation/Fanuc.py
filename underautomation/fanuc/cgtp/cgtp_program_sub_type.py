from enum import IntEnum

class CgtpProgramSubType(IntEnum):
	'''Sub-type of a TP program on the controller.'''
	None_ = 0 # No specific sub-type.
	Job = 1 # Job program.
	Process = 2 # Process program.
	Macro = 3 # Macro program.
	Condition = 4 # Condition handler program.
