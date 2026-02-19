import typing
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
from UnderAutomation.Fanuc.Rmi.Data import ControllerErrorText as controller_error_text

class ControllerErrorText(RmiResponseBase):
	'''Result of reading the most recent error text.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = controller_error_text()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def error_data(self) -> str:
		'''Controller error text in the form XXXX-NNN.'''
		return self._instance.ErrorData

	@error_data.setter
	def error_data(self, value: str):
		self._instance.ErrorData = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ControllerErrorText):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
