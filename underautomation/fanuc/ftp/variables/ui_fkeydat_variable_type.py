import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import UiFkeydatVariableType as ui_fkeydat_variable_type

class UiFkeydatVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = ui_fkeydat_variable_type()
		else:
			self._instance = _internal
	@property
	def enb_color(self) -> typing.List[int]:
		return self._instance.EnbColor
	@property
	def ps_backcolo(self) -> int:
		return self._instance.PsBackcolo
	@property
	def backcolor(self) -> typing.List[int]:
		return self._instance.Backcolor
	@property
	def forecolor(self) -> typing.List[int]:
		return self._instance.Forecolor
	@property
	def label(self) -> typing.List[str]:
		return self._instance.Label
	@property
	def icon(self) -> typing.List[str]:
		return self._instance.Icon
	@property
	def url(self) -> typing.List[str]:
		return self._instance.Url
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
