import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import SnpxAsgVariableType as snpx_asg_variable_type

class SnpxAsgVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = snpx_asg_variable_type()
		else:
			self._instance = _internal
	@property
	def address(self) -> int:
		return self._instance.Address
	@property
	def size(self) -> int:
		return self._instance.Size
	@property
	def var_name(self) -> str:
		return self._instance.VarName
	@property
	def multiply(self) -> float:
		return self._instance.Multiply
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
