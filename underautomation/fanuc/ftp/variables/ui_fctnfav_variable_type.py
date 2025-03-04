import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import UiFctnfavVariableType as ui_fctnfav_variable_type

class UiFctnfavVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ui_fctnfav_variable_type()
		else:
			self._instance = _internal
	@property
	def pwd_spid(self) -> int:
		return self._instance.PwdSpid
	@property
	def pwd_scid(self) -> int:
		return self._instance.PwdScid
	@property
	def press_text(self) -> str:
		return self._instance.PressText
	@property
	def press_icon(self) -> str:
		return self._instance.PressIcon
	@property
	def press_ptr(self) -> int:
		return self._instance.PressPtr
	@property
	def releas_text(self) -> str:
		return self._instance.ReleasText
	@property
	def releas_icon(self) -> str:
		return self._instance.ReleasIcon
	@property
	def releas_ptr(self) -> int:
		return self._instance.ReleasPtr
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
