from enum import IntEnum

class RobotStatusFlags(IntEnum):
	'''Robot status flags from state packet'''
	ReadyForCommands = 1 # Robot is ready to receive command packets
	CommandReceived = 2 # Robot has received at least one command packet
	SystemReady = 4 # System ready (SYSRDY)
	InMotion = 8 # Robot is in motion
