from __future__ import annotations
import typing
from underautomation.fanuc.common.files.variables.ui_config_variable_type import UiConfigVariableType
from underautomation.fanuc.common.files.variables.ui_custom_variable_type import UiCustomVariableType
from underautomation.fanuc.common.files.variables.ui_topmenu_variable_type import UiTopmenuVariableType
from underautomation.fanuc.common.files.variables.ui_usrview_variable_type import UiUsrviewVariableType
from underautomation.fanuc.common.files.variables.generic_variable_file import GenericVariableFile
from UnderAutomation.Fanuc.Common.Files.Variables import SysuifFile as sysuif_file

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
		__r = self._instance.UiConfig
		return None if __r is None else UiConfigVariableType(__r)

	@property
	def ui_custom(self) -> typing.List[UiCustomVariableType]:
		'''Value of variable $UI_CUSTOM'''
		__r = self._instance.UiCustom
		return None if __r is None else [None if x is None else UiCustomVariableType(x) for x in __r]

	@property
	def ui_topmenu(self) -> typing.List[UiTopmenuVariableType]:
		'''Value of variable $UI_TOPMENU'''
		__r = self._instance.UiTopmenu
		return None if __r is None else [None if x is None else UiTopmenuVariableType(x) for x in __r]

	@property
	def ui_userview(self) -> typing.List[UiUsrviewVariableType]:
		'''Value of variable $UI_USERVIEW'''
		__r = self._instance.UiUserview
		return None if __r is None else [None if x is None else UiUsrviewVariableType(x) for x in __r]

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
