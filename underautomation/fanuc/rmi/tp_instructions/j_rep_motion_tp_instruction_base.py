from __future__ import annotations
import typing
from underautomation.fanuc.common.joints_position import JointsPosition
from underautomation.fanuc.rmi.tp_instructions.full_motion_tp_instruction_base import FullMotionTpInstructionBase
from UnderAutomation.Fanuc.Rmi.TpInstructions import JRepMotionTpInstructionBase as j_rep_motion_tp_instruction_base

class JRepMotionTpInstructionBase(FullMotionTpInstructionBase):
	'''Extends FullMotionTpInstructionBase with a joint-angle target. Base class for all joint-representation motion instruction types.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = j_rep_motion_tp_instruction_base()
		else:
			self._instance = _internal

	@property
	def joints(self) -> JointsPosition:
		'''Target joint angles in degrees.'''
		return JointsPosition(None, None, None, None, None, None, None, None, None, self._instance.Joints)

	@joints.setter
	def joints(self, value: JointsPosition):
		self._instance.Joints = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JRepMotionTpInstructionBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
