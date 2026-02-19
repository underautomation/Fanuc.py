from enum import IntEnum

class PacketTypeToRobot(IntEnum):
	'''Stream Motion packet types for PC to Robot communication'''
	Start = 0 # Start streaming motion
	Command = 1 # Motion command packet
	Stop = 2 # Stop streaming motion
	Request = 3 # Request threshold information
