from __future__ import annotations
import typing
from underautomation.fanuc.rmi.tp_instructions.rmi_instruction_base import RmiInstructionBase
from UnderAutomation.Fanuc.Rmi.TpInstructions import CallProgramTpInstruction as call_program_tp_instruction

class CallProgramTpInstruction(RmiInstructionBase):
	'''Instruction for a CALL program instruction. Pass to RmiInstructionBase). Requires MajorVersion >= 4.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = call_program_tp_instruction()
		else:
			self._instance = _internal

	@property
	def program_name(self) -> str:
		'''Name of the TP program to call.'''
		return self._instance.ProgramName

	@program_name.setter
	def program_name(self, value: str):
		self._instance.ProgramName = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CallProgramTpInstruction):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
