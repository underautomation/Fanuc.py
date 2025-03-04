import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import DsblFaultVariableType as dsbl_fault_variable_type

class DsblFaultVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = dsbl_fault_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def max_count(self) -> int:
		return self._instance.MaxCount
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
