from enum import IntEnum

class ThresholdType(IntEnum):
	'''Threshold types for request packets'''
	Velocity = 0 # Velocity threshold (deg/s)
	Acceleration = 1 # Acceleration threshold (deg/s²)
	Jerk = 2 # Jerk threshold (deg/s³)
