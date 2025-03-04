import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TvOutputVariableType as tv_output_variable_type

class TvOutputVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tv_output_variable_type()
		else:
			self._instance = _internal
	@property
	def selected(self) -> typing.List[str]:
		return self._instance.Selected
	@property
	def datatype(self) -> typing.List[int]:
		return self._instance.Datatype
	@property
	def state(self) -> typing.List[str]:
		return self._instance.State
	@property
	def cmd_status(self) -> typing.List[int]:
		return self._instance.CmdStatus
	@property
	def tempint(self) -> typing.List[int]:
		return self._instance.Tempint
	@property
	def selectedmod(self) -> typing.List[str]:
		return self._instance.Selectedmod
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
