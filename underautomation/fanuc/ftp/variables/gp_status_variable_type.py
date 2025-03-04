import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import GpStatusVariableType as gp_status_variable_type

class GpStatusVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = gp_status_variable_type()
		else:
			self._instance = _internal
	@property
	def in_use(self) -> bool:
		return self._instance.InUse
	@property
	def space_num(self) -> int:
		return self._instance.SpaceNum
	@property
	def priority(self) -> int:
		return self._instance.Priority
	@property
	def status1(self) -> int:
		return self._instance.Status1
	@property
	def status2(self) -> int:
		return self._instance.Status2
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
