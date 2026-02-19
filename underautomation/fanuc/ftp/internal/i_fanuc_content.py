import typing
from UnderAutomation.Fanuc.Ftp.Internal import IFanucContent as i_fanuc_content

class IFanucContent:
	'''Interface of a file that comes from a Fanuc controller'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = i_fanuc_content()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''File name'''
		return self._instance.Name

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IFanucContent):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
