from enum import IntEnum

class StreamMotionError(IntEnum):
	'''Kind of Stream Motion error'''
	NotConnected = 0 # The client is not connected
	NotMonitoring = 1 # The robot status output is not started (call StartMonitoring)
	NoStatus = 2 # No status was received from the robot
	VersionMismatch = 3 # The robot uses another protocol version than the one requested
	SessionActive = 4 # The operation is not allowed while a session is active
	SourceBusy = 5 # Another source of positions is active
	FormatMismatch = 6 # The position format does not match the format of the session. A session uses only one format: call finish() and use the other format in the next session.
	CycleTimeMismatch = 7 # The trajectory was sampled with a period that is not the communication cycle of the robot
	StartMismatch = 8 # The first position of the trajectory is too far from the position where it starts
	LimitsUnavailable = 9 # The robot did not send its limits
	SessionEnded = 10 # The session ended before the end of the operation
	CallbackFailed = 11 # The callback did not give a position
	CommunicationError = 12 # Error during the communication with the robot
	NotTracking = 13 # The target tracking is not started (call StartTracking)
