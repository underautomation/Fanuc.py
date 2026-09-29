from enum import IntEnum

class LimitType(IntEnum):
	'''Type of limit of a robot axis'''
	Velocity = 0 # Velocity limit, in deg/s (mm/s for linear axes)
	Acceleration = 1 # Acceleration limit, in deg/s² (mm/s² for linear axes)
	Jerk = 2 # Jerk limit, in deg/s³ (mm/s³ for linear axes)
