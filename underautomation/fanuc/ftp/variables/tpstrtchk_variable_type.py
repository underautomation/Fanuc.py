import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import TpstrtchkVariableType as tpstrtchk_variable_type

class TpstrtchkVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = tpstrtchk_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def allow_name(self) -> str:
		return self._instance.AllowName
	@property
	def allow_line(self) -> int:
		return self._instance.AllowLine
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
