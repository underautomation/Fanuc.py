import typing
from underautomation.fanuc.ftp.variables.generic_field import GenericField
from UnderAutomation.Fanuc.Ftp.Variables import ArrayElement as array_element

class ArrayElement(GenericField):
	'''Describes all elements inside an array. Basically, a wrapping of GenericField where some properties are inherited from it'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = array_element()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def access(self) -> str:
		'''Parent Access'''
		return self._instance.Access

	@property
	def type(self) -> str:
		'''Parent Type'''
		return self._instance.Type

	@property
	def is_register(self) -> bool:
		'''Parent IsRegister'''
		return self._instance.IsRegister

	@property
	def string_length(self) -> int:
		'''Parent StringLength'''
		return self._instance.StringLength

	@property
	def name(self) -> str:
		'''Element index, example : [1] or [2,1]'''
		return self._instance.Name

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ArrayElement):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
