import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DynBrkVariableType as dyn_brk_variable_type

class DynBrkVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dyn_brk_variable_type()
		else:
			self._instance = _internal
	@property
	def di_idx(self) -> int:
		return self._instance.DiIdx
	@property
	def do_idx(self) -> int:
		return self._instance.DoIdx
	@property
	def brk_msk(self) -> int:
		return self._instance.BrkMsk
	@property
	def fltr_if(self) -> int:
		return self._instance.FltrIf
	@property
	def use_opdi(self) -> bool:
		return self._instance.UseOpdi
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
