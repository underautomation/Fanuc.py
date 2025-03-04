import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DryrunPortVariableType as dryrun_port_variable_type

class DryrunPortVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dryrun_port_variable_type()
		else:
			self._instance = _internal
	@property
	def type(self) -> int:
		return self._instance.Type
	@property
	def fst_idx(self) -> int:
		return self._instance.FstIdx
	@property
	def lst_idx(self) -> int:
		return self._instance.LstIdx
	@property
	def static_port(self) -> bool:
		return self._instance.StaticPort
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
