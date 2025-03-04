import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import ErNoautoVariableType as er_noauto_variable_type

class ErNoautoVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = er_noauto_variable_type()
		else:
			self._instance = _internal
	@property
	def noauto_enb(self) -> bool:
		return self._instance.NoautoEnb
	@property
	def noauto_num(self) -> int:
		return self._instance.NoautoNum
	@property
	def ps_noauto_c(self) -> int:
		return self._instance.PsNoautoC
	@property
	def noauto_code(self) -> typing.List[int]:
		return self._instance.NoautoCode
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
