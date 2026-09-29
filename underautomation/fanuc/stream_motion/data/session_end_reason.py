from enum import IntEnum

class SessionEndReason(IntEnum):
	'''Reason of the end of a Stream Motion session'''
	Finished = 0 # The session was finished normally. The program continues after the IBGN end instruction.
	ProgramStopped = 1 # The robot left the IBGN start instruction before the end of the session: program stopped, aborted, or alarm on the robot.
	StatusLost = 2 # No status was received from the robot during the configured timeout
	Disconnected = 3 # The client was disconnected
