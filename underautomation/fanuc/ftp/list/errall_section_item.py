import typing
from datetime import datetime, timedelta
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.List import ErrallSectionItem as errall_section_item

class ErrallSectionItem:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = errall_section_item()
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString() if self._instance is not None else ""
	@property
	def id(self) -> int:
		return self._instance.Id
	@property
	def text(self) -> str:
		return self._instance.Text
	@property
	def error_code(self) -> str:
		return self._instance.ErrorCode
	@property
	def message(self) -> str:
		return self._instance.Message
	@property
	def occurring_time(self) -> datetime:
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.OccurringTime.Ticks // 10)
	@property
	def is_reset(self) -> bool:
		return self._instance.IsReset
