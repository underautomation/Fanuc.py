from enum import IntEnum

class RmiJointSpeedType(IntEnum):
	'''Speed type for joint motion commands.'''
	Percent = 0 # Joint speed as a percentage of maximum (1–100 %).
	Time = 1 # Duration-based speed (0.1-second units).
	MSec = 2 # Duration-based speed in milliseconds.
