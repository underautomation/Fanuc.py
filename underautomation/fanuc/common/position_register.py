from __future__ import annotations
import typing
from underautomation.fanuc.common.joint_position_variable import JointPositionVariable
from underautomation.fanuc.common.cartesian_position_variable import CartesianPositionVariable
from UnderAutomation.Fanuc.Common import PositionRegister as position_register

class PositionRegister:
	'''Represents a position register that can hold either a Cartesian or joint position'''
	def __init__(self, jointsPosition: JointPositionVariable, cartesianPosition: CartesianPositionVariable, _internal = 0):
		'''Creates a position register from joint and Cartesian position values'''
		if(_internal == 0):
			self._instance = position_register(jointsPosition._instance if jointsPosition else None, cartesianPosition._instance if cartesianPosition else None)
		else:
			self._instance = _internal

	@staticmethod
	def parse(value: str) -> 'PositionRegister':
		'''Parses a position register from its string representation'''
		__r = position_register.Parse(value)
		return None if __r is None else PositionRegister(None, None, __r)

	@property
	def joints_position(self) -> JointPositionVariable:
		'''Joint position value, if available'''
		__r = self._instance.JointsPosition
		return None if __r is None else JointPositionVariable(None, None, __r)

	@joints_position.setter
	def joints_position(self, value: JointPositionVariable):
		self._instance.JointsPosition = value._instance if value else None

	@property
	def cartesian_position(self) -> CartesianPositionVariable:
		'''Cartesian position value, if available'''
		__r = self._instance.CartesianPosition
		return None if __r is None else CartesianPositionVariable(None, None, __r)

	@cartesian_position.setter
	def cartesian_position(self, value: CartesianPositionVariable):
		self._instance.CartesianPosition = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PositionRegister):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
