from __future__ import annotations
import typing
from UnderAutomation.Fanuc.Rmi.TpInstructions import RmiInstructionBase as rmi_instruction_base

class RmiInstructionBase:
	'''Base class for all RMI TP instructions. Pass an instance to RmiInstructionBase) to queue the instruction on the controller.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_instruction_base()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiInstructionBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
