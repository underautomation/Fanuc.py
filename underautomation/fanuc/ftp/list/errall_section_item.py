import typing
from datetime import datetime, timedelta
from UnderAutomation.Fanuc.Ftp.List import ErrallSectionItem as errall_section_item

class ErrallSectionItem:
	'''Represents a single error item from the ERRALL error log'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = errall_section_item()
		else:
			self._instance = _internal

	def equals(self, obj: typing.Any) -> bool:
		return self._instance.Equals(obj)

	def get_hash_code(self) -> int:
		return self._instance.GetHashCode()

	@property
	def id(self) -> int:
		'''Error entry identifier'''
		return self._instance.Id

	@property
	def text(self) -> str:
		'''Raw text of the error entry'''
		return self._instance.Text

	@property
	def error_code(self) -> str:
		'''Parsed error code (e.g. "SRVO-001")'''
		return self._instance.ErrorCode

	@property
	def message(self) -> str:
		'''Error message description'''
		return self._instance.Message

	@property
	def occurring_time(self) -> datetime:
		'''Date and time when the error occurred'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.OccurringTime.Ticks // 10)

	@property
	def is_reset(self) -> bool:
		'''Indicates whether this entry is a RESET marker'''
		return self._instance.IsReset

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ErrallSectionItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
