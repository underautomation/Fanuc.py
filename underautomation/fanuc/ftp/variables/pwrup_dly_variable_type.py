import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import PwrupDlyVariableType as pwrup_dly_variable_type

class PwrupDlyVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = pwrup_dly_variable_type()
		else:
			self._instance = _internal
	@property
	def delay_time(self) -> int:
		return self._instance.DelayTime
	@property
	def sy_ready(self) -> bool:
		return self._instance.SyReady
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
