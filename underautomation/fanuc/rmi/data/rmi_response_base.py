import typing
from UnderAutomation.Fanuc.Rmi.Data import RmiResponseBase as rmi_response_base

class RmiResponseBase:
	'''Base class for RMI responses that return an error id from the controller.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_response_base()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def error_id(self) -> int:
		'''Error identifier. 0 means success; non-zero indicates a controller error.'''
		return self._instance.ErrorId

	@error_id.setter
	def error_id(self, value: int):
		self._instance.ErrorId = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiResponseBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
