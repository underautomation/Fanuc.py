from enum import IntEnum

class KCLPorts(IntEnum):
	'''Enum representing the different KCL ports.'''
	DIN = 0 # Digital Input port.
	DOUT = 1 # Digital Output port.
	RDO = 2 # Robot Digital Output port.
	OPOUT = 3 # Operator Panel Output port.
	TPOUT = 4 # Teach Pendant Output port.
	WDI = 5 # Weld Digital Input port.
	WDO = 6 # Weld Digital Output port.
	AIN = 7 # Analog Input port.
	AOUT = 8 # Analog Output port.
	GIN = 9 # General Input port.
	GOUT = 10 # General Output port.
