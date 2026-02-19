import typing
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
from UnderAutomation.Fanuc.Rmi.Data import RmiSequenceResponse as rmi_sequence_response

class RmiSequenceResponse(RmiResponseBase):
	'''Base class for responses that include a sequence identifier.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_sequence_response()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def sequence_id(self) -> int:
		'''Echoed SequenceID of the instruction that completed.'''
		return self._instance.SequenceId

	@sequence_id.setter
	def sequence_id(self, value: int):
		self._instance.SequenceId = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiSequenceResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
