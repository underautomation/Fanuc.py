import typing
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
from UnderAutomation.Fanuc.Rmi.Data import RmiTimedResponse as rmi_timed_response

class RmiTimedResponse(RmiResponseBase):
	'''Base class for responses with a controller TimeTag value.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_timed_response()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def time_tag(self) -> int:
		'''Controller time tick for the data sample.'''
		return self._instance.TimeTag

	@time_tag.setter
	def time_tag(self, value: int):
		self._instance.TimeTag = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiTimedResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
