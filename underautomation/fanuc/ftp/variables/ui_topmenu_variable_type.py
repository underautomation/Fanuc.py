import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import UiTopmenuVariableType as ui_topmenu_variable_type

class UiTopmenuVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ui_topmenu_variable_type()
		else:
			self._instance = _internal
	@property
	def pwd_access(self) -> int:
		return self._instance.PwdAccess
	@property
	def dummy8(self) -> int:
		return self._instance.Dummy8
	@property
	def dummy(self) -> int:
		return self._instance.Dummy
	@property
	def title(self) -> str:
		return self._instance.Title
	@property
	def label(self) -> str:
		return self._instance.Label
	@property
	def text(self) -> typing.List[str]:
		return self._instance.Text
	@property
	def icon(self) -> typing.List[str]:
		return self._instance.Icon
	@property
	def url(self) -> typing.List[str]:
		return self._instance.Url
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
