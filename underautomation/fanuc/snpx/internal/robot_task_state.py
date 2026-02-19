from enum import IntEnum

class RobotTaskState(IntEnum):
	'''Represents the execution state of a robot task.'''
	Stopped = 0 # Task is stopped.
	Paused = 1 # Task is paused.
	Running = 2 # Task is running.
