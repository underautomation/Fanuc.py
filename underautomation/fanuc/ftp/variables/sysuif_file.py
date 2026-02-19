import typing
from underautomation.fanuc.ftp.variables.ui_config_variable_type import UiConfigVariableType
from underautomation.fanuc.ftp.variables.ui_custom_variable_type import UiCustomVariableType
from underautomation.fanuc.ftp.variables.ui_topmenu_variable_type import UiTopmenuVariableType
from underautomation.fanuc.ftp.variables.ui_usrview_variable_type import UiUsrviewVariableType
from underautomation.fanuc.ftp.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Ftp.Variables import SysuifFile as sysuif_file

class SysuifFile(GenericVariableFile):
	'''Describes the Fanuc variable file sysuif.va'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = sysuif_file()
		else:
			self._instance = _internal

	@property
	def ui_config(self) -> UiConfigVariableType:
		'''Value of variable $UI_CONFIG'''
		return UiConfigVariableType(self._instance.UiConfig)

	@property
	def ui_custom(self) -> typing.List[UiCustomVariableType]:
		'''Value of variable $UI_CUSTOM'''
		return [UiCustomVariableType(x) for x in self._instance.UiCustom]

	@property
	def ui_topmenu(self) -> typing.List[UiTopmenuVariableType]:
		'''Value of variable $UI_TOPMENU'''
		return [UiTopmenuVariableType(x) for x in self._instance.UiTopmenu]

	@property
	def ui_userview(self) -> typing.List[UiUsrviewVariableType]:
		'''Value of variable $UI_USERVIEW'''
		return [UiUsrviewVariableType(x) for x in self._instance.UiUserview]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SysuifFile):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
