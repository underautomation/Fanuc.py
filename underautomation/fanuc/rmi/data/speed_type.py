from enum import IntEnum

class SpeedType(IntEnum):
	'''Speed type selector for motion commands.'''
	MmSec = 0 # Linear speed in millimeters per second.
	InchMin = 1 # Linear speed in inches per minute.
	Time = 2 # Duration-based speed (0.1 seconds unit for Linear/Circular, milliseconds for Joint).
	Percent = 3 # Joint speed as percentage of maximum.
