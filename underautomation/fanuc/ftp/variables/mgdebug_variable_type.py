import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import MgdebugVariableType as mgdebug_variable_type

class MgdebugVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mgdebug_variable_type()
		else:
			self._instance = _internal
	@property
	def debugmask(self) -> int:
		return self._instance.Debugmask
	@property
	def maxdata(self) -> int:
		return self._instance.Maxdata
	@property
	def count(self) -> int:
		return self._instance.Count
	@property
	def tail(self) -> int:
		return self._instance.Tail
	@property
	def bufexist(self) -> bool:
		return self._instance.Bufexist
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
