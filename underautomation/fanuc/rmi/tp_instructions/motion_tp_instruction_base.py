from __future__ import annotations
import typing
from underautomation.fanuc.rmi.data.rmi_termination_type import RmiTerminationType
from underautomation.fanuc.rmi.tp_instructions.rmi_instruction_base import RmiInstructionBase
from UnderAutomation.Fanuc.Rmi.TpInstructions import MotionTpInstructionBase as motion_tp_instruction_base
from UnderAutomation.Fanuc.Rmi.Data import RmiTerminationType as rmi_termination_type

class MotionTpInstructionBase(RmiInstructionBase):
	'''Base class for all RMI motion instructions. Carries the three parameters that are mandatory on every motion instruction.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = motion_tp_instruction_base()
		else:
			self._instance = _internal

	@property
	def speed(self) -> int:
		'''Speed value whose unit is defined by the concrete subclass.'''
		return self._instance.Speed

	@speed.setter
	def speed(self, value: int):
		self._instance.Speed = value

	@property
	def term_type(self) -> RmiTerminationType:
		'''Termination type (FINE, CNT, or CR).'''
		return RmiTerminationType(int(self._instance.TermType))

	@term_type.setter
	def term_type(self, value: RmiTerminationType):
		self._instance.TermType = rmi_termination_type(int(value))

	@property
	def term_value(self) -> int:
		'''Termination value (0 for FINE, 1-100 for CNT, radius for CR).'''
		return self._instance.TermValue

	@term_value.setter
	def term_value(self, value: int):
		self._instance.TermValue = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MotionTpInstructionBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
