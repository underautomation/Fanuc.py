from __future__ import annotations
import typing
from underautomation.fanuc.common.cartesian_position_with_user_frame import CartesianPositionWithUserFrame
from underautomation.fanuc.rmi.tp_instructions.full_motion_tp_instruction_base import FullMotionTpInstructionBase
from UnderAutomation.Fanuc.Rmi.TpInstructions import CartesianMotionTpInstructionBase as cartesian_motion_tp_instruction_base

class CartesianMotionTpInstructionBase(FullMotionTpInstructionBase):
	'''Extends FullMotionTpInstructionBase with a Cartesian target position. Base class for all Cartesian motion instruction types.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cartesian_motion_tp_instruction_base()
		else:
			self._instance = _internal

	@property
	def target(self) -> CartesianPositionWithUserFrame:
		'''Target Cartesian position, configuration, and active frame/tool numbers.'''
		return CartesianPositionWithUserFrame(None, None, None, None, None, None, None, None, self._instance.Target)

	@target.setter
	def target(self, value: CartesianPositionWithUserFrame):
		self._instance.Target = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CartesianMotionTpInstructionBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
