import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import KarelmonVariableType as karelmon_variable_type

class KarelmonVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = karelmon_variable_type()
		else:
			self._instance = _internal
	@property
	def xref_once(self) -> bool:
		return self._instance.XrefOnce
	@property
	def watch_var(self) -> bool:
		return self._instance.WatchVar
	@property
	def prog_name(self) -> str:
		return self._instance.ProgName
	@property
	def field_name(self) -> str:
		return self._instance.FieldName
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
