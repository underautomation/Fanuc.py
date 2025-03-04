import typing
from underautomation.fanuc.ftp.variables.ui_config_variable_type import UiConfigVariableType
from underautomation.fanuc.ftp.variables.ui_custom_variable_type import UiCustomVariableType
from underautomation.fanuc.ftp.variables.ui_topmenu_variable_type import UiTopmenuVariableType
from underautomation.fanuc.ftp.variables.ui_usrview_variable_type import UiUsrviewVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SysuifFile as sysuif_file

class SysuifFile(GenericVariableFile):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sysuif_file()
		else:
			self._instance = _internal
	@property
	def ui_config(self) -> UiConfigVariableType:
		return UiConfigVariableType(self._instance.UiConfig)
	@property
	def ui_custom(self) -> typing.List[UiCustomVariableType]:
		return [UiCustomVariableType(x) for x in self._instance.UiCustom]
	@property
	def ui_topmenu(self) -> typing.List[UiTopmenuVariableType]:
		return [UiTopmenuVariableType(x) for x in self._instance.UiTopmenu]
	@property
	def ui_userview(self) -> typing.List[UiUsrviewVariableType]:
		return [UiUsrviewVariableType(x) for x in self._instance.UiUserview]
