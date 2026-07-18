from __future__ import annotations
import typing
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
from UnderAutomation.Fanuc.Rmi.Data import RmiControllerErrorTextResponse as rmi_controller_error_text_response

class RmiControllerErrorTextResponse(RmiResponseBase):
	'''Result of reading the most recent controller error text.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rmi_controller_error_text_response()
		else:
			self._instance = _internal

	@property
	def error_data_entries(self) -> typing.List[str]:
		'''Error entries in the form XXXX-NNN (up to 5 entries).'''
		return self._instance.ErrorDataEntries

	@error_data_entries.setter
	def error_data_entries(self, value: typing.List[str]):
		self._instance.ErrorDataEntries = value

	@property
	def error_data(self) -> str:
		'''First error entry, or an empty string when none.'''
		return self._instance.ErrorData

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RmiControllerErrorTextResponse):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
