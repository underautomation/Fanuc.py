import typing
from UnderAutomation.Fanuc.Ftp.Variables import VectorVariable as vector_variable

class VectorVariable:
	'''Represents a 3D vector variable with X, Y, Z components'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = vector_variable()
		else:
			self._instance = _internal

	@staticmethod
	def parse(value: str) -> 'VectorVariable':
		'''Parses a vector variable from its string representation'''
		return VectorVariable(vector_variable.Parse(value))

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def x(self) -> float:
		'''X component of the vector'''
		return self._instance.X

	@x.setter
	def x(self, value: float):
		self._instance.X = value

	@property
	def y(self) -> float:
		'''Y component of the vector'''
		return self._instance.Y

	@y.setter
	def y(self, value: float):
		self._instance.Y = value

	@property
	def z(self) -> float:
		'''Z component of the vector'''
		return self._instance.Z

	@z.setter
	def z(self, value: float):
		self._instance.Z = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, VectorVariable):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
