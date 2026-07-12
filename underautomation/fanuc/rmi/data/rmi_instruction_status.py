from enum import IntEnum

class RmiInstructionStatus(IntEnum):
	'''Execution state of an RMI instruction in the pipeline.'''
	LocalQueued = 0 # The instruction is held in the local client buffer and has not been sent to the controller yet.
	ControllerQueued = 1 # The instruction has been sent to the controller and is waiting in its 8-slot execution queue.
	Executing = 2 # The controller is currently executing this instruction.
	Completed = 3 # The instruction completed without error.
	Error = 4 # The instruction ended with a controller error or was cancelled. Check ErrorId.
