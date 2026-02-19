import typing
from underautomation.fanuc.common.cartesian_position import CartesianPosition
from UnderAutomation.Fanuc.Ftp.Variables import CartesianPositionVariable as cartesian_position_variable

class CartesianPositionVariable(CartesianPosition):
	'''Represents a Cartesian position variable parsed from a Fanuc variable file'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cartesian_position_variable()
		else:
			self._instance = _internal

	@staticmethod
	def parse(value: str) -> 'CartesianPositionVariable':
		'''Parses a Cartesian position from its string representation'''
		return CartesianPositionVariable(cartesian_position_variable.Parse(value))

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def group(self) -> int:
		'''Motion group number'''
		return self._instance.Group

	@group.setter
	def group(self, value: int):
		self._instance.Group = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CartesianPositionVariable):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
