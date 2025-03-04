import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import T2spdlimVariableType as t2spdlim_variable_type

class T2spdlimVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = t2spdlim_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> bool:
		return self._instance.Enable
	@property
	def use_taskid(self) -> int:
		return self._instance.UseTaskid
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
