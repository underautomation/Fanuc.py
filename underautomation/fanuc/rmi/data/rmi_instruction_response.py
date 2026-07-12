from __future__ import annotations
import typing
from underautomation.fanuc.rmi.data.rmi_instruction_status import RmiInstructionStatus
from underautomation.fanuc.rmi.tp_instructions.rmi_instruction_base import RmiInstructionBase
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
from UnderAutomation.Fanuc.Rmi.Data import RmiInstructionResponse as rmi_instruction_response
from UnderAutomation.Fanuc.Rmi.Data import RmiInstructionStatus as rmi_instruction_status

class RmiInstructionResponse(RmiResponseBase):
	'''Response returned immediately when a motion instruction is queued. The Status property and ErrorId are updated in the background as the controller processes the instruction. Use Int32) to block until the instruction reaches a terminal state.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_instruction_response()
		else:
			self._instance = _internal

	def status_changed(self, handler):
		class Wrapper :
			def __init__(self, _internal):
				self._instance = _internal
		self._instance.StatusChanged+= lambda obj : handler(Wrapper(obj))

	def wait_for_completion(self, timeoutMs: int=-1) -> bool:
		'''Blocks the calling thread until the instruction reaches a terminal state (Completed or Error), or until timeoutMs milliseconds have elapsed. Pass -1 (or omit) to wait indefinitely.

		:param timeoutMs: Maximum time to wait in milliseconds, or -1 to wait indefinitely.
		:returns: True when the instruction reached a terminal state; false on timeout.
		'''
		return self._instance.WaitForCompletion(timeoutMs)

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def sequence_id(self) -> int:
		'''Sequence identifier assigned to this instruction. 0 until the instruction has been dispatched to the controller.'''
		return self._instance.SequenceId

	@property
	def status(self) -> RmiInstructionStatus:
		'''Current execution state of the instruction.'''
		return RmiInstructionStatus(int(self._instance.Status))

	@property
	def instruction(self) -> RmiInstructionBase:
		'''Sent instruction'''
		return RmiInstructionBase(self._instance.Instruction)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiInstructionResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
