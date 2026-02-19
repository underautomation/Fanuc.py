from enum import IntEnum

class TpCoordinates(IntEnum):
	'''Enumeration of TP (Teach Pendant) coordinate systems.'''
	Unknown = -1 # Unknown coordinate system.
	Tool = 0 # Tool coordinate system.
	User = 1 # User coordinate system.
	Joint = 2 # Joint coordinate system.
	JogFrame = 3 # Jog frame coordinate system.
	World = 4 # World coordinate system.
