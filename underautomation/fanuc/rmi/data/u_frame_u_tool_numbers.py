import typing
from underautomation.fanuc.rmi.data.rmi_response_base import RmiResponseBase
from UnderAutomation.Fanuc.Rmi.Data import UFrameUToolNumbers as u_frame_u_tool_numbers

class UFrameUToolNumbers(RmiResponseBase):
	'''Current UFRAME and UTOOL numbers.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = u_frame_u_tool_numbers()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def u_frame_number(self) -> int:
		'''Current user frame number.'''
		return self._instance.UFrameNumber

	@u_frame_number.setter
	def u_frame_number(self, value: int):
		self._instance.UFrameNumber = value

	@property
	def u_tool_number(self) -> int:
		'''Current user tool number.'''
		return self._instance.UToolNumber

	@u_tool_number.setter
	def u_tool_number(self, value: int):
		self._instance.UToolNumber = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, UFrameUToolNumbers):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
