from enum import IntEnum

class KinematicsCategory(IntEnum):
	'''Category of kinematics model for a robot arm.'''
	Invalid = 0 # Invalid or unsupported kinematics configuration.
	Crx = 1 # CRX collaborative robot kinematics.
	Opw = 2 # OPW (ortho-parallel wrist) kinematics for standard industrial robots.
