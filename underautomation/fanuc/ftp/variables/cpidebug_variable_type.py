import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CpidebugVariableType as cpidebug_variable_type

class CpidebugVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = cpidebug_variable_type()
		else:
			self._instance = _internal
	@property
	def output(self) -> int:
		return self._instance.Output
	@property
	def filename(self) -> str:
		return self._instance.Filename
	@property
	def group_mask(self) -> int:
		return self._instance.GroupMask
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
