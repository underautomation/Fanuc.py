import typing
from underautomation.fanuc.ftp.internal.i_fanuc_content import IFanucContent
from underautomation.fanuc.ftp.list.errall_section_item import ErrallSectionItem
from UnderAutomation.Fanuc.Ftp.List import ErrorList as error_list

class ErrorList(IFanucContent):
	'''Represents the parsed content of the ERRALL.LS error log file'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = error_list()
		else:
			self._instance = _internal

	def filter_active_alarms(self) -> typing.List[ErrallSectionItem]:
		'''Return active alarms among the list of all error items'''
		return [ErrallSectionItem(x) for x in self._instance.FilterActiveAlarms()]

	@property
	def name(self) -> str:
		'''File name (ERRALL.LS)'''
		return self._instance.Name

	@property
	def items(self) -> typing.List[ErrallSectionItem]:
		'''List of all error items (active and history)'''
		return [ErrallSectionItem(x) for x in self._instance.Items]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ErrorList):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
