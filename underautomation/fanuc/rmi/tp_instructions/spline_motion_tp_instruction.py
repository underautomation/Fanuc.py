from __future__ import annotations
import typing
from underautomation.fanuc.rmi.data.rmi_linear_speed_type import RmiLinearSpeedType
from underautomation.fanuc.rmi.tp_instructions.cartesian_motion_tp_instruction_base import CartesianMotionTpInstructionBase
from UnderAutomation.Fanuc.Rmi.TpInstructions import SplineMotionTpInstruction as spline_motion_tp_instruction
from UnderAutomation.Fanuc.Rmi.Data import RmiLinearSpeedType as rmi_linear_speed_type

class SplineMotionTpInstruction(CartesianMotionTpInstructionBase):
	'''Instruction for a spline motion with a Cartesian target. Pass to RmiInstructionBase). Requires MajorVersion >= 7.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = spline_motion_tp_instruction()
		else:
			self._instance = _internal

	@property
	def speed_type(self) -> RmiLinearSpeedType:
		'''Speed unit (mm/s, inch/min, or time).'''
		return RmiLinearSpeedType(int(self._instance.SpeedType))

	@speed_type.setter
	def speed_type(self, value: RmiLinearSpeedType):
		self._instance.SpeedType = rmi_linear_speed_type(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SplineMotionTpInstruction):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
