import typing
from underautomation.fanuc.ftp.variables.com_space_variable_type import ComSpaceVariableType
from underautomation.fanuc.ftp.variables.gp_hold_variable_type import GpHoldVariableType
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import RspacegVariableType as rspaceg_variable_type

class RspacegVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rspaceg_variable_type()
		else:
			self._instance = _internal
	@property
	def com_space(self) -> typing.List[ComSpaceVariableType]:
		return [ComSpaceVariableType(x) for x in self._instance.ComSpace]
	@property
	def gp_hold(self) -> typing.List[GpHoldVariableType]:
		return [GpHoldVariableType(x) for x in self._instance.GpHold]
	@property
	def spare_int(self) -> typing.List[int]:
		return self._instance.SpareInt
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
