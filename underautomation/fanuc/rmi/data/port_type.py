from enum import IntEnum

class PortType(IntEnum):
	'''Digital port type used with Local Condition Block (LCB).'''
	DOUT = 1 # Digital Output (DO/DOUT).
	ROUT = 2 # Robot Output (RO/ROUT).
