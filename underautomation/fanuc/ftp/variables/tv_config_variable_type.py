import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TvConfigVariableType as tv_config_variable_type

class TvConfigVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tv_config_variable_type()
		else:
			self._instance = _internal
	@property
	def dbglvl(self) -> int:
		return self._instance.Dbglvl
	@property
	def datatype(self) -> typing.List[int]:
		return self._instance.Datatype
	@property
	def tempint(self) -> typing.List[int]:
		return self._instance.Tempint
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
