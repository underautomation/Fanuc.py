import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PocfgVariableType as pocfg_variable_type

class PocfgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pocfg_variable_type()
		else:
			self._instance = _internal
	@property
	def podebug(self) -> int:
		return self._instance.Podebug
	@property
	def overrun_tol(self) -> typing.List[int]:
		return self._instance.OverrunTol
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
