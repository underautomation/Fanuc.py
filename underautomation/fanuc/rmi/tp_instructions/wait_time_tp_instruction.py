from __future__ import annotations
import typing
from underautomation.fanuc.rmi.tp_instructions.rmi_instruction_base import RmiInstructionBase
from UnderAutomation.Fanuc.Rmi.TpInstructions import WaitTimeTpInstruction as wait_time_tp_instruction

class WaitTimeTpInstruction(RmiInstructionBase):
	'''Instruction for a WAIT t (sec) time delay. Pass to RmiInstructionBase).'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = wait_time_tp_instruction()
		else:
			self._instance = _internal

	@property
	def seconds(self) -> float:
		'''Duration to wait, in seconds.'''
		return self._instance.Seconds

	@seconds.setter
	def seconds(self, value: float):
		self._instance.Seconds = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, WaitTimeTpInstruction):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
