import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CollectVariableType as collect_variable_type

class CollectVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = collect_variable_type()
		else:
			self._instance = _internal
	@property
	def multi_prog(self) -> bool:
		return self._instance.MultiProg
	@property
	def allow_proc(self) -> bool:
		return self._instance.AllowProc
	@property
	def fstchildren(self) -> bool:
		return self._instance.Fstchildren
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
