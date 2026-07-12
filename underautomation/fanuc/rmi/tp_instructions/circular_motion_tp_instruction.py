from __future__ import annotations
import typing
from underautomation.fanuc.rmi.data.rmi_linear_speed_type import RmiLinearSpeedType
from underautomation.fanuc.common.cartesian_position_with_user_frame import CartesianPositionWithUserFrame
from underautomation.fanuc.rmi.tp_instructions.cartesian_motion_tp_instruction_base import CartesianMotionTpInstructionBase
from UnderAutomation.Fanuc.Rmi.TpInstructions import CircularMotionTpInstruction as circular_motion_tp_instruction
from UnderAutomation.Fanuc.Rmi.Data import RmiLinearSpeedType as rmi_linear_speed_type

class CircularMotionTpInstruction(CartesianMotionTpInstructionBase):
	'''Instruction for a circular motion (C in TP), Cartesian target representation. Pass to RmiInstructionBase).'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = circular_motion_tp_instruction()
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
	def via(self) -> CartesianPositionWithUserFrame:
		'''Via-point Cartesian position that defines the arc.'''
		return CartesianPositionWithUserFrame(None, None, None, None, None, None, None, None, self._instance.Via)

	@via.setter
	def via(self, value: CartesianPositionWithUserFrame):
		self._instance.Via = value._instance if value else None

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
		'''When true, disables blending with the next instruction.'''
		return self._instance.NoBlend

	@no_blend.setter
	def no_blend(self, value: bool):
		self._instance.NoBlend = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CircularMotionTpInstruction):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
