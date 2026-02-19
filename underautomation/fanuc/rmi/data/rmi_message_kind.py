from enum import IntEnum

class RmiMessageKind(IntEnum):
	'''Identifies the top-level message kind sent to the controller. Must be the first key according to the RMI protocol.'''
	Communication = 0 # Communication packet (FRC_Connect / FRC_Disconnect).
	Command = 1 # Administrative command (e.g., FRC_Initialize, FRC_Reset).
	Instruction = 2 # Instruction that appends a new TP line to the RMI_MOVE program.
