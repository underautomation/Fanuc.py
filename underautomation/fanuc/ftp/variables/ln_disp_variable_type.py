import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import LnDispVariableType as ln_disp_variable_type

class LnDispVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ln_disp_variable_type()
		else:
			self._instance = _internal
	@property
	def hide_line_n(self) -> bool:
		return self._instance.HideLineN
	@property
	def disp_menu(self) -> bool:
		return self._instance.DispMenu
	@property
	def hide_parln(self) -> bool:
		return self._instance.HideParln
	@property
	def hide_dauln(self) -> bool:
		return self._instance.HideDauln
	@property
	def head_parent(self) -> str:
		return self._instance.HeadParent
	@property
	def head_daught(self) -> str:
		return self._instance.HeadDaught
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
