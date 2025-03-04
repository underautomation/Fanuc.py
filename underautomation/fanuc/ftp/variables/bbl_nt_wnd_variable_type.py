import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import BblNtWndVariableType as bbl_nt_wnd_variable_type

class BblNtWndVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = bbl_nt_wnd_variable_type()
		else:
			self._instance = _internal
	@property
	def wnd_top(self) -> int:
		return self._instance.WndTop
	@property
	def wnd_left(self) -> int:
		return self._instance.WndLeft
	@property
	def wnd_bottom(self) -> int:
		return self._instance.WndBottom
	@property
	def wnd_right(self) -> int:
		return self._instance.WndRight
	@property
	def brdr_clr(self) -> int:
		return self._instance.BrdrClr
	@property
	def bckgrnd_clr(self) -> int:
		return self._instance.BckgrndClr
	@property
	def text_clr(self) -> int:
		return self._instance.TextClr
	@property
	def brdr_width(self) -> int:
		return self._instance.BrdrWidth
	@property
	def disptime(self) -> int:
		return self._instance.Disptime
	@property
	def flags(self) -> int:
		return self._instance.Flags
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
