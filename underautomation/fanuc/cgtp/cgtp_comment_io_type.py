from enum import IntEnum

class CgtpCommentIoType(IntEnum):
	'''Type of I/O pair whose comments can be read via CGTP.'''
	RobotIO = 32 # Robot I/O (RI/RO).
	DigitalIO = 33 # Digital I/O (DI/DO).
	GroupIO = 34 # Group I/O (GI/GO).
	AnalogIO = 35 # Analog I/O (AI/AO).
