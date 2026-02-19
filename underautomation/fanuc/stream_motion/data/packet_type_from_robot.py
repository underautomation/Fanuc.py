from enum import IntEnum

class PacketTypeFromRobot(IntEnum):
	'''Stream Motion packet types for Robot to PC communication'''
	State = 0 # Robot state/status packet
	Ack = 3 # Acknowledgment packet (response to Request)
