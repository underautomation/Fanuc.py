from __future__ import annotations
import typing
from underautomation.fanuc.rmi.data.rmi_linear_speed_type import RmiLinearSpeedType
from underautomation.fanuc.rmi.tp_instructions.cartesian_motion_tp_instruction_base import CartesianMotionTpInstructionBase
from UnderAutomation.Fanuc.Rmi.TpInstructions import LinearMotionTpInstruction as linear_motion_tp_instruction
from UnderAutomation.Fanuc.Rmi.Data import RmiLinearSpeedType as rmi_linear_speed_type

class LinearMotionTpInstruction(CartesianMotionTpInstructionBase):
	'''Instruction for a linear motion (L in TP), Cartesian target representation. Pass to RmiInstructionBase).'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = linear_motion_tp_instruction()
		else:
			self._instance = _internal

	@property
	def speed_type(self) -> RmiLinearSpeedType:
		'''Speed unit (mm/s, inch/min, or time).'''
		return RmiLinearSpeedType(int(self._instance.SpeedType))

	@speed_type.setter
	def speed_type(self, value: RmiLinearSpeedType):
		self._instance.SpeedType = rmi_linear_speed_type(int(value))

	@property
	def wrist_joint(self) -> bool:
		'''When true, enables wrist-joint mode for this motion.'''
		return self._instance.WristJoint

	@wrist_joint.setter
	def wrist_joint(self, value: bool):
		self._instance.WristJoint = value

	@property
	def mrot(self) -> bool:
		'''When true, enables coordinated motion (MROT).'''
		return self._instance.Mrot

	@mrot.setter
	def mrot(self, value: bool):
		self._instance.Mrot = value

	@property
	def no_blend(self) -> bool:
		'''When true, disables blending with the next instruction. Requires MajorVersion >= 5.'''
		return self._instance.NoBlend

	@no_blend.setter
	def no_blend(self, value: bool):
		self._instance.NoBlend = value

	@property
	def alim(self) -> int | None:
		'''Acceleration limit value. null uses the controller default. Requires MajorVersion >= 5 and the R921 option.'''
		return self._instance.Alim

	@alim.setter
	def alim(self, value: int | None):
		self._instance.Alim = value

	@property
	def alim_reg(self) -> int | None:
		'''Acceleration limit register number. null disables register-based limit. Requires MajorVersion >= 5 and the R921 option.'''
		return self._instance.AlimReg

	@alim_reg.setter
	def alim_reg(self, value: int | None):
		self._instance.AlimReg = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, LinearMotionTpInstruction):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
