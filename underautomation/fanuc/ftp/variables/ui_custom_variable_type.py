import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import UiCustomVariableType as ui_custom_variable_type

class UiCustomVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ui_custom_variable_type()
		else:
			self._instance = _internal
	@property
	def start_spid(self) -> int:
		return self._instance.StartSpid
	@property
	def start_scid(self) -> int:
		return self._instance.StartScid
	@property
	def config_page(self) -> typing.List[str]:
		return self._instance.ConfigPage
	@property
	def device_page(self) -> typing.List[str]:
		return self._instance.DevicePage
	@property
	def screen_def(self) -> typing.List[int]:
		return self._instance.ScreenDef
	@property
	def config_pane(self) -> typing.List[int]:
		return self._instance.ConfigPane
	@property
	def flags(self) -> typing.List[int]:
		return self._instance.Flags
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
