import typing
from UnderAutomation.Fanuc.Ftp.Diagnosis import Feature as feature

class Feature:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = feature()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def name(self) -> str:
		'''Name of the feature'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def order_no(self) -> str:
		'''Order number of the feature (set of 4 alphanumeric characters)'''
		return self._instance.OrderNo

	@order_no.setter
	def order_no(self, value: str):
		self._instance.OrderNo = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Feature):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
