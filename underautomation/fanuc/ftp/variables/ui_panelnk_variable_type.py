import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import UiPanelnkVariableType as ui_panelnk_variable_type

class UiPanelnkVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ui_panelnk_variable_type()
		else:
			self._instance = _internal
	@property
	def help_url(self) -> typing.List[str]:
		return self._instance.HelpUrl
	@property
	def hlp_context(self) -> typing.List[int]:
		return self._instance.HlpContext
	@property
	def help_flag(self) -> typing.List[int]:
		return self._instance.HelpFlag
	@property
	def relv_index(self) -> int:
		return self._instance.RelvIndex
	@property
	def relv_url(self) -> typing.List[str]:
		return self._instance.RelvUrl
	@property
	def relv_mtext(self) -> typing.List[str]:
		return self._instance.RelvMtext
	@property
	def relv_contex(self) -> typing.List[int]:
		return self._instance.RelvContex
	@property
	def relv_flags(self) -> typing.List[int]:
		return self._instance.RelvFlags
	@property
	def relv_spid(self) -> typing.List[int]:
		return self._instance.RelvSpid
	@property
	def relv_scid(self) -> typing.List[int]:
		return self._instance.RelvScid
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
