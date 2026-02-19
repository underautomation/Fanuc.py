from enum import IntEnum

class TerminationType(IntEnum):
	'''Termination type for motion.'''
	Fine = 0 # FINE termination; precise stop.
	Cnt = 1 # Continuous termination; blend motions (1-100).
	Cr = 2 # Constant path mode (requires option).
