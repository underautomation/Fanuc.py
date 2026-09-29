from enum import IntEnum

class TerminationType(IntEnum):
	'''Type of termination of a motion'''
	Stop = 0 # The robot stops at the target position
	Overlap = 1 # The next motion starts during the deceleration of this one. The corner is rounded, more at high speed. Between linear and circular motions, the corner is replaced by a smooth curve that starts where the robot would start to decelerate (overlap of 100%), or closer to the target.
	Corner = 2 # Corner region: the corner is replaced by a smooth curve that starts and ends at a given distance from the target position. The speed stays constant in the curve, and is reduced when its curvature needs it. Only between Cartesian motions.
