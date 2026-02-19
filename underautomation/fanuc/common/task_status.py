from enum import IntEnum

class TaskStatus(IntEnum):
	'''Represents the status of a task.'''
	Unknown = 0 # The task status is unknown.
	Running = 1 # The task is running.
	Paused = 2 # The task is paused.
	Aborted = 3 # The task is aborted.
