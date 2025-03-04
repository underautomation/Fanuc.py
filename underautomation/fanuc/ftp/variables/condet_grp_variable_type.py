import typing
from underautomation.fanuc.ftp.variables.generic_variable_type import GenericVariableType
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Fanuc.dll')))
from UnderAutomation.Fanuc.Ftp.Variables import CondetGrpVariableType as condet_grp_variable_type

class CondetGrpVariableType(GenericVariableType):
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = condet_grp_variable_type()
		else:
			self._instance = _internal
	@property
	def enable(self) -> int:
		return self._instance.Enable
	@property
	def data_type(self) -> int:
		return self._instance.DataType
	@property
	def flag(self) -> int:
		return self._instance.Flag
	@property
	def fanuc_internal_type_name(self) -> str:
		return self._instance.FanucInternalTypeName
