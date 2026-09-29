from enum import IntEnum

class StreamMotionState(IntEnum):
	'''State of a Stream Motion client'''
	Disconnected = 0 # The client is not connected
	Connected = 1 # The client is connected but the robot does not send its status (call StartMonitoring)
	Monitoring = 2 # The robot sends its status, but no program is waiting on an IBGN start instruction
	Ready = 3 # A program is waiting on an IBGN start instruction and the robot accepts positions
	Streaming = 4 # Positions are sent to the robot every communication cycle
	Finishing = 5 # The last position was sent. The client waits for the robot to leave the IBGN start instruction.
