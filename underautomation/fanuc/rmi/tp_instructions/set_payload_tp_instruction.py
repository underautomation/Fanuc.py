from __future__ import annotations
import typing
from underautomation.fanuc.rmi.tp_instructions.rmi_instruction_base import RmiInstructionBase
from UnderAutomation.Fanuc.Rmi.TpInstructions import SetPayloadTpInstruction as set_payload_tp_instruction

class SetPayloadTpInstruction(RmiInstructionBase):
	'''Instruction for a PAYLOAD[n] schedule selection. Pass to RmiInstructionBase).'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = set_payload_tp_instruction()
		else:
			self._instance = _internal

	@property
	def schedule_number(self) -> int:
		'''Payload schedule number to activate.'''
		return self._instance.ScheduleNumber

	@schedule_number.setter
	def schedule_number(self, value: int):
		self._instance.ScheduleNumber = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SetPayloadTpInstruction):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
