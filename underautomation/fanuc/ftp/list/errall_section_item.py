import typing
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
		return self._instance.ToString()
	@property
	def is_reset(self) -> bool:
		return self._instance.IsReset
	@property
	def id(self) -> int:
		return self._instance.Id
	@id.setter
	def id(self, value: int):
		self._instance.Id = value
	@property
	def text(self) -> str:
		return self._instance.Text
	@text.setter
	def text(self, value: str):
		self._instance.Text = value
