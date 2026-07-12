from enum import IntEnum

class RmiLinearSpeedType(IntEnum):
	'''Speed type for linear and circular motion commands.'''
	MmSec = 0 # Linear speed in millimeters per second.
	InchMin = 1 # Linear speed in inches per minute.
	Time = 2 # Duration-based speed (0.1-second units).
	MSec = 3 # Duration-based speed in milliseconds.
