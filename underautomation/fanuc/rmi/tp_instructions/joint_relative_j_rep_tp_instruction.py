from __future__ import annotations
import typing
from underautomation.fanuc.rmi.data.rmi_joint_speed_type import RmiJointSpeedType
from underautomation.fanuc.rmi.tp_instructions.j_rep_motion_tp_instruction_base import JRepMotionTpInstructionBase
from UnderAutomation.Fanuc.Rmi.TpInstructions import JointRelativeJRepTpInstruction as joint_relative_j_rep_tp_instruction
from UnderAutomation.Fanuc.Rmi.Data import RmiJointSpeedType as rmi_joint_speed_type

class JointRelativeJRepTpInstruction(JRepMotionTpInstructionBase):
	'''Instruction for an incremental joint motion (J in TP), joint-angle representation, full options. Pass to RmiInstructionBase).'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = joint_relative_j_rep_tp_instruction()
		else:
			self._instance = _internal

	@property
	def speed_type(self) -> RmiJointSpeedType:
		'''Speed unit (percent override or time).'''
		return RmiJointSpeedType(int(self._instance.SpeedType))

	@speed_type.setter
	def speed_type(self, value: RmiJointSpeedType):
		self._instance.SpeedType = rmi_joint_speed_type(int(value))

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
		if not isinstance(other, JointRelativeJRepTpInstruction):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
