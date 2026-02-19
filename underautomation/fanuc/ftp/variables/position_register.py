import typing
from underautomation.fanuc.ftp.variables.joint_position_variable import JointPositionVariable
from underautomation.fanuc.ftp.variables.cartesian_position_variable import CartesianPositionVariable
from UnderAutomation.Fanuc.Ftp.Variables import PositionRegister as position_register

class PositionRegister:
	'''Represents a position register that can hold either a Cartesian or joint position'''
	def __init__(self, jointsPosition: JointPositionVariable, cartesianPosition: CartesianPositionVariable, _internal = 0):
		'''Creates a position register from joint and Cartesian position values'''
		if(_internal == 0):
			self._instance = position_register(jointsPosition, cartesianPosition)
		else:
			self._instance = _internal

	@staticmethod
	def parse(value: str) -> 'PositionRegister':
		'''Parses a position register from its string representation'''
		return PositionRegister(None, None, position_register.Parse(value))

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def joints_position(self) -> JointPositionVariable:
		'''Joint position value, if available'''
		return JointPositionVariable(self._instance.JointsPosition)

	@joints_position.setter
	def joints_position(self, value: JointPositionVariable):
		self._instance.JointsPosition = value._instance if value else None

	@property
	def cartesian_position(self) -> CartesianPositionVariable:
		'''Cartesian position value, if available'''
		return CartesianPositionVariable(self._instance.CartesianPosition)

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
